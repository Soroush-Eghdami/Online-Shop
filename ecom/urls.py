"""
URL configuration for ecom project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    # explicit top-level apps MUST come before the shop include
    path('cart/', include(('cart.urls', 'cart'), namespace='cart')),
    # path('accounts/', include(('accounts.urls', 'accounts'), namespace='accounts')),
    # add other top-level routes here (orders, dashboard, etc.)

    # finally include shop at root — product_list will handle `/`
    path('', include(('shop.urls', 'shop'), namespace='shop')),
]
