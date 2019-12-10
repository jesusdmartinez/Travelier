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

    let user_data_upload = {
    "first_name":user_data[0],
    "last_name":user_data[1],
    "email":user_data[2],
    "phone_number":user_data[3]
    };

    fetch('/get-started', {
    method: 'post',
    headers: {
            "Content-Type": "application/json; charset=utf-8",
        },
    body: JSON.stringify(user_data_upload)
  }).then(function(response) {
    return response.json();
  }).then(function(data) {
    console.log(data)
  });

/////////// Answers Upload /////////////

  let user_answer_upload = {
    "1":user_answers[0],
    "2":user_answers[1],
    "3":user_answers[2],
    "4":user_answers[3],
    "5":user_answers[4],
    "6":user_answers[5],
    "7":user_answers[6],
    "8":user_answers[7],
    };

    fetch('/get-started', {
    method: 'post',
    headers: {
            "Content-Type": "application/json; charset=utf-8",
        },
    body: JSON.stringify(user_answer_upload)
  }).then(function(response) {
    return response.json();
  }).then(function(data) {
    console.log(data)
  });


//    $.ajax({
//    type: 'POST',
//    url: '/get-started',
//    data: JSON.stringify(user_data),
//    dataType: 'json'
//    }).done(function(data) {
//    console.log(data)
//    })

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
