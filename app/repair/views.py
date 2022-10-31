from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from rest_framework.permissions import IsAuthenticated

from app.repair.models import Repair
from app.repair.permissions import IsBioMedorAdmin
from app.repair.serializers import RepairSerializer


class RepairList(ListCreateAPIView):
    queryset = Repair.objects.all()
    permission_classes = (IsAuthenticated, IsBioMedorAdmin)
    serializer_class = RepairSerializer


class RepairDetail(RetrieveUpdateDestroyAPIView):
    queryset = Repair.objects.all()
    permission_classes = (IsAuthenticated, IsBioMedorAdmin)
    serializer_class = RepairSerializer
