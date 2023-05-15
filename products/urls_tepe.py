"""denteca URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path
import products.views_tepe
from django.conf.urls.static import static
from django.conf import settings

app_name = 'products_tepe'
urlpatterns = [
    path('', products.views_tepe.products, name='products'),
    path('interdental', products.views_tepe.interdental, name='interdental'),
    path('interdental/original', products.views_tepe.original, name='original'),
    path('interdental/extra_soft', products.views_tepe.extra_soft, name='extra_soft'),
    path('interdental/angle', products.views_tepe.angle, name='angle'),
    path('toothpicks', products.views_tepe.toothpicks, name='toothpicks'),
    path('dental_floss', products.views_tepe.dental_floss, name='dental_floss'),
    path('brushers', products.views_tepe.brushers, name='brushers'),
    path('brushers/adult', products.views_tepe.adult, name='adult'),
    path('brushers/kids', products.views_tepe.kids, name='kids'),
    path('special_brushes', products.views_tepe.special_brushes, name='special_brushes'),
    path('accesories', products.views_tepe.accesories, name='accesories'),
    path('add', products.views_tepe.add, name='add'),
    path('detail/<product_id>', products.views_tepe.product_detail, name='detail'),
]