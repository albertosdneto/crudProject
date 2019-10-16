from django.shortcuts import render
from .models import Company
# Create your views here.


def home(request):
    return render(request, 'company/home.html')


def company(request):
    context = {
        'companies': Company.objects.all(),
    }
    return render(request, 'company/company_list.html', context)
