$(function () {

    // Submit form for Company Creation
    $("#companyForm").submit(function (e) {
        // prevent from normal form behaviour
        e.preventDefault();

        $.blockUI();
        // serialize the form data  
        let serializedData = $(this).serialize();
        createCompany(serializedData, '#companyForm', '#messageBox');
        $.unblockUI();
    });

    // Options for company update
    let options = {
        success: function (response) {
            $('#messageBox').attr("class", "alert alert-success col-md-6");
            $('#messageBox').find('span').html("<strong>Success!</strong><br>" + response.message);
            $('#messageBox').css("display", "block");
        },
        error: function (response) {
            $('#messageBox').attr("class", "alert alert-danger col-md-6");
            $('#messageBox').find('span').html("<strong>Error! </strong> Contact System support.<br>" + response.message);
            $('#messageBox').css("display", "block");
        },
    };
    $('#companyFormUpdate').ajaxForm(options);

    // $("#companyFormUpdate").submit(function (e) {
    //     e.preventDefault();
    //     $.blockUI();
    //     let serializedData = $(this).serialize();
    //     $id = $('#company_id').attr('value');
    //     if (false) {//(validateCompanyForm('#companyFormUpdate') == false) {
    //         alert("Please complete the required field");
    //         return false;
    //     } else {
    //         $name = $('#id_name').val();
    //         $.ajax({
    //             url: '/company/update/' + $id,
    //             type: 'POST',
    //             data: serializedData,
    //             // data: {
    //             //     name: $name,
    //             //     // csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
    //             // },
    //             success: function (response) {
    //                 $('#messageBox').attr("class", "alert alert-success col-md-6");
    //                 $('#messageBox').find('span').html("<strong>Success!</strong><br>" + response.message);
    //                 $('#messageBox').css("display", "block");
    //             },
    //             error: function (response) {
    //                 $('#messageBox').attr("class", "alert alert-danger col-md-6");
    //                 $('#messageBox').find('span').html("<strong>Error! </strong> Contact System support.<br>" + response.message);
    //                 $('#messageBox').css("display", "block");
    //             }
    //         });
    //     }
    //     $.unblockUI();
    // });

    $("#companyAddressForm").submit(function (e) {
        // prevent from normal form behaviour
        e.preventDefault();

        $.blockUI();
        // serialize the form data  
        let serializedData = $(this).serialize();
        createAddress(serializedData, '#companyAddressForm', '#messageBox');
        $.unblockUI();
    });


    setupCompanyTable('#myTable');

    // Reload table start
    $('.reloadButton').click(function () {
        $.blockUI();
        reloadCompanyTable('#myTable');
        $.unblockUI();
    });
    // Reload table end

    // Delete Item start
    $('#myTable tbody').on('click', 'button.delete-row', function () {
        pk = $(this).closest('tr').attr('id').substr(3);
        deleteCompany(parseInt(pk, 10), '#myTable');
    });
    // Delete Item end


    // New Address for company
    $('#newAddressButton').click(function () {
        $('#newAddressContainer').attr("class", "col-sm-12");
        $('#newAddressContainer').css("display", "block");
    });
    $('#newAddressCancelButton').click(function () {
        $('#newAddressContainer').css("display", "none");
    });


});

// Validate form for company creation
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

function createCompany(serializedData, formID, messageBoxID) {
    if (validateCompanyForm(formID) == true) {
        $.ajax({
            type: 'POST',
            url: "/ajax/post_new_company/",
            data: serializedData,
            success: function (response) {
                //reset the form after successful submit
                $(formID)[0].reset();
                $(messageBoxID).attr("class", "alert alert-success col-md-2");
                $(messageBoxID).find('span').html("<strong>Success!</strong> Company Created");
                $(messageBoxID).css("display", "block");
            },
            error: function (response) {
                $(messageBoxID).attr("class", "alert alert-danger col-md-2");
                $(messageBoxID).find('span').html("<strong>Error!</strong> Contact system support.");
                $(messageBoxID).css("display", "block");
            }
        });

    }

}

function updateCompany(serializedData, formID, messageBoxID) {
    if (validateCompanyForm(formID) == true) {
        $.ajax({
            type: 'POST',
            url: '/ajax/company/post_update/',
            data: serializedData,
            success: function (response) {
                //reset the form after successful submit
                $(formID)[0].reset();
                $(messageBoxID).attr("class", "alert alert-success col-md-2");
                $(messageBoxID).find('span').html("<strong>Success!</strong> Company updated");
                $(messageBoxID).css("display", "block");
            },
            error: function (response) {
                $(messageBoxID).attr("class", "alert alert-danger col-md-2");
                $(messageBoxID).find('span').html("<strong>Error!</strong> Contact system support.");
                $(messageBoxID).css("display", "block");
            }
        });

    }

}

function createAddress(serializedData, formID, messageBoxID) {
    if (validateAddressForm(formID) == true) {
        $.ajax({
            type: 'POST',
            url: "/ajax/post_new_address/",
            data: serializedData,
            success: function (response) {
                //reset the form after successful submit
                // $(formID)[0].reset();
                $(messageBoxID).attr("class", "alert alert-success col-md-2");
                $(messageBoxID).find('span').html("<strong>Success!</strong>" + response.data.message);
                $(messageBoxID).css("display", "block");
            },
            error: function (response) {
                $(messageBoxID).attr("class", "alert alert-danger col-md-2");
                $(messageBoxID).find('span').html("<strong>Error!</strong> Contact system support.");
                $(messageBoxID).css("display", "block");
            }
        });

    }

}

// Validate form for company creation
function validateAddressForm(formID) {
    if ($.trim($('#id_addressType').val()) == '') {
        alert("Fill in the Address Type!");
        $('#id_addressType').focus();
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
            "defaultContent": "<a><button class='open-row btn btn-info'>Open</button></a><a><button class='edit-row btn btn-warning'>Edit</button></a><button class='delete-row btn btn-danger'>Delete</button>",
        }],

        createdRow: function (row, data, dataIndex) {
            pk = $(row).closest('tr').attr('id').substr(3);
            $(row).find('a:eq(0)').attr({ 'href': "/company/details/" + pk });

            // .attr({ 'href': "/company/details/" + pk });

            $(row).find('a:eq(1)')
                .attr({ 'href': "/company/update/" + pk });
        }
    });
}
