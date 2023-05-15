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
import products.views_bilimplant

app_name = 'products_bilimplant'
urlpatterns = [
    path('', products.views_bilimplant.products, name='products'),
    path('interdental', products.views_bilimplant.interdental, name='interdental'),
    path('interdental/original', products.views_bilimplant.original, name='original'),
    path('interdental/extra_soft', products.views_bilimplant.extra_soft, name='extra_soft'),
    path('interdental/angle', products.views_bilimplant.angle, name='angle'),
    path('toothpicks', products.views_bilimplant.toothpicks, name='toothpicks'),
    path('dental_floss', products.views_bilimplant.dental_floss, name='dental_floss'),
    path('brushers', products.views_bilimplant.brushers, name='brushers'),
    path('brushers/adult', products.views_bilimplant.adult, name='adult'),
    path('brushers/kids', products.views_bilimplant.kids, name='kids'),
    path('special_brushes', products.views_bilimplant.special_brushes, name='special_brushes'),
    path('accesories', products.views_bilimplant.accesories, name='accesories'),
    path('add', products.views_bilimplant.add, name='add'),
    path('detail/<product_id>', products.views_bilimplant.product_detail, name='detail'),
]
