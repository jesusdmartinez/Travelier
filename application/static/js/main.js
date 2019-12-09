user_answers = []
user_data = []

$(document).ready(function(){

	$('.single-item').slick({
		infinite: false,
		slidesToShow: 1
	});

$(".next1").click(function(){
    user_answers.push(document.querySelector(".checked11").closest(".col-6").querySelector("h3.title").innerHTML);
    $(".slick-next ").click();
    $("ul#progressbar li.active1 ").addClass("active");
    return false;
});

$(".next2").click(function(){
    user_answers.push(document.querySelector(".checked11").closest(".col-6").querySelector("h3.title").innerHTML);
});

$(".next3").click(function(){
    user_answers.push(document.querySelector(".checked11").closest(".col-12").querySelector("h3.title").innerHTML);
});

$(".next5").click(function(){
    user_answers.push(document.querySelector(".checked11").closest(".col-6").querySelector("h3.title").innerHTML);
});

$(".next6").click(function(){
    user_answers.push(document.querySelector(".checked11").closest(".col-6").querySelector("h3.title").innerHTML);
});

$(".next7").click(function(){
    user_answers.push(document.querySelector(".checked11").closest(".col-6").querySelector("h3.title").innerHTML);
});

$(".next8").click(function(){
    user_answers.push(document.querySelector(".checked11").closest(".col-6").querySelector("h3.title").innerHTML);
});

$(".next9").click(function(){
    user_answers.push(document.querySelector(".checked11").closest(".col-6").querySelector("h3.title").innerHTML);
});

$(".next10").click(function(){
    user_answers.push(document.querySelectorAll(".form-control")[4].value);
});

$(".btn-trip").click(function(){
    for (let i = 5; i < document.querySelectorAll('.form-control').length; i++) {
  user_data.push(document.querySelectorAll('.form-control')[i].value)};
});

$(".next").click(function(){
    $(".slick-next ").click();
	  //$(this).closest('ul#progressbar li.active').find('ul#progressbar li.active').addClass("prev_show");
    $("ul#progressbar li.active + li").addClass("active");
    return false;
});
$(".nexts").click(function(){
    $(".slick-next ").click();
    return false;
});
$(".previouss ").click(function(){
    $(".slick-prev ").click();
    return false;
});
$(".previous ").click(function(){
    $(".slick-prev ").click();
	var lastli = $('ul#progressbar li.active').length;
	$( "ul#progressbar li:nth-child("+ lastli +")" ).removeClass('active' );

    return false;
});

$(".nexthide ").click(function(){
$(".progressbar").hide();
});
 $(".modal .btn.next").click(function(){
        $(".modal").modal('hide');
    });
$('.datepicker').datepicker({});
$(function(){
    $('.selectpicker').flagStrap({
    countries: {
        "BR": "Brazil"
    }
});
});
 var $radioButtons = $('input[type="radio"]');
$radioButtons.click(function() {
    $radioButtons.each(function() {
        $(this).parent().toggleClass('checked11', this.checked);
    });
});
		});
