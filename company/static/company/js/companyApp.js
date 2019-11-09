$(function () {

    // ************ Company Creation Start ************ 
    $("#companyForm").submit(function (e) {
        // prevent from normal form behaviour
        e.preventDefault();

        $.blockUI();

        $form = $(this)
        var formData = new FormData(this);
        if (validateCompanyForm("#companyForm") == true) {
            $.ajax({
                type: 'POST',
                url: window.location.pathname,
                data: formData,
                success: function (response) {
                    //reset the form after successful submit
                    $("#companyForm")[0].reset();
                    $('#messageBox').attr("class", "alert alert-success col-md-2");
                    $('#messageBox').find('span').html("<strong>Success!</strong> " + response.message);
                    $('#messageBox').css("display", "block");
                },
                error: function (response) {
                    $('#messageBox').attr("class", "alert alert-danger col-md-2");
                    $('#messageBox').find('span').html("<strong>Error!</strong> " + response.message);
                    $('#messageBox').css("display", "block");
                },
                cache: false,
                contentType: false,
                processData: false
            });

        }
        $.unblockUI();
    });
    // ************ Company Creation End ************ 


    // ************ Company Update - Start ************ 
    $("#companyFormUpdate").submit(function (e) {
        // prevent from normal form behaviour
        e.preventDefault();

        $.blockUI();

        $form = $(this)
        var formData = new FormData(this);

        if (validateCompanyForm('#companyFormUpdate') == true) {
            $.ajax({
                type: 'POST',
                url: window.location.pathname,
                data: formData,
                success: function (response) {
                    $('#messageBox').attr("class", "alert alert-success col-md-6");
                    $('#messageBox').find('span').html("<strong>Success!</strong> " + response.message);
                    $('#messageBox').css("display", "block");
                    countNewAddress = 0;
                    $('#id_new_address_counter').attr('value', countNewAddress);
                    reloadAddresses($('#id_new_address_counter').attr('companyID'));
                },
                error: function (response) {
                    $('#messageBox').attr("class", "alert alert-danger col-md-6");
                    $('#messageBox').find('span').html("<strong>Error!</strong> " + response.message);
                    $('#messageBox').css("display", "block");
                },
                cache: false,
                contentType: false,
                processData: false
            });

        }
        $.unblockUI();
    });


    // Create New Address Inputs start
    var countNewAddress = 0;
    $('#companyFormUpdate').on('click', 'a.create-address', function () {
        countNewAddress += 1;

        $('#address-block-model')
            .clone(true)
            .insertBefore('hr.address_end:last')
            .css('display', 'block')
            .attr('id', 'new_' + countNewAddress);

        $('#id_new_address_counter').attr('value', countNewAddress);

        $('#new_' + countNewAddress)
            .find('input#id_addressType')
            .attr({ name: 'new.' + countNewAddress + '.addressType', required: 'true' });

        $('#new_' + countNewAddress)
            .find('input#id_line1')
            .attr({ name: 'new.' + countNewAddress + '.line1', required: 'true' });

        $('#new_' + countNewAddress)
            .find('input#id_line2')
            .attr({ name: 'new.' + countNewAddress + '.line2', required: 'true' });

        $('#new_' + countNewAddress)
            .find('input#id_zipCode')
            .attr({ name: 'new.' + countNewAddress + '.zipCode', required: 'true' });

        $('#new_' + countNewAddress)
            .find('input#id_city')
            .attr({ name: 'new.' + countNewAddress + '.city', required: 'true' });

        $('#new_' + countNewAddress)
            .find('input#id_state')
            .attr({ name: 'new.' + countNewAddress + '.state', required: 'true' });

        $('#new_' + countNewAddress)
            .find('input#id_country')
            .attr({ name: 'new.' + countNewAddress + '.country', required: 'true' });
    });
    // Create New Address Input end

    // Delete Address Start
    $('#companyFormUpdate div').on('click', 'a.delete-address', function () {
        if ($(this).attr('addressid') == 'null') {
            $(this).closest('.address-block').remove();
            countNewAddress -= 1;
            $('#id_new_address_counter').attr('value', countNewAddress)
        }
        else {
            deleteAddress($(this).attr('addressid'));
        }
    });
    // Delete Address end

    // ************ Company Update - End ************ 


    // ************ List of Companies - Start ************ 
    setupCompanyTable('#myTable');

    // Reload table start
    $('.reloadButton').click(function () {
        $.blockUI();
        reloadCompanyTable('#myTable');
        $.unblockUI();
    });
    // Reload table end

    // Delete Company start
    $('#myTable tbody').on('click', 'button.delete-row', function () {
        pk = $(this).closest('tr').attr('id').substr(3);
        deleteCompany(parseInt(pk, 10), '#myTable');
    });
    // Delete Company end
    // ************ List of Companies - End ************ 

    // ************ Address Creation - Start ************ 
    $("#companyAddressForm").submit(function (e) {
        // prevent from normal form behaviour
        e.preventDefault();

        $.blockUI();
        // serialize the form data  
        let serializedData = $(this).serialize();
        createAddress(serializedData, '#companyAddressForm', '#messageBox');
        $.unblockUI();
    });
    // ************ Address Creation - End ************ 


});


// Company Related Functions - Start

