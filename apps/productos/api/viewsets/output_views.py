from datetime import timedelta

from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.parsers import (FileUploadParser, FormParser,
                                    MultiPartParser)
from rest_framework.response import Response

from apps.productos.api.serializers.output_serializers import OutputSerializer
from apps.productos.models import Producto, output


class OutputViewSet(viewsets.ModelViewSet):
    serializer_class = OutputSerializer

    def get_queryset(self, pk=None):
        model = self.get_serializer().Meta.model
        if pk == None:
            return (
                model.objects.all()
            )
        else:
            return (
                model.objects.filter(id=pk)
                .first()
            )

    def list(self, request):
        output_serializer = self.serializer_class(self.get_queryset(), many=True)
        data = {
            "total": self.get_queryset().count(),
            "outputs": output_serializer.data,
        }
        return Response(data, status=status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):
        parser_classes = [MultiPartParser, FormParser]
        serializer = OutputSerializer(data=request.data)
        if serializer.is_valid():
            producto = Producto.objects.filter( id = request.data['producto']).first()
            print(producto)
            if producto:
                stock = producto.stock - int(request.data['cantidad'])
                producto.stock = stock
                producto.save()
            else:
                producto= serializer.validated_data.get('producto')
                producto.save()
            
            serializer.save()
            return Response(
                {"message": "Salida agregada con exito!"}, status=status.HTTP_200_OK
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        output = self.get_queryset(pk)
        if output:
            output_serializer = self.serializer_class(output)
            return Response(output_serializer.data, status=status.HTTP_200_OK)
        return Response(
            {"error": "No existe un output con estos datos!"},
            status=status.HTTP_400_BAD_REQUEST,
        )

    def update(self, request, pk=None):
        parser_classes = [MultiPartParser, FormParser]
        if self.get_queryset(pk):
            output_serializer = OutputSerializer(self.get_queryset(pk), data=request.data)
            if output_serializer.is_valid():
                output_serializer.save()
                return Response(output_serializer.data, status=status.HTTP_200_OK)
            return Response(output_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


