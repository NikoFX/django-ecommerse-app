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
import products.views_miradent

app_name = 'products_miradent'
urlpatterns = [
    path('', products.views_miradent.products, name='products'),
    path('interdental', products.views_miradent.interdental, name='interdental'),
    path('interdental/original', products.views_miradent.original, name='original'),
    path('interdental/extra_soft', products.views_miradent.extra_soft, name='extra_soft'),
    path('interdental/angle', products.views_miradent.angle, name='angle'),
    path('toothpicks', products.views_miradent.toothpicks, name='toothpicks'),
    path('dental_floss', products.views_miradent.dental_floss, name='dental_floss'),
    path('brushers', products.views_miradent.brushers, name='brushers'),
    path('brushers/adult', products.views_miradent.adult, name='adult'),
    path('brushers/kids', products.views_miradent.kids, name='kids'),
    path('special_brushes', products.views_miradent.special_brushes, name='special_brushes'),
    path('accesories', products.views_miradent.accesories, name='accesories'),
    path('add', products.views_miradent.add, name='add'),
    path('detail/<product_id>', products.views_miradent.product_detail, name='detail'),
]
