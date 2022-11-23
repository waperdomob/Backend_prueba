from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.parsers import (FileUploadParser, FormParser,
                                    MultiPartParser)
from rest_framework.response import Response

from apps.productos.api.serializers.input_serializers import InputSerializer
from apps.productos.models import Producto, input


class InputViewSet(viewsets.ModelViewSet):
    serializer_class = InputSerializer
    # permission_classes = [IsAuthenticatedOrReadOnly]

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
        input_serializer = self.serializer_class(self.get_queryset(), many=True)
        data = {
            "total": self.get_queryset().count(),
            "inputs": input_serializer.data,
        }
        return Response(data, status=status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):
        parser_classes = [MultiPartParser, FormParser]
        serializer = InputSerializer(data=request.data)

        if serializer.is_valid():
            producto = Producto.objects.filter( id = request.data['producto']).first()
            if producto:
                stock = producto.stock + int(request.data['cantidad'])
                producto.stock = stock
                producto.save()
            else:
                producto= serializer.validated_data.get('producto')
                producto.save()
            
            serializer.save()
            
            return Response(
                {"message": "Entrada registrada con exito!"}, status=status.HTTP_200_OK
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        input = self.get_queryset(pk)
        if input:
            input_serializer = self.serializer_class(input)
            return Response(input_serializer.data, status=status.HTTP_200_OK)
        return Response(
            {"error": "No existe una entrada con estos datos!"},
            status=status.HTTP_400_BAD_REQUEST,
        )

    def update(self, request, pk=None):
        parser_classes = [MultiPartParser, FormParser]
        if self.get_queryset(pk):
            input_serializer = InputSerializer(self.get_queryset(pk), data=request.data)
            if input_serializer.is_valid():
                input_serializer.save()
                return Response(input_serializer.data, status=status.HTTP_200_OK)
            return Response(input_serializer.errors, status=status.HTTP_400_BAD_REQUEST)



