from django.forms import inlineformset_factory
from django.http import JsonResponse
from django.shortcuts import redirect, render, get_object_or_404
from django.views.decorators.csrf import csrf_protect

from .forms import CompanyForm, CompanyFormUpdate, CompanyAddressForm, CompanyAddressFormHelper
from .models import Company, CompanyAddress


def home(request):
    return render(request, 'company/home.html')


def company(request):
    return render(request, 'company/company_list.html')


def getCompanyList(request):
    if request.method == "GET" and request.is_ajax():
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
    addresses = CompanyAddress.objects.filter(
        company=company).order_by('zipCode')
    form_address = CompanyAddressForm()
    context = {
        'company': company,
        'addresses': addresses,
        'addressForm': form_address,
    }
    return render(request, 'company/company_details.html', context)


def update_company(request, company_pk):
    company = get_object_or_404(Company, pk=company_pk)
    company_form = CompanyForm(request.POST or None,
                               request.FILES or None, instance=company)

    addresses = CompanyAddress.objects.filter(company=company_pk)

    if request.method == "POST" and request.is_ajax():
        if company_form.is_valid():
            company_form.save()
            return JsonResponse({'message': 'Company updated successfully!', 'success': True}, status=200)
        elif (not company_form.is_valid()):
            return JsonResponse({'message': 'Error during form validation!', 'success': False}, status=400)

    context = {
        'company': company,
        'company_form': company_form,
        'addresses': addresses,
    }
    return render(request, 'company/company_update.html', context)


def editCompany(request, pk):
    company = get_object_or_404(Company, pk=pk)
    context = {
        'company': company
    }
    return render(request, 'company/company_edit.html', context)


def updateCompanyDetails(request, pk):
    data = dict()
    try:
        company = Company.objects.get(pk=pk)
        company.name = request.POST['name']
        company
        company.save()

        data['message'] = 'Company updated successfully!'
        data['success'] = True
        return JsonResponse(data, status=200)
    except:
        data['message'] = 'Error during update. Contact Support.'
        data['success'] = False
        return JsonResponse(data, status=400)


def newCompanytPage(request):
    form_company = CompanyForm()

    context = {
        'companyForm': form_company,
    }
    return render(request, 'company/company_create.html', context)


def postNewCompany(request):
    data = dict()
    if request.method == "POST" and request.is_ajax():
        form_company = CompanyForm(request.POST, request.FILES)
        form_company.save()
        data['message'] = 'Company created successfully'
        data['success'] = True
        return JsonResponse(data, status=200)

    data['message'] = 'Error creating company. Contact system administrator'
    data['success'] = False
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


def newAddressPage(request):
    form_address = CompanyAddressForm()
    context = {
        'company': company,
        'addressForm': form_address
    }
    return render(request, 'company/address_create.html', context)


def postNewAddress(request):
    data = dict()
    if request.method == "POST" and request.is_ajax():
        form_address = CompanyAddressForm(request.POST)
        form_address.save()
        data['message'] = 'Company created successfully'
        data['success'] = True
        return JsonResponse(data, status=200)

    data['message'] = 'Error creating company. Contact system administrator'
    data['success'] = False
    return JsonResponse(data, status=400)
