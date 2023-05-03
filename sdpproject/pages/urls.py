"""sdpproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path

from . import views

from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from .views import logoutuser

#dynamic routing
urlpatterns = [

    path('admin/', admin.site.urls),
    path('', views.home,name='home'),
    path('register/', views.register,name='register'),
    path('login/', views.login,name='login'),
    path('buy/', views.buy,name='buy'),
    path('explorewc/', views.explorewc, name='explorewc'),
    path('exploremc/', views.exploremc, name='exploremc'),
    path('exploremfc/', views.exploremfc, name='exploremfc'),
    path('explorewfc/', views.explorewfc, name='explorewfc'),
    path('explorekids/', views.explorekids, name='explorekids'),
    path('explorebg/', views.explorebg, name='explorebg'),
    path('explorewj/', views.explorewj, name='explorewj'),
    path('explorepb/', views.explorepb, name='explorepb'),
    path('cart/', views.cart, name='cart'),
    path('contactus/', views.contactus, name='contactus'),
    path('checkout/', views.checkout, name='checkout'),
    path('sell/', views.sell, name='sell'),
    path('logout/', logoutuser, name='logout'),
    path('aboutus/', views.aboutus, name='aboutus')
]

urlpatterns += staticfiles_urlpatterns()
