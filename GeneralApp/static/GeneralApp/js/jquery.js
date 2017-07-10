

$(document).ready(function(){
	$('.vp-form-head').fadeOut().queue(function (next) {
        $(".vp-form-head").css("visibility", "visible");
        next();
    }).fadeIn("slow", "easeInOutExpo");
    $('.symptom-body-scroll').fadeOut().queue(function (next) {
        $(".symptom-body-scroll").css("visibility", "visible");
        next();
    }).fadeIn("slow", "easeInOutExpo");
    $('.symptoms-body-desc').fadeOut().queue(function (next) {
        $(".symptoms-body-desc").css("visibility", "visible");
        next();
    }).fadeIn("slow", "easeInOutExpo");    
	$("div#image_tab").animate({ left: '86%' }, "slow", "easeInOutExpo");
});
