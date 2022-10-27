from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from rest_framework.permissions import (
    IsAdminUser,
    IsAuthenticated,
)

from .models import (
    Department,
    Section,
)
from .serializers import (
    DepartmentSerializer,
    SectionSerializer,
)


class DepartmentList(ListCreateAPIView):
    """
    List all departments or create a new department.
    """

    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    permission_classes = (IsAuthenticated, IsAdminUser)


class DepartmentDetail(RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a department instance.
    """

    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    permission_classes = (IsAuthenticated, IsAdminUser)


class SectionList(ListCreateAPIView):
    """
    List all sections or create a new section.
    """

    queryset = Section.objects.all()
    serializer_class = SectionSerializer
    permission_classes = (IsAuthenticated, IsAdminUser)


class SectionDetail(RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a section instance.
    """

    queryset = Section.objects.all()
    serializer_class = SectionSerializer
    permission_classes = (IsAuthenticated, IsAdminUser)
