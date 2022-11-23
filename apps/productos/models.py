from django.conf import settings
from django.db import models
from django.forms import model_to_dict

from apps.users.models import User

# Create your models here.

CATEGORIAS = [
    ('Materiales para construcción ','Materiales para construcción '),
    ('Materiales de seguridad','Materiales de seguridad'),
    ('Materiales para decoración del hogar ','Materiales para decoración del hogar '),
    ('Herramientas','Herramientas'),
    ('Repuestos para electrodomésticos','Repuestos para electrodomésticos')
]
SUBCATEGORIAS = [
    ('Materiales para pisos','Materiales para pisos'),
    ('Materiales para baños','Materiales para baños'),
    ('Materiales para cocina','Materiales para cocina'),
    ('Materiales para patio','Materiales para patio'),
    ('Seguridad para la construcción ','Seguridad para la construcción '),
    ('Seguridad Eléctrica ','Seguridad Eléctrica '),
    ('Seguridad en el campo','Seguridad en el campo'),
    ('Herramientas eléctricas','Herramientas eléctricas'),
    ('Herramientas inalámbricas','Herramientas inalámbricas'),
    ('Repuestos para televisores','Repuestos para televisores'),
    ('Repuestos para neveras','Repuestos para neveras'),
    ('Repuestos para lavadoras','Repuestos para lavadoras'),
    ('Repuestos para estufas','Repuestos para estufas'),
]

SUCURSALES = [
    ('La Ferretería - Sucursal Norte','La Ferretería - Sucursal Norte'),
    ('La Ferretería - Sucursal Noreste','La Ferretería - Sucursal Noreste'),
    ('La Ferretería - Sucursal Noroccidente','La Ferretería - Sucursal Noroccidente'),
]


class Categoria(models.Model):
    categoria= models.CharField(max_length=45,choices=CATEGORIAS)
    def __str__(self):
        return self.categoria

class subCategoria(models.Model):
    subcategoria= models.CharField(max_length=45,choices=SUBCATEGORIAS)
    categoria=models.ForeignKey(Categoria,null=True,blank=True, on_delete=models.CASCADE)
    def __str__(self):
        return self.subcategoria
class Sucursal(models.Model):
    sucursal= models.CharField(max_length=45,choices=SUCURSALES)
    def __str__(self):
        return self.sucursal

class Producto(models.Model):
    codigo=models.CharField(max_length=45,null=True, blank=True)
    producto=models.CharField(max_length=45)
    descripcion = models.CharField(max_length=100, null=True, blank=True)
    stock=models.IntegerField()
    precio_compra=models.FloatField(max_length=45)
    precio_venta=models.FloatField(max_length=20)
    state = models.BooleanField('Estado',default = True)
    imagen=models.ImageField(upload_to='productos/', null=True, blank=True)
    subCategoria=models.ForeignKey(subCategoria,null=True, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.producto

class input(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE,  blank=True, null=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    cantidad = models.IntegerField(blank=True, null=True)
    fecha = models.DateField(null=True, blank=True, auto_now=True)
    def __str__(self):
        return self.producto.producto
        
class output(models.Model):

    producto = models.ForeignKey(Producto, on_delete=models.CASCADE,  blank=True, null=True)
    sucursal = models.ForeignKey(Sucursal, on_delete=models.CASCADE,  blank=True, null=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    cantidad = models.IntegerField(blank=True, null=True)
    fecha = models.DateField(null=True, blank=True, auto_now=True)
    def __str__(self):
        return self.producto.producto
        
