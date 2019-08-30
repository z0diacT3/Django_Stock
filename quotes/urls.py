# Copyright (c) 2019-2020 Eugene Davies All Rights Reserved. Some HTML pages are purely created for test purpose and are not the best views I would suggest

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('add_stock/', views.add_stock, name='add_stock'),
    path('delete/<stock_id>', views.delete, name="delete"),
    path('delete_stock/', views.delete_stock, name='delete_stock'),


]