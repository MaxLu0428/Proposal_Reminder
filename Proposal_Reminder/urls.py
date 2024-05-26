"""Proposal_Reminder URL Configuration

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

from django.urls import path
from . import views

urlpatterns = [
    path('', views.select_document_number, name='select_document_number'),
    path('<str:document_number>/', views.mymodel_list, name='mymodel_list'),
    path('add/', views.mymodel_add, name='mymodel_add'),
    path('edit/<int:pk>/', views.mymodel_edit, name='mymodel_edit'),
    path('delete/<int:pk>/', views.mymodel_delete, name='mymodel_delete'),
    path('compare/<int:pk>/', views.mymodel_compare, name='mymodel_compare'),
    path('upload_vdrm/', views.upload_vdrm, name='upload_vdrm'),
    path('vdrm_list/', views.vdrm_list, name='vdrm_list'),
    path('update_mymodel_field/', views.update_mymodel_field, name='update_mymodel_field'),
]
