"""Views available for company App."""


from company.forms import (CompanyForm, CompanyFormUpdate,
                           CompanyAddressForm)
from company.models import Company, CompanyAddress
from django.core.paginator import Paginator
from django.forms import inlineformset_factory
from django.http import JsonResponse
from django.shortcuts import redirect, render, get_object_or_404
from django.views.decorators.csrf import csrf_protect


def home(request):
    """
    Display home page for company app.

    **Template:**
    :template:`company/home.html`
    """
    return render(request, 'company/home.html')


def company(request):
    """
    Display page where all the companies will be listed.

    **Template:**
    :template:`company/company_list.html`
    """
    return render(request, 'company/company_list.html')


def get_company_list(request):
    """
    Return the list of companies, even when searching.

    Arguments:
        searchText -- name, or part of the name, of a company been searched.
        start -- item from which should display
        length -- Length of the list of items to send to client
        request {GET} and ajax -- Only runs search when performing an ajax
                                    request.

    Returns:
        Json -- Returns Json 'data' with keys:
                'draw': necessary for dataTables
                'recordsTotal': total of records on database,
                'recordsFiltered': total of records been sent to the client

    """
    if request.method == "GET" and request.is_ajax():

        if(request.GET.get('searchText') != ''):
            companies = list(
                Company.objects.filter(
                    name__icontains=request.GET.get('searchText')
                ).values()
            )
        else:
            companies = list(Company.objects.all().values())

        paginator = Paginator(companies, request.GET.get('length'))
        page = (int(request.GET.get('start')) /
                int(request.GET.get('length'))) + 1
        data = dict()
        data['draw'] = int(request.GET.get('draw'))
        data['recordsTotal'] = paginator.count
        data['recordsFiltered'] = paginator.count

        data['data'] = list(paginator.get_page(page))

        return JsonResponse(data, status=200)

    return JsonResponse({'message': 'Error not GET method!', 'success': False},
                        status=400)


def create_company(request):
    """
    Create a new copany.

    Arguments:
        request {POST} and ajax-- Creates the new company with the data from
                                    form.

    **Context**

    ``companyForm``
        An instance of `company.CompanyForm`

    **Template:**
    :template:`company/company_create.html`

    """
    form_company = CompanyForm(request.POST or None, request.FILES or None)

    if request.method == "POST" and request.is_ajax():
        if form_company.is_valid():
            form_company.save()
            return JsonResponse({'message': 'Company created successfully',
                                 'success': True}, status=200)
        else:
            return JsonResponse({
                'message': 'Error during form validation. Contact Support.',
                'success': False}, status=200)

    context = {
        'companyForm': form_company,
    }
    return render(request, 'company/company_create.html', context)


def read_company(request, pk):
    """
    Read the company data.

    Arguments:
        pk {integer} -- id of the company

    **Context**

    ``company``
        An instance of :model:`company.Company`

    ``addresses``
        An instance of :model:`company.CompanyAddress`

    ``addressForm``
        An instance of form `company.CompanyAddressForm`

    **Template:**
    :template:`company/company_details.html`

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


# This View was built this way for educational purpose.
# The idea here is to receive part of the data (addresses)
# from user and save it without the use of Django Form.
def update_company(request, company_pk):
    """
    Update company data and add new addresses if required.

    Arguments:
        company_pk {integer]} -- id of the company

    **Context**
    ``company``
        An instance of :model:`company.Company`

    ``company_form``
        An instance of form `company.CompanyForm`

    ``addresses``
        An instance of :model:`company.CompanyAddress`

    **Templates:**

    :template:`company/company_update.html`


    """
    company = get_object_or_404(Company, pk=company_pk)
    company_form = CompanyForm(request.POST or None,
                               request.FILES or None, instance=company)

    addresses = CompanyAddress.objects.filter(company=company_pk)

    if request.method == "POST" and request.is_ajax():
        new_address_counter = 0

        for data in request.POST:
            input_name = data.split(".")

            # Make sure we only try to add addresses when necessary
            # Then we create as much dictionaries as the number of new
            # addresses to be created
            if((input_name[0] == 'new_address_counter')
               and (request.POST[data] != '')
               and (request.POST[data] != '0')):
                new_address_counter = int(request.POST[data])
                if new_address_counter > 0:
                    new_addresses = dict()
                    for i in range(1, new_address_counter + 1):
                        new_addresses[i] = dict()

            # Updates an existing address
            elif (len(input_name) > 2) and (input_name[0] == 'address'):
                input_name[1] = int(input_name[1])
                address = CompanyAddress.objects.get(pk=input_name[1])
                if(getattr(address, input_name[2]) != request.POST[data]):
                    setattr(address, input_name[2], request.POST[data])
                    address.save()

            # Populates dictionaries with the data of new addresses
            elif (len(input_name) > 2) and (input_name[0] == 'new'):
                input_name[1] = int(input_name[1])
                new_addresses[input_name[1]
                              ][input_name[2]] = request.POST[data]

        # Saves New Addresses
        if new_address_counter > 0:
            for i in range(1, new_address_counter + 1):
                address = CompanyAddress()
                address.company = company

                for data in new_addresses[i]:
                    setattr(address, data, new_addresses[i][data])

                address.save()

        # Saves Company related data
        if company_form.is_valid():
            company_form.save()
            return JsonResponse({'message': 'Company updated successfully!',
                                 'success': True}, status=200)
        elif (not company_form.is_valid()):
            return JsonResponse({'message': 'Error during form validation!',
                                 'success': False}, status=400)

    context = {
        'company': company,
        'company_form': company_form,
        'addresses': addresses,
    }
    return render(request, 'company/company_update.html', context)


@csrf_protect
def delete_company(request, pk):
    """
    Delete Company.

    Arguments:
        pk {integer} -- id of the company

    Returns:
        Json -- Confirmation of deletion or error.

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


def reload_addresses(request, company_pk):
    """
    Reload all the addresses of a company of id 'company_pk'.

    Arguments:
        company_pk {integer} -- id of the company

    **Context**

    ``addresses``
        An instance of :model:`company.CompanyAddress`
    **Template:**

    :template:`company/_address_update.html`

    """
    addresses = CompanyAddress.objects.filter(company=company_pk)

    context = {
        'addresses': addresses,
    }

    return render(request, 'company/_address_update.html', context)


def delete_address(request, address_pk):
    """
    Delete address.

    Arguments:
        address_pk {integer} -- id of the address

    Returns:
        Json -- Message with confirmation of deletion or error.

    """
    if request.method == "POST" and request.is_ajax():
        data = dict()
        address = CompanyAddress.objects.get(pk=address_pk)
        if address:
            address.delete()
            data['message'] = "Address deleted!"
        else:
            data['message'] = "Error!"
        return JsonResponse(data)
