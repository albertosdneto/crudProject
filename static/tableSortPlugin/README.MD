# tableSortPlugin

## About

jQuery plugin to sort and search items of an html table.


## Usage
- You need to have a table with an id at your code. At this example we use #sort_this_table as the id.
Change it to the id of the table you want to sort.

- Add the script to the Html. Remember to call jQuery as well. At the <head> do:
```shell
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>
    <script src="tableSortPlugin.js"></script>

    <script>
        $(document).ready(function () {
            $('#sort_this_table').sortTable({
                // Choose between 'top' or 'bottom' (default: 'top')
                searchInputPosition: 'bottom',
            });
        });
    </script>

```

- There is a search field which can be configured to be shown at top or bottom of the table.

- Suggestions and contributions are wellcome. Enjoy.
