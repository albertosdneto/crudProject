$(function () {
    $("#companyForm").submit(function (e) {
        // prevent from normal form behaviour
        e.preventDefault();

        $.blockUI();
        // serialize the form data  
        var serializedData = $(this).serialize();
        createCompany(serializedData, '#companyForm', '#messageBox');
        $.unblockUI();
    });
});

// Validate form for company creation
function validateCreateCompanyForm(formID) {
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
    if (validateCreateCompanyForm(formID) == true) {
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