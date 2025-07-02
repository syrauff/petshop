from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, CategoryListView # Impor viewset baru

# Router untuk ProductViewSet
router = DefaultRouter()
# Argumen pertama (r'') adalah prefix URL. Kita kosongkan agar URL-nya
# menjadi /api/products/ dan /api/products/{id}/
router.register(r'', ProductViewSet, basename='product')

urlpatterns = [
    # URL untuk Product (dibuat oleh router)
    path('', include(router.urls)),
    
    # URL untuk kategori kita biarkan terpisah karena bukan ViewSet
    # Sebenarnya ini tidak akan pernah diakses karena router di atas menangkap semua
    # path('categories/', CategoryListView.as_view(), name='category-list'),
]