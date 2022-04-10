from django.urls import path
from .views import api_detail_product_view,api_delete_product_view,api_update_product_view
app_name='products'
urlpatterns = [
    path('<id>/',api_detail_product_view,name="detail"),
    path('<id>/delete',api_delete_product_view,name="delete"),
    path('<id>/update',api_update_product_view,name="update"),
]