from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import ModelViewSet
from atracoes.models import Atracao
from .serializers import AtracaoSerializer

from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class AtracaoViewSet(ModelViewSet):
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    # Apenas se estiver autenticado: IsAuthenticated
    # Apenas se for administrador: IsAdminUser
    # Autenticado ou acesso somente à leitura (GET): IsAuthenticatedOrReadOnly
    permission_classes = (IsAuthenticatedOrReadOnly,)

    queryset = Atracao.objects.all()
    serializer_class = AtracaoSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('nome', 'descricao')
