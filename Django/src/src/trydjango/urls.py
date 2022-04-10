"""trydjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include,path
from pages.views import homepage_view,contact_view,social_view,about_view
urlpatterns = [
    path('products/',include('products.urls')),
    path('home/',homepage_view),
    path('about/',about_view),
    path('contact/',contact_view),
    path('admin/', admin.site.urls),
    path('blog/',include('blog.urls')),
    path('courses/',include('courses.urls')),

    #REST FRAMEWORK URLS
    path('api/blog/',include('blog.api.urls', 'blog_api')),
    path('api/products/',include('products.api.urls', 'products_api')),

]
