

// // Sticky Navbar

// window.onscroll = function() {myFunction()};

// var navbar = document.getElementById("navbar");
// var sticky = navbar.offsetTop;

//     function myFunction() {
//     if (window.pageYOffset >= sticky) {
//         navbar.classList.add("sticky")
//     } else {
//         navbar.classList.remove("sticky");
//     }
//     }

// (function ($) {
//     "use strict";

//         // Sticky Navbar
//         $(window).scroll(function () {
//             if ($(this).scrollTop() > 300) {
//                 $('.sticky-top').addClass('shadow-sm').css('top', '0px');
//             } else {
//                 $('.sticky-top').removeClass('shadow-sm').css('top', '-100px');
//             }
//         });


//      // Back to top button
//         $(window).scroll(function () {
//         if ($(this).scrollTop() > 300) {
//             $('.back-to-top').fadeIn('slow');
//         } else {
//             $('.back-to-top').fadeOut('slow');
//         }
//     });
//     $('.back-to-top').click(function () {
//         $('html, body').animate({scrollTop: 0}, 1500, 'easeInOutExpo');
//         return false;
//     });


//     // Facts counter
//     $('[data-toggle="counter-up"]').counterUp({
//         delay: 10,
//         time: 2000
//     });

// })(jQuery);


    function myFunction() {
        var dots = document.getElementById("dots");
        var moreText = document.getElementById("more");
        var btnText = document.getElementById("myBtn");
    
        if (dots.style.display === "none") {
        dots.style.display = "inline";
        btnText.innerHTML = "Read more"; 
        moreText.style.display = "none";
        } else {
        dots.style.display = "none";
        btnText.innerHTML = " Read less "; 
        moreText.style.display = "inline";
        }
    }



window.onscroll = function() {myFunction1()};
var header = document.getElementById("myHeader");
var sticky = header.offsetTop+250;


    function myFunction1() {
    if (window.pageYOffset > sticky) {
        header.classList.add("sticky");
    } else {
        header.classList.remove("sticky");
    }
    }