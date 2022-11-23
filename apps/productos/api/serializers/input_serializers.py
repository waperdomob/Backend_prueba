from rest_framework import serializers

from apps.productos.api.serializers.producto_serializers import \
    ProductoSerializer
from apps.productos.models import input
from apps.users.api.serializers.user_serializers import UserSerializer


class InputSerializer( serializers.ModelSerializer):
    usuario = UserSerializer
    producto = ProductoSerializer
    class Meta:
        model = input
        fields = "__all__"