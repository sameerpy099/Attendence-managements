// // document.addEventListener('DOMContentLoaded', () => {
// //   const slider = document.querySelector('.slider');
// //   const toggleBtn = document.querySelector('.toggle');
// //   const icon = toggleBtn.querySelector('i');
// //   const hero = document.querySelector('.content');

// //   // ✅ Sidebar open by default (no forced layout change)
// //   slider.classList.remove('slider-closed');
// //   icon.classList.replace('bx-chevron-right', 'bx-chevron-left');

// //   // ✅ Toggle manually without breaking responsive layout
// //   toggleBtn.addEventListener('click', (e) => {
// //     e.stopPropagation();
// //     slider.classList.toggle('slider-closed');

// //     const isClosed = slider.classList.contains('slider-closed');
// //     icon.classList.replace(
// //       isClosed ? 'bx-chevron-left' : 'bx-chevron-right',
// //       isClosed ? 'bx-chevron-right' : 'bx-chevron-left'
// //     );

// //     // ✅ Adjust hero layout safely (only if hero exists)
// //     if (hero) {
// //       hero.style.marginLeft = isClosed ? '50px' : '250px';
// //       hero.style.width = isClosed ? 'calc(100vw - 50px)' : 'calc(100vw - 250px)';
// //     }
// //   });

// //   // ✅ Prevent clicks inside the slider from toggling
// //   slider.addEventListener('click', (e) => e.stopPropagation());

// //   // ✅ Prevent sidebar toggle when clicking on <a> links (no reload issues)
// //   const links = slider.querySelectorAll('a');
// //   links.forEach(link => {
// //     link.addEventListener('click', (e) => {
// //       e.stopPropagation();
// //       // no sidebar toggle, allow navigation normally
// //     });
// //   });
// // });


// document.addEventListener('DOMContentLoaded', () => {
//   const slider = document.querySelector('.slider');
//   const toggleBtn = document.querySelector('.toggle');
//   const icon = toggleBtn.querySelector('i');
//   const hero = document.querySelector('.content');

//   // ✅ Check screen width at load
//   const isMobile = window.innerWidth < 1000;

//   // ✅ Set initial sidebar state based on screen size
//   if (isMobile) {
//     slider.classList.add('slider-closed');
//     icon.classList.replace('bx-chevron-left', 'bx-chevron-right');
//     if (hero) {
//       hero.style.marginLeft = '50px';
//       hero.style.width = 'calc(100vw - 50px)';
//     }
//   } else {
//     slider.classList.remove('slider-closed');
//     icon.classList.replace('bx-chevron-right', 'bx-chevron-left');
//     if (hero) {
//       hero.style.marginLeft = '250px';
//       hero.style.width = 'calc(100vw - 250px)';
//     }
//   }

//   // ✅ Toggle sidebar manually
//   toggleBtn.addEventListener('click', (e) => {
//     e.stopPropagation();
//     slider.classList.toggle('slider-closed');

//     const isClosed = slider.classList.contains('slider-closed');
//     icon.classList.replace(
//       isClosed ? 'bx-chevron-left' : 'bx-chevron-right',
//       isClosed ? 'bx-chevron-right' : 'bx-chevron-left'
//     );

//     if (hero) {
//       hero.style.marginLeft = isClosed ? '50px' : '250px';
//       hero.style.width = isClosed ? 'calc(100vw - 50px)' : 'calc(100vw - 250px)';
//     }
//   });

//   // ✅ Prevent sidebar toggle when clicking inside slider or links
//   slider.addEventListener('click', (e) => e.stopPropagation());
//   const links = slider.querySelectorAll('a');
//   links.forEach(link => {
//     link.addEventListener('click', (e) => e.stopPropagation());
//   });

