// Separate JavaScript file (e.g., custom.js)

$(document).ready(function() {
    // Add a click event listener to the "message" button
    $('.message-button').on('click', function() {
        var recipient_email = '{{ obj.email }}';  // Get the recipient's email from the user object

        // Make an AJAX request to send the notification
        $.ajax({
            url: '/send_notification/' + recipient_email + '/',
            type: 'GET',
            success: function(data) {
                if (data.success) {
                    alert('Notification sent successfully.');
                } else if (data.error) {
                    alert('Error sending notification: ' + data.error);
                }
            }
        });
    });
});
