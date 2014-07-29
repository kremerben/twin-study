$(document).ready(function() {

var app_id = '467f2f67';
var app_key = '727ff689667c548878e56369109af78f';

$('#enroll_image').on('click', function() {
   $.ajax("test_post/", {
        success: function(response) {
            console.log(response);
            $('#resultsBox').text(response);
        },
        error: function(error_response) {
            console.log(error_response);
        }
   });
});


$('#eenroll_image').on('click', function() {
    console.log('hello');

    $('#resultsBox').empty();
    var header_settings = {
       "app_id": "6667e13f",
       "app_key": "a5d5074a84da848f6fab9f0a021a0b93",
        "Accept": "*/*",
        "Content-Type": "application/json",
        "contentType": "application/json",
/*
        "User-Agent": "curl/7.30.0",
        "userAgent": "curl/7.30.0"
*/
        };
    var data = {
        "url": "http://dev.kremerdesign.com/twin_study/images/1.jpg",
        "subject_id":"Ben1",
        "gallery_name":"Kremer"
    };
    data = JSON.stringify(data);
    console.log(data);
    $.ajax("http://api.kairos.io/enroll", {
        headers: header_settings,
        type: "POST",
		dataType: "jsonp",
		dataType: "raw",
		json: false,
        contentType: "application/json",
		
/*
		processData: false,
*/
        data: data,
        success: function(response) {
            console.log(response);
            $('#resultsBox').text(response);
        },
        error: function(error_response) {
            console.log(error_response);
        }
    });
});
});
