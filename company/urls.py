"""URLs for company app."""

from django.urls import path
from company import views

app_name = 'company'

urlpatterns = [
    path('', views.home, name='home'),
    path('company/list/', views.company, name='list'),
    path('company/details/<int:pk>',
         views.read_company, name='details'),
    path('company/update/<int:company_pk>/',
         views.update_company, name='update'),
    path('ajax/get_company_list/', views.get_company_list,
         name='get_company_list'),
    path('company/create/', views.create_company, name='create'),
    path('ajax/company/delete/<int:pk>',
         views.delete_company, name='delete'),
    path('ajax/address/delete/<int:address_pk>',
         views.delete_address, name='address-delete'),
    path('company/address/reload/<int:company_pk>',
         views.reload_addresses, name='address-reload'),
]
