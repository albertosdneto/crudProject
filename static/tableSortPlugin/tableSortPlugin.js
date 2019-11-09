/* eslint-disable no-undef */
(function ($) {

    $.fn.sortTable = function (options) {
        // Wrap table in a div
        $(this).wrap("<div></div>");

        // Default Options
        let settings = $.extend({
            'searchInputPosition': 'top',
        }, options);

        // Treats the case when the user passes a value different from 'top' or 'bottom' 
        // as position for the search field
        if ((settings.searchInputPosition != 'top') && (settings.searchInputPosition != 'bottom')) {
            settings.searchInputPosition = 'top'
        }

        // Sets the input and shows it
        if (settings.searchInputPosition == 'bottom') {
            $(this).after("<input type='text' class='search_" + settings.searchInputPosition + "' placeholder='Search'>")
        } else {
            $(this).before("<br><br><input type='text' class='search_" + settings.searchInputPosition + "' placeholder='Search'>")
        }

        $(this).parents('div').find('.search_' + settings.searchInputPosition).show()


        // Performs the search at the input field related to the table

        // Looks for the content typed at the input and toggles the lines that do no match
        $(this).parents('div').find('.search_' + settings.searchInputPosition).on("keyup", function () {
            let value = $(this).val().toLowerCase();

            // Toggles (show or hide) the tr where the search content was foun
            $(this).parents('div').find("table tr:gt(0)").filter(function () {
                $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1)
            });
        });

        // Sets the span that will show whether the items are order ascending or descending
        $(this).find('th').append("<br><span class='order_by'></strong>")

        // Whenever a th is clicked the whole column gets ordered
        $(this).find('th').click(function () {
            let table = $(this).parents('table').eq(0)

            let rows = table.find('tr:gt(0)').toArray().sort(comparer($(this).index()))
            this.asc = !this.asc

            if (!this.asc) {
                rows = rows.reverse()
            }
            for (let i = 0; i < rows.length; i++) {
                table.append(rows[i])
                table.find('th').find('.order_by').text('')
            }

            // Changes the text according to the ordenation
            if (this.asc) {
                $(this).find('.order_by').text('(Asc)')
            } else if (!this.asc) {
                $(this).find('.order_by').text('(Desc)')
            } else {
                $(this).find('.order_by').text('')
            }

            return table;
        })

        // Function passed to the sort() method. It makes sure the values are treated accoding to 
        // there nature (numeric or not numeric)
        function comparer(index) {

            return function (a, b) {
                let valA = getCellValue(a, index),
                    valB = getCellValue(b, index)
                return $.isNumeric(valA) && $.isNumeric(valB) ? valA - valB : valA.toString().localeCompare(valB)
            }

        }

        // Get the value of a certain cell at a row
        function getCellValue(row, index) {
            return $(row).children('td').eq(index).text()
        }


    };

}(jQuery));