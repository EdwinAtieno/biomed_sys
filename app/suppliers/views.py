from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)

from app.suppliers.models import (
    ContactPerson,
    Supplier,
)
from app.suppliers.permissions import IsBioMedorAdmin
from app.suppliers.serializers import (
    ContactPersonSerializer,
    SupplierSerializer,
)


class SupplierList(ListCreateAPIView):
    """
    List all suppliers or create a new supplier
    """

    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer
    permission_classes = (IsBioMedorAdmin,)


class SupplierDetail(RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a supplier instance.
    """

    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer
    permission_classes = (IsBioMedorAdmin,)


class ContactPersonList(ListCreateAPIView):
    """
    List all contact persons or create a new contact person
    """

    queryset = ContactPerson.objects.all()
    serializer_class = ContactPersonSerializer
    permission_classes = (IsBioMedorAdmin,)


class ContactPersonDetail(RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a contact person instance.
    """

    queryset = ContactPerson.objects.all()
    serializer_class = ContactPersonSerializer
    permission_classes = (IsBioMedorAdmin,)
