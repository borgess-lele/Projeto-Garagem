from rest_framework.viewsets import ModelViewSet

from garagem.models import Categoria, Cor, Acessorio, Veiculo
from garagem.serializers import CategoriaSerializer, CorSerializer, AcessorioSerializer, VeiculoSerializer

class CategoriaViewSet(ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class CorViewSet(ModelViewSet):
    queryset = Cor.objects.all()
    serializer_class = CorSerializer

class AcessorioViewSet(ModelViewSet):
    queryset = Acessorio.objects.all()
    serializer_class = AcessorioSerializer

class VeiculoViewSet(ModelViewSet):
    queryset = Veiculo.objects.all()
    serializer_class = VeiculoSerializer


