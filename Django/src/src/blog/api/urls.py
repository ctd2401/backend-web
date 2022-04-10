from django.urls import path
from .views import api_update_blog_view, api_detail_blog_view,api_delete_blog_view
app_name='blog'
urlpatterns = [
    path('<id>/',api_detail_blog_view,name="detail"),
    path('<id>/delete',api_delete_blog_view,name="delete"),
    path('<id>/update',api_update_blog_view,name="update"),
]
