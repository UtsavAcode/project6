document.querySelectorAll('.btn-danger').forEach(function (btn) {
    btn.addEventListener('click', function (event) {
      var confirmed = window.confirm('Are you sure you want to delete this item?');
      if (confirmed) {
        var row = event.target.closest('tr');
        var rowId = row.dataset.rowId;
        var csrftoken = getCookie('csrftoken');

        fetch('/delete/' + rowId + '/', {
          method: 'POST',
          headers: {
            'X-CSRFToken': csrftoken,
          },
        })
          .then(function (response) {
            if (response.status === 200) {
              row.remove();
              alert('Deleted successfully.');
            } else {
              alert('Error deleting the item.');
            }
          })
          .catch(function (error) {
            console.error('Error:', error);
          });
      }
    });
  });

  function renumberTableIds(){
    var rows =  document.querySelectorAll('tr[data-row-id]');
    rows.forEach(function(row, index){
        row.dataset.rowId=index +1;
        row.cells[0].textContent = index+1;
    });
  }

  function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
      var cookies = document.cookie.split(';');
      for (var i = 0; i < cookies.length; i++) {
        var cookie = cookies[i].trim();
        if (cookie.substring(0, name.length + 1) === name + '=') {
          cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
          break;
        }
      }
    }
    return cookieValue;
  }


