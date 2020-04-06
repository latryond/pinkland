$(function() {
    $('.carousel-item').eq(0).addClass('active');
    var total = $('.carousel-item').length;
    var current = 0;
    $('#moveRight').on('click', function() {
        var next = current;
        current = current + 1;
        setSlide(next, current);
    });
    $('#moveLeft').on('click', function() {
        var prev = current;
        current = current - 1;
        setSlide(prev, current);
    });

    function animateSlide() {
        var next = current;
        current = current + 1;
        setSlide(next, current);
    }
    setInterval(animateSlide, 5000)

    function setSlide(prev, next) {
        var slide = current;
        if (next > total - 1) {
            slide = 0;
            current = 0;
        }
        if (next < 0) {
            slide = total - 1;
            current = total - 1;
        }
        $('.carousel-item').eq(prev).removeClass('active');
        $('.carousel-item').eq(slide).addClass('active');
        setTimeout(function() {

        }, 800);



        console.log('current ' + current);
        console.log('prev ' + prev);
    }
});

// ------------- VARIABLES ------------- //
var ticking = false;
var isFirefox = (/Firefox/i.test(navigator.userAgent));
var isIe = (/MSIE/i.test(navigator.userAgent)) || (/Trident.*rv\:11\./i.test(navigator.userAgent));
var scrollSensitivitySetting = 30; //Increase/decrease this number to change sensitivity to trackpad gestures (up = less sensitive; down = more sensitive) 
var slideDurationSetting = 600; //Amount of time for which slide is "locked"
var currentSlideNumber = 0;
var totalSlideNumber = $(".background").length;

// ------------- DETERMINE DELTA/SCROLL DIRECTION ------------- //
function parallaxScroll(evt) {
    if (isFirefox) {
        //Set delta for Firefox
        delta = evt.detail * (-120);
    } else if (isIe) {
        //Set delta for IE
        delta = -evt.deltaY;
    } else {
        //Set delta for all other browsers
        delta = evt.wheelDelta;
    }

    if (ticking != true) {
        if (delta <= -scrollSensitivitySetting) {
            //Down scroll
            ticking = true;
            if (currentSlideNumber !== totalSlideNumber - 1) {
                currentSlideNumber++;
                animateItem(currentSlideNumber);
                nextItem();
            }
            slideDurationTimeout(slideDurationSetting);
        }
        if (delta >= scrollSensitivitySetting) {
            //Up scroll
            ticking = true;
            if (currentSlideNumber !== 0) {
                currentSlideNumber--;
                animateItem(currentSlideNumber);
            }
            previousItem();
            slideDurationTimeout(slideDurationSetting);
        }
    }
}

// ------------- SET TIMEOUT TO TEMPORARILY "LOCK" SLIDES ------------- //
function slideDurationTimeout(slideDuration) {
    setTimeout(function() {
        ticking = false;
    }, slideDuration);
}

// ------------- ADD EVENT LISTENER ------------- //
var mousewheelEvent = isFirefox ? "DOMMouseScroll" : "wheel";
window.addEventListener(mousewheelEvent, _.throttle(parallaxScroll, 60), false);

// ------------- SLIDE MOTION ------------- //
function nextItem() {
    var $previousSlide = $(".background").eq(currentSlideNumber - 1);
    // animateItem($previousSlide);
    $previousSlide.removeClass("up-scroll").addClass("down-scroll");
}

function previousItem() {
    var $currentSlide = $(".background").eq(currentSlideNumber);
    // animateItem($currentSlide);
    $currentSlide.removeClass("down-scroll").addClass("up-scroll");
}

function animateItem(slideNumber) {
    var $targettSlide = $(".background").eq(slideNumber);
    var $previoustSlide = $(".background").eq(slideNumber - 1);
    console.log($targettSlide.find(".content-title"));
    $(".background").find(".content-title").removeClass("animated");
    $targettSlide.find(".content-title").addClass("animated", 2000);
}

$("#burger").click(function() {
    $(".loading-screen").toggleClass("circle");
    menuExpend();
});

function menuExpend() {
    console.log("expending");
    $(".menu").toggleClass("show");
    if ($(".menu").hasClass("show")) {
        $.each($('.menu-item'), function(i, el) {
            // $(el).css({ 'opacity': 0 });

            setTimeout(function() {
                $(el).animate({
                    'opacity': 1,
                    "margin-left": "0",
                }, 10);
            }, (i * 50));

        });
    } else {
        $.each($('.menu-item'), function(i, el) {
            // $(el).css({ 'opacity': 0 });

            setTimeout(function() {
                $(el).animate({
                    'opacity': 0,
                    "margin-left": "-100px",
                }, 10);
            }, (i * 50));

        });
    }
}