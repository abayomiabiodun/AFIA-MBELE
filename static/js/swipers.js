var swiper = new Swiper(".mySwiperServices", {
    slidesPerView: 1,
    spaceBetween: 10,
    pagination: {
      el: ".swiper-pagination",
      clickable: true,
    },
    navigation: {
        nextEl: ".swiper-button-next",
        prevEl: ".swiper-button-prev",
      },
    breakpoints: {
      560: {
        slidesPerView: 2,
        spaceBetween: 20,
      },
      950: {
        slidesPerView: 3,
        spaceBetween: 40,
      },
      1050: {
        slidesPerView: 4 ,
        spaceBetween: 50,
      },
    },
  });

  // team
  var swiper = new Swiper(".myteam", {
    slidesPerView: 1,
    spaceBetween: 10,
    pagination: {
      el: ".swiper-pagination",
      clickable: true,
    },
    navigation: {
        nextEl: ".swiper-button-next",
        prevEl: ".swiper-button-prev",
      },
    breakpoints: {
      560: {
        slidesPerView: 2,
        spaceBetween: 20,
      },
    
      950: {
        slidesPerView: 3,
        spaceBetween: 40,
      },

      1050: {
        slidesPerView: 4,
        spaceBetween: 50,
      },
    },
  });