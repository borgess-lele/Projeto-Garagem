from django.contrib import admin
from django.urls import include, path

from rest_framework.routers import DefaultRouter

from garagem.views import CategoriaViewSet, MarcaViewSet, CorViewSet, AcessorioViewSet, VeiculoViewSet

router = DefaultRouter()
router.register(r"acessorios", AcessorioViewSet)
router.register(r"Marca", MarcaViewSet)
router.register(r"categorias", CategoriaViewSet)
router.register(r"cores", CorViewSet)
router.register(r"veiculos", VeiculoViewSet)


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(router.urls)),
]
