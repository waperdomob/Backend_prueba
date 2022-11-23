from rest_framework import viewsets

from apps.productos.api.serializers.general_serializers import *
from apps.productos.models import Categoria, Sucursal, subCategoria


class categoriaViewset(viewsets.ModelViewSet):

    serializer_class = CategoriaSerializer

    def get_queryset(self):
        queryset = Categoria.objects.all()
        return queryset


class subCategoriaViewset(viewsets.ModelViewSet):

    serializer_class = subCategoriaSerializer

    def get_queryset(self):
        queryset = subCategoria.objects.all()
        return queryset


class sucursalViewset(viewsets.ModelViewSet):
    serializer_class = sucursalSerializer

    def get_queryset(self):
        queryset = Sucursal.objects.all()
        return queryset

