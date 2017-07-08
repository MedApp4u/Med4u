

$(document).ready(function(){
	$('.vp-form-head').fadeOut().queue(function (next) {
        $(".vp-form-head").css("visibility", "visible");
        next();
    }).fadeIn("slow", "easeInOutExpo");
    $('.procedure-body-scroll').fadeOut().queue(function (next) {
        $(".procedure-body-scroll").css("visibility", "visible");
        next();
    }).fadeIn("slow", "easeInOutExpo");
    $('.procedure-body-desc').fadeOut().queue(function (next) {
        $(".procedure-body-desc").css("visibility", "visible");
        next();
    }).fadeIn("slow", "easeInOutExpo");    
	$("div#image_tab").animate({ left: '86%' }, "slow", "easeInOutExpo");
});
