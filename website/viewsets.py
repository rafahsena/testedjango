from rest_framework import viewsets
from rest_framework import generics, mixins
from .models import *
from .serializers import *
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly, BasePermission
from website.recommender import recommender
from django.http import Http404
from rest_framework.filters import BaseFilterBackend
import coreapi
import coreschema
from rest_framework.schemas import AutoSchema
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from .filters import *
from .schema_view import CustomSchema
tag_schema = AutoSchema(manual_fields=[coreapi.Field('tags', required=False,
                                                     location='query',
                                                     description='Categorias dos produtos(separadas por virgulas).',
                                                     schema=coreschema.String(),
                                                     )
                                       ])


def list_response(viewset, model_serializer, qs, request):
    page = viewset.paginate_queryset(qs)
    if page is not None:
        serializer = model_serializer(
            page, many=True, context={"request": request})
        return viewset.get_paginated_response(serializer.data)
    serializer = viewset.get_serializer(qs, many=True)
    return Response(serializer.data)


class IsOwnerdOrCreateOnly(BasePermission):
    """
    The request is authenticated as a user, or is a read-only request.
    """

    def has_object_permission(self, request, view, obj):
        return request.method == 'POST' or obj.user == request.user


class EnderecoViewSet(viewsets.ModelViewSet):
    """

    Endpoint relacionado aos endereços.

    """
    serializer_class = EnderecoSerializer
    queryset = Endereco.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly,)

    @action(methods=['get'], detail=True)
    def clientes(self, request, pk):
        """

        Obter os clientes que possuem um determinado endereço.

        """
        cliente = Cliente.objects.get(pk=pk)
        serializer_data = VendaSerializer(cliente.vendas.all(), many=True).data
        return Response(serializer_data)


class ClienteViewSet(viewsets.ModelViewSet):
    """

    Endpoint relacionado aos clientes.

    """
    serializer_class = ClienteSerializer
    queryset = Cliente.objects.all()
    permission_classes = [IsOwnerdOrCreateOnly]

    @action(methods=['get'], detail=True)
    def vendas(self, request, pk):
        """
        Obter vendas relacionadas a um determinado cliente.
        """
        try:
            cliente = Cliente.objects.get(pk=pk)
            return list_response(self, VendaSerializer, cliente.vendas.all(), request)
        except models.ObjectDoesNotExist:
            raise Http404

    @action(methods=['get'], detail=True)
    def lojas(self, request, pk):
        """
        Obter lojas recomendadas para um usuário.
        """
        try:
            lojasId = recommender.get_topk_lojas(int(pk))
            lojas = [Loja.objects.get(id=lojaId) for lojaId in lojasId]
            return list_response(self, LojaSerializer, lojas, request)
        except models.ObjectDoesNotExist:
            raise Http404

    @action(methods=['get'], detail=True)
    def avaliacoes(self, request, pk):
        try:
            cliente = Cliente.objects.get(pk=pk)
            serializer_data = AvaliacaoSerializer(
                cliente.avaliacoes_cliente.all(), many=True, context={"request": request}).data
            return Response(serializer_data)
        except models.ObjectDoesNotExist:
            raise Http404


class LojaViewSet(viewsets.ModelViewSet):
    """
    Endpoint relacionado as lojas.
    """
    serializer_class = LojaSerializer
    queryset = Loja.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly,)
    filter_backends = [DjangoFilterBackend,
                       filters.SearchFilter]
    search_fields = ['nome_fantasia']

    @action(methods=['get'], detail=True, schema=tag_schema)
    def produtos(self, request, pk):
        """
        Produtos de uma loja
        """
        try:
            loja = self.get_queryset().get(pk=pk)
            slugs = request.GET.get('tags', None)
            if slugs:
                slugs = slugs.split(',')
                categorias = loja.categorias.filter(slug__in=slugs)
                qs = loja.produtos.filter(categorias__in=categorias).distinct()
            else:
                qs = loja.produtos.all()
            return list_response(self, ProdutoSerializer, qs, request)
        except models.ObjectDoesNotExist:
            raise Http404

    @action(methods=['get'], detail=True)
    def avaliacoes(self, request, pk):
        """
        Obter as avaliações de uma loja.
        """
        try:
            loja = self.get_queryset().get(pk=pk)
        except models.ObjectDoesNotExist:
            raise Http404
        qs = loja.avaliacoes_loja.all()
        return list_response(self, AvaliacaoSerializer, qs, request)

    @action(methods=['get'], detail=True)
    def categorias(self, request, pk):
        """
        Obter as categorias de uma loja.
        """
        try:
            loja = self.get_queryset().get(pk=pk)
        except models.ObjectDoesNotExist:
            raise Http404
        qs = loja.categorias.all()
        return Response(CategoriaSerializer(
            qs, many=True, context={"request": request}).data)


class ProdutoViewSet(mixins.CreateModelMixin,
                     mixins.ListModelMixin,
                     mixins.RetrieveModelMixin,
                     mixins.UpdateModelMixin,
                     viewsets.GenericViewSet):

    """


    Endpoint relacionado aos produtos.


    """
    schema = CustomSchema()
    serializer_class = ProdutoSerializer
    queryset = Produto.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def list(self, request, *args, **kwargs):
        """
        ---
        desc:
         Listar produtos.
        input:
        - name: tags
          desc: Categorias dos produtos(separadas por virgulas).
          type: string
          required: false
          location: query
        """

        queryset = self.filter_queryset(self.get_queryset())
        slugs = request.GET.get('tags', None)
        if slugs:
            slugs = slugs.split(',')
            categorias = Categoria.objects.filter(slug__in=slugs)
            queryset = queryset.filter(categorias__in=categorias).distinct()
        return list_response(self, self.get_serializer, queryset, request)


class VendaViewSet(mixins.CreateModelMixin,
                   mixins.ListModelMixin,
                   mixins.RetrieveModelMixin,
                   viewsets.GenericViewSet):

    """
    Endpoint relacionado as vendas.
    """
    serializer_class = VendaSerializer
    queryset = Venda.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly,)


class AvaliacaoViewSet(mixins.CreateModelMixin,
                       mixins.ListModelMixin,
                       mixins.RetrieveModelMixin,
                       viewsets.GenericViewSet):

    serializer_class = AvaliacaoSerializer
    queryset = Avaliacao.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly,)


class CategoriaViewSet(viewsets.ModelViewSet):
    serializer_class = CategoriaSerializer
    queryset = Categoria.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly,)
    pagination_class = None
