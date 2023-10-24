// notifications.js

const openNotificationSlider = document.getElementById('openNotificationSlider');
const notificationSlider = document.getElementById('notificationSlider');
const closeNotificationSlider = document.querySelector('.close-slider');

openNotificationSlider.addEventListener('click', (event) => {
    event.preventDefault();
    notificationSlider.style.display = 'block';
});

closeNotificationSlider.addEventListener('click', (event) => {
    event.preventDefault();
    notificationSlider.style.display = 'none';
});
