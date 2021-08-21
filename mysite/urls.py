"""datacenter URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from mysite import views

urlpatterns = [
    # ----- 寵寵欲動的功能 -----
    path('updateTF/<str:pk>/', views.updateTF, name='UpdateTF'),
    path('deleteTF/<str:pk>/', views.deleteTF, name='DeleteTF'),
    path('set/', views.set, name='Set'),
    path('about/', views.about, name='About'),
    # -------------------------

    # ----- Index 的功能 -----
    path('updateF/<str:pk>/', views.updateF, name='UpdateF'),
    path('deleteF/<str:pk>/', views.deleteF, name='DeleteF'),
    path('',views.index, name='Index'),
    # ------------------------

    # ----- 系統功能 -----
    path('register/', views.sign_up, name='Register'),
    path('login/', views.sign_in, name='Login'),
    path('logout/', views.mylogout, name='Logout'),
    # --------------------

    # ----- 其他功能 -----
    path('delete/<int:id>/', views.delete),
    path('chart/', views.chart),
    path('rank/', views.rank),
    path('show/<int:id>/', views.show),
    path('news/', views.news),
    # --------------------
]
