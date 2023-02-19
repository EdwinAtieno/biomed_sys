from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveAPIView,
    UpdateAPIView,
)
from rest_framework.permissions import IsAuthenticated

from app.equipments.models import Equipment
from app.equipments.permissions import IsHodorAdmin
from app.equipments.serializers import (
    EquipmentSerializer,
    EquipmentStatusSerializer,
)


class EquipmentList(ListCreateAPIView):
    """
    List all equipments or create a new equipments
    """

    queryset = Equipment.objects.all()
    serializer_class = EquipmentSerializer
    permission_classes = (IsAuthenticated, IsHodorAdmin)


class EquipmentDetail(RetrieveAPIView):
    """
    Retrieve a equipment instance.
    """

    queryset = Equipment.objects.all()
    serializer_class = EquipmentSerializer
    permission_classes = (IsAuthenticated, IsHodorAdmin)


class EquipmentStatusUpdate(UpdateAPIView):
    """
    Update a equipment instance.
    """

    queryset = Equipment.objects.all()
    serializer_class = EquipmentStatusSerializer
    permission_classes = (IsAuthenticated, IsHodorAdmin)
