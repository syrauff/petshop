from rest_framework import generics, viewsets
from rest_framework.permissions import AllowAny, IsAdminUser
from .models import Product, Category
from .serializers import ProductSerializer, CategorySerializer

# Create your views here.
class ProductViewSet(viewsets.ModelViewSet):
    """
    ViewSet ini secara otomatis menyediakan aksi `list`, `create`, `retrieve`,
    `update`, dan `destroy`.
    """
    queryset = Product.objects.all().order_by('-created_at')
    serializer_class = ProductSerializer

    # Metode untuk menentukan izin berdasarkan jenis aksi (request)
    def get_permissions(self):
        """
        Memberikan izin yang berbeda untuk aksi yang berbeda.
        """
        if self.action in ['list', 'retrieve']:
            # Izinkan siapa saja (AllowAny) untuk melihat daftar dan detail produk
            permission_classes = [AllowAny]
        else:
            # Hanya admin/staf (IsAdminUser) yang bisa membuat, update, atau hapus
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]

class CategoryListView(generics.ListCreateAPIView):
    queryset = Category.objects.all().order_by('name')
    serializer_class = CategorySerializer
