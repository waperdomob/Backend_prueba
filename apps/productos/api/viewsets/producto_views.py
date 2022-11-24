
from datetime import timedelta

from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.parsers import (FileUploadParser, FormParser,
                                    MultiPartParser)
from rest_framework.response import Response

from apps.productos.api.serializers.producto_serializers import \
    ProductoSerializer


class ProductoViewSet(viewsets.ModelViewSet):
    serializer_class = ProductoSerializer

    def get_queryset(self, pk=None):
        model = self.get_serializer().Meta.model
        if pk == None:
            return (
                model.objects.filter(state=True)
                .prefetch_related("subCategoria")
            )
        else:
            return (
                model.objects.filter(state=True)
                .filter(id=pk)
                .prefetch_related("subCategoria")
                .first()
            )

    def list(self, request):
        producto_serializer = self.serializer_class(self.get_queryset(), many=True)
        data = {
            "total": self.get_queryset().count(),
            "productos": producto_serializer.data,
        }
        return Response(data, status=status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):
        parser_classes = [MultiPartParser, FormParser]
        Producto_serializer = ProductoSerializer(data=request.data)

        if Producto_serializer.is_valid():
            Producto_serializer.save(state=True)

            return Response(
                {"message": "Producto agregado con exito!"}, status=status.HTTP_200_OK
            )
        return Response(Producto_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        producto = self.get_queryset(pk)
        if producto:
            producto_serializer = self.serializer_class(producto)
            return Response(producto_serializer.data, status=status.HTTP_200_OK)
        return Response(
            {"error": "No existe un producto con estos datos!"},
            status=status.HTTP_400_BAD_REQUEST,
        )

    def update(self, request, pk=None):
        parser_classes = [MultiPartParser, FormParser]
        if self.get_queryset(pk):
            producto_serializer = ProductoSerializer(self.get_queryset(pk), data=request.data)
            if producto_serializer.is_valid():
                producto_serializer.save(
                    state=True,
                )
                return Response(producto_serializer.data, status=status.HTTP_200_OK)
            return Response(producto_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk):
        producto = self.get_queryset().filter(id=pk).first()
        if producto:
            producto.state = False
            producto.save()
            return Response(
                {"message": "Producto eliminado correctamente!"}, status=status.HTTP_200_OK
            )
        return Response(
            {"error": "No existe un video con estos datos!"},
            status=status.HTTP_400_BAD_REQUEST,
        )

