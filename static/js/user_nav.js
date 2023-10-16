

window.addEventListener('DOMContentLoaded', function() {
    
    var matchesCount = document.getElementById('matchesCount');

    
    var numMatches = parseInt(matchesCount.textContent, 10);

    
    if (numMatches > 0) {
        
        matchesCount.style.color = 'red';
    }
});
