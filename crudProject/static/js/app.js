// CSRF token setup start
// This configuration is necessary to make sure ajax requests
// are going to work withou a form

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

function createCompany(serializedData, formID, messageBoxID) {
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
            $(row).find('a:eq(0)')
                .attr({ 'href': "/company/details/" + pk });
            $(row).find('a:eq(1)')
                .attr({ 'href': "/company/update/" + pk });
        }
    });
}

// Setup Company Table end



// Table related end