from django.forms import inlineformset_factory
from django.http import JsonResponse
from django.shortcuts import redirect, render, get_object_or_404
from django.views.decorators.csrf import csrf_protect

from .forms import CompanyForm, CompanyFormUpdate, CompanyAddressForm, CompanyAddressFormHelper
from .models import Company, CompanyAddress


def home(request):
    """View to present the home page of the application

    Arguments:
        request {none} -- none

    Returns:
        Html Page -- Returns the template for the Home Page
    """
    return render(request, 'company/home.html')


def company(request):
    """Lists all the companies saved in the database

    Arguments:
        request {None} -- None

    Returns:
        Html Page -- Renders the template to show all the companies and 
                     allows one to search, edit, delete or open to view 
                     details of a certain company
    """
    return render(request, 'company/company_list.html')


def getCompanyList(request):
    """Reloads the company list at the company view

    Arguments:
        request {GET} -- Must be a GET request and ajax.

    Returns:
        Json -- Returns a Json response containing the list of companies
    """
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
    """Returns the details of a company

    Arguments:
        request {GET} -- This function is called at the company view
        pk {integer} -- This is the integer corresponding to the id of the company at the database


    Returns:
        Html Page -- Returns the template page with company details
    """
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
        company.save()
        
        data['message'] = 'Company updated successfully!'
        data['success'] = True
        return JsonResponse(data, status=200)
    except:
        data['message'] = 'Error during update. Contact Support.'
        data['success'] = False
        return JsonResponse(data, status=400)





def newCompanytPage(request):
    """Render the page to Create a new company 

    Arguments:
        request {GET} -- [description]

    Returns:
        Html Page -- Renders the template to create a new company
    """
    form_company = CompanyForm()

    context = {
        'companyForm': form_company,
    }
    return render(request, 'company/company_create.html', context)


def postNewCompany(request):
    """Saves the data of the new company

    Arguments:
        request {POST} -- Must be a Post request performed by ajax

    Returns:
        Json -- Returns Json data informing about the success or failure of the operation
    """
    data = dict()
    if request.method == "POST" and request.is_ajax():
        form_company = CompanyForm(request.POST)
        form_company.save()
        data['message'] = 'Company created successfully'
        data['success'] = True
        return JsonResponse(data, status=200)

    data['message'] = 'Error creating company. Contact system administrator'
    data['success'] = False
    return JsonResponse(data, status=400)


@csrf_protect
def deleteCompany(request, pk):
    """Deletes a copany by ajax

    Arguments:
        request {POST} -- Must be a Post request by ajax
        pk {integer} -- Integer corresponding to the id of the company to be deleted

    Returns:
        Json -- Returns Json data informing about the success or failure of the operation
    """
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
    """Returns the page to create a new address for a company

    Arguments:
        request {GET} -- [description]

    Returns:
        Html Page -- Html page that allows to add an address for a company
    """
    form_address = CompanyAddressForm()
    context = {
        'company': company,
        'addressForm': form_address
    }
    return render(request, 'company/address_create.html', context)


def postNewAddress(request):
    """Records a new address at the database

    Arguments:
        request {POST} -- Must be a Post request by ajax

    Returns:
        Json -- Returns Json data informing about the success or failure of the operation
    """
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
