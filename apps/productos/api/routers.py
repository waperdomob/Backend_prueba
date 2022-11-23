from rest_framework.routers import DefaultRouter

from apps.productos.api.viewsets.general_views import *
from apps.productos.api.viewsets.producto_views import *
from apps.productos.api.viewsets.input_views import *
from apps.productos.api.viewsets.output_views import *



router = DefaultRouter()

router.register(r'productos',ProductoViewSet, basename = 'productos')
router.register(r'categorias',categoriaViewset, basename = 'categorias')
router.register(r'subCategorias',subCategoriaViewset, basename = 'subCategorias')
router.register(r'sucursales', sucursalViewset, basename='sucursales')
router.register(r'inputs',InputViewSet, basename = 'entradas')
router.register(r'outputs',OutputViewSet, basename = 'salidas')


urlpatterns = router.urls