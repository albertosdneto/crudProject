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
