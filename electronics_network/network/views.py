from rest_framework import viewsets, permissions, filters
from .models import Supplier
from .serializers import SupplierSerializer
from django_filters.rest_framework import DjangoFilterBackend

class SupplierViewSet(viewsets.ModelViewSet):
    queryset = Supplier.objects.filter(is_active=True)
    serializer_class = SupplierSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['contact__country']
    search_fields = ['name', 'contact__city']

    def get_permissions(self):
        if self.request.user.is_authenticated and self.request.user.is_active:
            return [permissions.IsAuthenticated()]
        return [permissions.AllowAny()]