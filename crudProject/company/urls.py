from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='company-home'),
    path('company/list/', views.company, name='company-list'),
    path('company/details/<int:pk>',
         views.getCompanyDetails, name='company-details'),
    path('company/update/<int:pk>',
         views.updateCompanyDetails, name='company-update'),
    path('ajax/get_company_list/', views.getCompanyList, name='get_company_list'),
    path('company/create/', views.newCompanytPage, name='company-create'),
    path('ajax/post_new_company/', views.postNewCompany, name='post_new_company'),
    path('ajax/company/delete/<int:pk>',
         views.deleteCompany, name='delete-company'),
]
