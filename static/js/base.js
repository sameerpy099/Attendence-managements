const profileWrapper = document.getElementById('profileWrapper');
const profilePopup = document.getElementById('profilePopup');

profileWrapper.addEventListener('click', () => {
    // Toggle popup
    if(profilePopup.style.display === "flex"){
        profilePopup.style.display = "none";
    } else {
        profilePopup.style.display = "flex";
    }
});

// Optional: click outside to close
document.addEventListener('click', (e) => {
    if(!profileWrapper.contains(e.target)){
        profilePopup.style.display = "none";
    }
});

// slider navbar 
