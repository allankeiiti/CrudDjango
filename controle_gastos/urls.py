"""controle_gastos URL Configuration

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
from django.urls import path
from contas.views import home, update, listagem, nova_transacao, nova_categoria, update_categoria

urlpatterns = [
    path('admin/', admin.site.urls), # OK
    path('',home), # OK
    path('update/<int:pk>/', update, name='url_update'), # OK
    path('delete/<int:pk>/', update, name='url_delete'), # OK
    path('update_categoria/<int:pk>/', update_categoria, name='url_update_categoria'),
    path('delete_categoria/<int:pk>/', update_categoria, name='url_delete_categoria'),
    path('listagem/', listagem, name='url_listagem'), # OK
    path('contas/form/', nova_transacao, name='url_nova'), # OK
    path('contas/form_categoria', nova_categoria, name='url_nova_categoria') # OK
]
