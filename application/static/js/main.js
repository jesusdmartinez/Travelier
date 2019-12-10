user_answers = []

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
  user_answers.push(document.querySelectorAll('.form-control')[i].value)};

//        let user_answers_upload = {
//    "1":user_answers[0],
//    "2":user_answers[1],
//    "3":user_answers[2],
//    "4":user_answers[3],
//    "5":user_answers[4],
//    "6":user_answers[5],
//    "7":user_answers[6],
//    "8":user_answers[7],
//    "first_name":user_answers[8],
//    "last_name":user_answers[9],
//    "email":user_answers[10],
//    "phone_number":user_answers[11],
//    };


        let user_answers_upload = {
    "answers":[
        {'question_id':0, 'answer':user_answers[0], 'question':"How are you traveling?"},
        {'question_id':1, 'answer':user_answers[1], 'question':"What type of experience would you like?"},
        {'question_id':2, 'answer':user_answers[2], 'question':"Have you purchased your flights?"},
        {'question_id':3, 'answer':user_answers[3], 'question':"Great. When would you like to go?"},
        {'question_id':4, 'answer':user_answers[4], 'question':"How long are you thinking?"},
        {'question_id':5, 'answer':user_answers[5], 'question':"What type of hotel do you prefer?"},
        {'question_id':6, 'answer':user_answers[6], 'question':"What is your total budget (excluding flights)?"},
        {'question_id':7, 'answer':user_answers[7], 'question':"Any additional information you’d like to tell us?"}
    ],
    "first_name":user_answers[8],
    "last_name":user_answers[9],
    "email":user_answers[10],
    "phone_number":user_answers[11]
    };

    fetch('/get-started', {
    method: 'post',
    headers: {
            "Content-Type": "application/json; charset=utf-8",
        },
    body: JSON.stringify(user_answers_upload)
  }).then(function(response) {
    return response.json();
  }).then(function(data) {
    console.log(data)
  });
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



