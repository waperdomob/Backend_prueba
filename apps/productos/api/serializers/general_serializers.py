from rest_framework import serializers

from apps.productos.models import Categoria, Sucursal, subCategoria


class subCategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = subCategoria
        fields = "__all__"

class CategoriaSerializer(serializers.ModelSerializer):
    categoria = subCategoriaSerializer
    class Meta:
        model = Categoria
        fields = "__all__"

class sucursalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sucursal
        fields = "__all__"



