document.getElementById('delete').addEventListener('click', function(event){
    var confirmed = window.confirm('Are you sure you want to delete this?');

    if(confirmed){
        alert('Deleted successfully.');
    }

    else{
        event.preventDefault();
    }

});