from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='company-home'),
    path('company/', views.company, name='company-list'),
    path('ajax/get_company_list/', views.getCompanyList, name='get_company_list'),
]
