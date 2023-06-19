const menuItems = document.querySelectorAll('.menu-item');
const pages = document.querySelectorAll('.page');

menuItems.forEach((item) => {
  item.addEventListener('click', (e) => {
    const target = e.target.getAttribute('data-target');
    pages.forEach((page) => {
      if (page.id === target) {
        page.classList.add('active');
      } else {
        page.classList.remove('active');
      }
    });
  });
});


