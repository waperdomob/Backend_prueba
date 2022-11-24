from django.contrib import admin

from apps.productos.models import *

# Register your models here.

class categoriaAdmin(admin.ModelAdmin):
    list_display = ('id','categoria')
class subCategoriAdmin(admin.ModelAdmin):
    list_display = ('id','subcategoria')

class sucursalAdmin(admin.ModelAdmin):
    list_display = ('id','sucursal')

class productoAdmin(admin.ModelAdmin):
    list_display = ('id','producto')

admin.site.register(Categoria,categoriaAdmin)
admin.site.register(subCategoria,subCategoriAdmin)
admin.site.register(Sucursal,sucursalAdmin)
admin.site.register(Producto, productoAdmin)
