from rest_framework.routers import DefaultRouter
from . import views
from rest_framework.routers import path


product_list = views.ProductViewSet.as_view({
    'get': 'list',
    'post': 'create',
})

product_detail = views.ProductViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    })

urlpatterns = [
    path('products/', product_list, name="product-list"),
    path('products/<str:id>/', product_detail, name="product-detail")
]