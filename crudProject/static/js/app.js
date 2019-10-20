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

function deleteCompany(pk) {
    companyPk = pk;
    $.ajax({
        url: `/ajax/company/delete/${companyPk}`,
        type: 'POST',
        dataType: 'json',
        success: function (data) {
            //$(el).parents()[1].remove()
            $('#myTable').DataTable().ajax.reload();
        }
    });
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

$('#reload').on("click", function (event) {

    $.ajax({

        type: "GET",
        url: "/ajax/get_company_list/",
        contentType: "application/json; charset=utf-8",

    }).done(function (response) {

        $('#myTable').DataTable().ajax.reload();

    }).fail(function (xhr, result, status) {

        console.log('Error retrieving list of companies. Contact system admin.');

    });
});