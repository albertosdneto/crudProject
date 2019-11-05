from django.urls import path
from . import views

app_name = 'company'

urlpatterns = [
    path('', views.home, name='home'),
    path('company/list/', views.company, name='list'),
    path('company/details/<int:pk>',
         views.read_company, name='details'),
    path('company/update/<int:company_pk>/',
         views.update_company, name='update'),
    path('ajax/get_company_list/', views.getCompanyList, name='get_company_list'),
    path('company/create/', views.newCompanytPage, name='create'),
    path('ajax/post_new_company/', views.postNewCompany, name='post_new_company'),
    path('ajax/company/delete/<int:pk>',
         views.deleteCompany, name='delete'),
    path('company/address/create/',
         views.newAddressPage, name='address-create'),
    path('ajax/post_new_address/',
         views.postNewAddress, name='post_new_address'),
    path('ajax/address/delete/<int:address_pk>',
         views.delete_address, name='address-delete'),
]