// Validate form for company creation or update
function validateCompanyForm(formID) {
    if ($.trim($('#id_name').val()) == '') {
        alert("Fill in the Name of the Company!");
        $('#id_name').focus();
        return false;
    }

    if (!$.isNumeric($('#id_cnpj').val())) {
        alert("Tax ID Number must be a number");
        $('#id_cnpj').focus();
        return false;
    }

    if (!(/^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/.test($('#id_email01').val()))) {
        alert("You have entered an invalid email address!");
        $('#id_email01').focus();
        return false;
    }

    if (!(/^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/.test($('#id_email02').val()))) {
        alert("You have entered an invalid email address!");
        $('#id_email02').focus();
        return false;
    }
    if (!(/(http|https):\/\/(\w+:{0,1}\w*)?(\S+)(:[0-9]+)?(\/|\/([\w#!:.?+=&%!\-\/]))?/.test($('#id_webPage').val()))) {
        alert("Fill in Web Page Address. Remember to put http or https at the beginning.");
        $('#id_webPage').focus();
        return false;
    }
    if ($.trim($('#id_line1').val()) == '') {
        alert("Fill in Address Info");
        $('#id_line1').focus();
        return false;
    }

    if ($.trim($('#id_line2').val()) == '') {
        alert("Fill in Address Info");
        $('#id_line2').focus();
        return false;
    }
    if ($.trim($('#id_zipCode').val()) == '') {
        alert("Fill in Zip Code");
        $('#id_zipCode').focus();
        return false;
    }

    if ($.trim($('#id_city').val()) == '') {
        alert("Fill in City");
        $('#id_city').focus();
        return false;
    }

    if ($.trim($('#id_state').val()) == '') {
        alert("Fill in State or Province");
        $('#id_state').focus();
        return false;
    }

    if ($.trim($('#id_country').val()) == '') {
        alert("Fill in Country");
        $('#id_country').focus();
        return false;
    }
    return true;

}


// CSRF token setup start
// This configuration is necessary to make sure ajax requests
// are going to work without a form (necessary for deleteCompany)

function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

var csrftoken = getCookie('csrftoken');

function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}
$.ajaxSetup({
    beforeSend: function (xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});

// CSRF token setup end

function deleteCompany(pk, tableID) {
    companyPk = pk;

    Swal.fire({
        title: 'Are you sure?',
        text: "You won't be able to revert this!",
        type: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#3085d6',
        cancelButtonColor: '#d33',
        confirmButtonText: 'Yes, delete it!'
    }).then((result) => {
        if (result.value) {
            $.ajax({
                url: `/ajax/company/delete/${companyPk}`,
                type: 'POST',
                dataType: 'json',
                success: function () {
                    $(tableID).DataTable().ajax.reload();
                    Swal.fire(
                        'Deleted!',
                        'Item deleted!',
                        'success'
                    );
                },
                error: function (response) {
                    Swal.fire(
                        'Fail!',
                        'Item NOT deleted!',
                        'error'
                    )
                }
            });

        }
    })

}


// Table related start

// Reloads table data at every click on 'Reload'
function reloadCompanyTable(tableID) {
    $.ajax({

        type: "GET",
        url: "/ajax/get_company_list/",
        contentType: "application/json; charset=utf-8",

    }).done(function (response) {

        $(tableID).DataTable().ajax.reload();

    }).fail(function (xhr, result, status) {

        console.log('Error retrieving content. Contact system admin.');

    });
}

// Setup Company Table start
function setupCompanyTable(tableID) {
    let buttonOpen = "<a target='_blank'><button class='open-row btn btn-info'><span class='pcoded-micon'><i class='ti-new-window'></i></span></button></a>";
    let buttonEdit = "<a target='_blank'><button class='edit-row btn btn-warning'><span class='pcoded-micon'><i class='ti-pencil'></i></span></button></a>";
    let buttonDelete = "<button class='delete-row btn btn-danger'><span class='pcoded-micon'><i class='ti-trash'></i></span></button>";
    $(tableID).DataTable({
        "ordering": true,
        "ajax": "/ajax/get_company_list/",
        rowId: function (a) {
            return 'pk_' + a.id;
        },
        "columns": [
            { "data": "name" },
            { "data": "cnpj" },
            { "data": "" },
        ],
        "columnDefs": [{
            "targets": -1,
            "data": null,
            "defaultContent": `${buttonOpen}${buttonEdit}${buttonDelete}`,
        }],

        createdRow: function (row, data, dataIndex) {
            pk = $(row).closest('tr').attr('id').substr(3);
            $(row).find('a:eq(0)').attr({ 'href': "/company/details/" + pk });
            $(row).find('a:eq(1)')
                .attr({ 'href': "/company/update/" + pk });
        }
    });
}
// Company Related Functions - End


// Address Related Functions - Start
function deleteAddress(pk) {
    addressPK = pk;

    Swal.fire({
        title: 'Are you sure?',
        text: "You won't be able to revert this!",
        type: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#3085d6',
        cancelButtonColor: '#d33',
        confirmButtonText: 'Yes, delete it!'
    }).then((result) => {
        if (result.value) {
            $.ajax({
                url: `/ajax/address/delete/${addressPK}`,
                type: 'POST',
                dataType: 'json',
                success: function () {
                    Swal.fire(
                        'Deleted!',
                        'Item deleted!',
                        'success'
                    );
                    let div_id = `#div_address_${addressPK}`;
                    $(div_id).remove();
                },
                error: function (response) {
                    Swal.fire(
                        'Fail!',
                        'Item NOT deleted!',
                        'error'
                    );
                }
            });

        }
    })

}


function reloadAddresses(companyID) {
    $.ajax({
        type: 'GET',
        url: `/company/address/reload/${companyID}`,
        success: function (data) {
            $('#address_container').html(data);
        }
    });
}

// Address Related Functions - End