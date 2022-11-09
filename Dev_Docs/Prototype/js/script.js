document.addEventListener('click', e => {
  const isDropdownButton = e.target.matches("[data-dropdown-button]")
  if (!isDropdownButton && e.target.closest("[data-dropdown-button]") != null) return 

  let currentDropdown 
  if (isDropdownButton) {
    currentDropdown = e.target.closest('[data-dropdown]')
    currentDropdown.classList.toggle('active')
  }

  document.querySelectorAll("[data-dropdown].active").forEach(dropdown =>{
    if (dropdown === currentDropdown) return
    dropdown.classList.remove('active')
  })
})




const slider = docement.querySelector('.slider'); 

const leftArrow = document.querySelector('.left'); 
const rightArrow = document.querySelector('.right'); 

var sectionIndex = 0;

rightArrow.addEventListener('click', function () {
  sectionIndex = sectionIndex + 1
  slider.style.transform = 'translate('+ sectionIndex * -25 +'%)';

})