//   // ✅ Optional: Auto adjust when resizing window
//   window.addEventListener('resize', () => {
//     const isNowMobile = window.innerWidth < 1000;
//     if (isNowMobile) {
//       slider.classList.add('slider-closed');
//       icon.classList.replace('bx-chevron-left', 'bx-chevron-right');
//       if (hero) {
//         hero.style.marginLeft = '50px';
//         hero.style.width = 'calc(100vw - 50px)';
//       }
//     } else {
//       slider.classList.remove('slider-closed');
//       icon.classList.replace('bx-chevron-right', 'bx-chevron-left');
//       if (hero) {
//         hero.style.marginLeft = '250px';
//         hero.style.width = 'calc(100vw - 250px)';
//       }
//     }
//   });
// });
// document.addEventListener('DOMContentLoaded', () => {
//   const slider = document.querySelector('.slider');
//   const toggleBtn = document.querySelector('.toggle');
//   const icon = toggleBtn.querySelector('i');
//   const hero = document.querySelector('.content');

//   // ✅ Check screen width at load
//   const isMobile = window.innerWidth < 1000;

//   // ✅ Set initial sidebar state
//   const setSidebarState = (closed) => {
//     if (closed) {
//       slider.classList.add('slider-closed');
//       icon.classList.replace('bx-chevron-left', 'bx-chevron-right');
//       if (hero) {
//         hero.style.marginLeft = '50px';
//         hero.style.width = 'calc(100vw - 50px)';
//       }
//     } else {
//       slider.classList.remove('slider-closed');
//       icon.classList.replace('bx-chevron-right', 'bx-chevron-left');
//       // if (hero) {
//       //   hero.style.marginLeft = '250px';
//       //   hero.style.width = 'calc(100vw - 250px)';
//       // }
//     }
//   };

//   setSidebarState(isMobile);

//   // ✅ Toggle manually (only with button)
//   toggleBtn.addEventListener('click', (e) => {
//     e.preventDefault();
//     e.stopPropagation();

//     const isClosed = slider.classList.toggle('slider-closed');
//     icon.classList.replace(
//       isClosed ? 'bx-chevron-left' : 'bx-chevron-right',
//       isClosed ? 'bx-chevron-right' : 'bx-chevron-left'
//     );
//     hero.style.marginLeft = isClosed ? '50px' : '250px';
//     hero.style.width = isClosed ? 'calc(100vw - 50px)' : 'calc(100vw - 250px)';
//   });

//   // ✅ Stop sidebar link clicks from triggering anything
//   const links = slider.querySelectorAll('a');
//   links.forEach(link => {
//     link.addEventListener('click', (e) => {
//       // allow normal navigation but never trigger toggle
//       e.stopPropagation();
//     });
//   });

//   // ✅ Optional: auto adjust on resize
//   window.addEventListener('resize', () => {
//     const isNowMobile = window.innerWidth < 1000;
//     setSidebarState(isNowMobile);
//   });
// });


document.addEventListener('DOMContentLoaded', () => {
  const slider = document.querySelector('.slider');
  const toggleBtn = document.querySelector('.toggle');
  const icon = toggleBtn.querySelector('i');
  const hero = document.querySelector('.content');

  const handleSidebar = (isClosed) => {
    const isMobile = window.innerWidth < 1000;

    if (isClosed) {
      slider.classList.add('slider-closed');
      icon.classList.replace('bx-chevron-left', 'bx-chevron-right');
      if (hero) {
        hero.style.marginLeft = isMobile ? '0px' : '50px';
      }
    } else {
      slider.classList.remove('slider-closed');
      icon.classList.replace('bx-chevron-right', 'bx-chevron-left');
      if (hero) {
        hero.style.marginLeft = isMobile ? '50px' : '250px';
      }
    }
  };

  // initialize on load
  handleSidebar(window.innerWidth < 1000);

  // toggle on click
  toggleBtn.addEventListener('click', (e) => {
    e.preventDefault();
    e.stopPropagation();
    const isClosed = slider.classList.toggle('slider-closed');
    handleSidebar(isClosed);
  });

  // auto adjust on resize
  window.addEventListener('resize', () => {
    const isClosed = slider.classList.contains('slider-closed');
    handleSidebar(isClosed);
  });
});
