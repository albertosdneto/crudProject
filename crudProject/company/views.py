from django.http import JsonResponse
from django.shortcuts import render
from .forms import CompanyForm
from .models import Company

# Create your views here.


def home(request):
    return render(request, 'company/home.html')


def company(request):
    context = {
        'companies': Company.objects.all(),
    }
    return render(request, 'company/company_list.html', context)


def getCompanyList(request):
    if request.method == "GET" and request.is_ajax():  # and request.is_ajax():
        try:
            companies = list(Company.objects.all().values())
            data = dict()
            data['data'] = companies
        except:
            return JsonResponse({"success": False}, status=400)

        return JsonResponse(data, status=200)
    return JsonResponse({"success": False}, status=400)


def newCompanytPage(request):
    form = CompanyForm()
    return render(request, 'company/new_company.html', {'companyForm': form})


def postNewCompany(request):
    if request.method == "POST":
        form = CompanyForm(request.POST)
        form.save()
        return JsonResponse({"success": True}, status=200)
    return JsonResponse({"success": False}, status=400)
