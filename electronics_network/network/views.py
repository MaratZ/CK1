from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Supplier
from .serializers import SupplierSerializer
from .permissions import IsActiveEmployee  # Импортируем наш permission

class SupplierViewSet(viewsets.ModelViewSet):
    queryset = Supplier.objects.filter(is_active=True)
    serializer_class = SupplierSerializer
    permission_classes = [IsActiveEmployee]  # Подключаем проверку
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['contact__country']
    search_fields = ['name', 'contact__city']
