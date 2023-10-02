const readMoreLinks = document.querySelectorAll('.read-more')

readMoreLinks.forEach((link) => {
    link.addEventListener('click', (event) => {
        event.preventDefault();

        const moreDetails = link.nextElementSibling;

        if(moreDetails.style.display === 'none' || moreDetails.style.display===''){
            moreDetails.style.display = 'block';

        }

        else{
            moreDetails.style.display = 'none';
        }
    });
});