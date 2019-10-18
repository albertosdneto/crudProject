
$('#reload').click(function (e) {
    $.blockUI({ message: null });
    $.ajax({
        type: 'GET',
        url: "/ajax/get_company_list/",
        dataType: 'json',
        success: function (response) {
            let rows = '';
            response.companytList.forEach(company => {
                rows += `
							<tr>
								<td>${company.name}</td>
								<td>${company.cnpj}</td>
							</tr>`;
            });
            $("#table_companies tbody").html(rows);

        }
    });
    setTimeout($.unblockUI, 1000);
});


// $("#users").change(function (e) {
//     e.preventDefault();
//     var pk = $(this).val();
//     var data = { pk };
//     $.ajax({
//         type: 'GET',
//         url: "{% url 'get_user_info' %}",
//         data: data,
//         success: function (response) {
//             $("#user_info table tbody").html(`<tr>
//    				<td>${response.user_info.name || "-"}</td>
//    				<td>${response.user_info.email || "-"}</td>
//    				<td>${response.user_info.message}</td>
//    				<td>${response.user_info.timestamp}</td>
//    				</tr>`)
//         },
//         error: function (response) {
//             console.log(response)
//         }
//     })
// })
