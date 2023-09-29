  $(document).on('click', '.bi', function () {
            var itemId = $(this).data('item-id');

            // Send an AJAX request to delete the item
            $.ajax({
                type: 'POST',
                url: '/delete-item/', // Replace with your Django URL
                data: {
                    'item_id': itemId,
                    csrfmiddlewaretoken: '{{ csrf_token }}' // Include the CSRF token
                },
                success: function () {
                    // Remove the table row on success
                    $(this).closest('tr').remove();
                }
            });
        });