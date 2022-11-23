from rest_framework import serializers

from apps.productos.api.serializers.general_serializers import \
    sucursalSerializer
from apps.productos.api.serializers.producto_serializers import \
    ProductoSerializer
from apps.productos.models import output
from apps.users.api.serializers.user_serializers import UserSerializer


class OutputSerializer(serializers.ModelSerializer):
    usuario = UserSerializer
    producto = ProductoSerializer
    sucursal = sucursalSerializer
    class Meta:
        model = output
        fields = "__all__"