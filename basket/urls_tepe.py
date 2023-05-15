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
import basket.views_tepe

app_name = 'basket_tepe'
urlpatterns = [
    path('', basket.views_tepe.basket, name='basket'),
    path('ref', basket.views_tepe.refresh, name='refresh'),
    path('del', basket.views_tepe.delete, name='delete'),
    path('checkout', basket.views_tepe.checkout, name='checkout'),
]