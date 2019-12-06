$(document).ready(function(){

	$('.single-item').slick({
		infinite: false,
		slidesToShow: 1
	});

$(".next1").click(function(){
    $(".slick-next ").click();
    $("ul#progressbar li.active1 ").addClass("active");
    return false;
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

let user_info = [];

const addUserInfo = (ev)=>{
    ev.preventDefault();
    let user_input = {
    first_name: document.getElementById('title').value

    }

}