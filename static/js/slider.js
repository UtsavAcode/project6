
var readMoreLinks = document.querySelectorAll('.read-more');

var sliders = document.querySelectorAll('.slider');
var sliderOverlays = document.querySelectorAll('.slider-overlay');


readMoreLinks.forEach(function (link, index) {
    link.addEventListener('click', function (e) {
        e.preventDefault();
        
        const slider = sliders[index];
        const overlay = sliderOverlays[index];
        if (slider.style.right === '0%') {
            slider.style.right = '-50%';
            overlay.style.display = 'none';
        } else {
            slider.style.right = '0%';
            overlay.style.display = 'block';
        }
    });
});


var closeSliderLinks = document.querySelectorAll('.close-slider');
closeSliderLinks.forEach(function (closeLink, index) {
    closeLink.addEventListener('click', function (e) {
        e.preventDefault();
       
        const slider = sliders[index];
        const overlay = sliderOverlays[index];
        slider.style.right = '-50%';
        overlay.style.display = 'none';
    });
});



