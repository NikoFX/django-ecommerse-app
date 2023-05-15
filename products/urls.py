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
import products.views
from django.conf.urls.static import static
from django.conf import settings

app_name = 'products'
urlpatterns = [
    path('', products.views.products, name='products'),
    path('interdental', products.views.interdental, name='interdental'),
    path('interdental/original', products.views.original, name='original'),
    path('interdental/extra_soft', products.views.extra_soft, name='extra_soft'),
    path('interdental/angle', products.views.angle, name='angle'),
    path('toothpicks', products.views.toothpicks, name='toothpicks'),
    path('dental_floss', products.views.dental_floss, name='dental_floss'),
    path('brushers', products.views.brushers, name='brushers'),
    path('brushers/adult', products.views.adult, name='adult'),
    path('brushers/kids', products.views.kids, name='kids'),
    path('special_brushes', products.views.special_brushes, name='special_brushes'),
    path('accesories', products.views.accesories, name='accesories'),
    path('tepe', products.views.tepe, name='tepe'),
    path('miradent', products.views.miradent, name='miradent'),
    path('aquapick', products.views.aquapick, name='aquapick'),
    path('add', products.views.add, name='add'),
    path('detail/<product_id>', products.views.product_detail, name='detail'),
]