from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect
from .forms import CompanyForm, CompanyAddressForm
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


def getCompanyDetails(request, pk):
    company = get_object_or_404(Company, pk=pk)
    context = {
        'company': company
    }
    return render(request, 'company/company_details.html', context)


def editCompanyDetails(request, pk):
    company = get_object_or_404(Company, pk=pk)
    form = CompanyForm(request.POST or None, instance=company)

    if form.is_valid():
        form.save()
        return redirect('/')

    context = {
        'companyForm': form
    }

    return render(request, 'company/company_edit.html', context)


def newCompanytPage(request):
    form_company = CompanyForm()

    context = {
        'companyForm': form_company,
    }
    return render(request, 'company/new_company.html', context)


def postNewCompany(request):
    data = dict()
    if request.method == "POST" and request.is_ajax():
        form_company = CompanyForm(request.POST)
        form_company.save()
        data['message'] = 'Company created successfully'
        data['success'] = True
        # return JsonResponse({"success": True}, status=200)
        return JsonResponse(data, status=200)

    data['message'] = 'Error creating company. Contact system administrator'
    data['success'] = False
    # return JsonResponse({"success": False}, status=400)
    return JsonResponse(data, status=400)


@csrf_protect
def deleteCompany(request, pk):
    if request.method == "POST" and request.is_ajax():
        data = dict()
        company = Company.objects.get(pk=pk)
        if company:
            company.delete()
            data['message'] = "Company deleted!"
        else:
            data['message'] = "Error!"
        return JsonResponse(data)
