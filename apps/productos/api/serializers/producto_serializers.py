from rest_framework import serializers

from apps.productos.api.serializers.general_serializers import \
    CategoriaSerializer
from apps.productos.models import Producto


#serializer for create and update
class ProductoSerializer(serializers.ModelSerializer):
    categoria = CategoriaSerializer
    class Meta:
        model = Producto
        fields = [
            "id",
            "codigo",
            "producto",
            "descripcion",
            "stock",
            "precio_compra",
            "precio_venta",
            "state",
            "categoria",
        ]


#serializer for list and retrieve
#class ProductoSerializer2(serializers.ModelSerializer):
#    categoria = CategoriaSerializer
#
#    class Meta:
#        model = producto
#        fields = [
#            "id",
#            "codigo",
#            "producto",
#            "descripcion",
#            "stock",
#            "precio_compra",
#            "precio_venta",
#            "state",
#            "categoria",
#        ]