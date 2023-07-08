window.addEventListener('scroll', function() {
    var scrollTop = document.documentElement.scrollTop || document.body.scrollTop;
    var scrollHeight = document.documentElement.scrollHeight || document.body.scrollHeight;
    var clientHeight = document.documentElement.clientHeight || document.body.clientHeight;
    
    if (scrollTop + clientHeight >= scrollHeight) {
      // Send an AJAX request to update the Django admin status
      $.ajax({
        url: '/update-status/',  // Replace with your Django view URL for updating the status
        method: 'POST',  // Adjust the HTTP method if needed
        data: {status: 'finish'},  // Data to be sent in the request body
        success: function(response) {
          console.log('Status updated successfully');
        },
        error: function(xhr, textStatus, errorThrown) {
          console.error('Error updating status:', errorThrown);
        }
      });
    }
  });