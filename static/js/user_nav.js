

window.addEventListener('DOMContentLoaded', function() {
    
    var matchesCount = document.getElementById('matchesCount');

    
    var numMatches = parseInt(matchesCount.textContent, 10);
     console.log('numMatches:', numMatches);
    
    if (numMatches > 0) {
        
        matchesCount.style.color = 'red';
        console.log('Setting color to red');
    }
});
