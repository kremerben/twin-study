$(document).ready(function() {


var myApiKey = 'rd5c6aj88gw6ycbn4sv2n3a6';
var searchQuery = "The Hobbit";
var pageLimit = 10;
var movieInfo = {};


// SEARCH FOR A MOVIE - RETURN 10
currentSearch = [];
$('#searchMovie').on('click', function() {
    currentSearch = [];
    var searchString = $('#searchBox').val();
    $('.movieInfoContainer').empty();
    $.ajax({
        url: 'http://api.rottentomatoes.com/api/public/v1.0/' +
              'movies.json?apikey=' + myApiKey + '&q=' +
               searchString + '&page_limit=' + pageLimit,
        type: 'GET',
        dataType: 'jsonp',
        success: function(movie_response) {
//            console.log(movie_response);
//            console.log(movie_response.movies);
            $.each(movie_response.movies, function(index, movie) {
                movieInfo = {};
                movieInfo.title = movie.title;
                movieInfo.rt_id = movie.id;
                movieInfo.release_year = movie.year;
                movieInfo.critic_rating = movie.ratings.critics_score;
                movieInfo.audience_score = movie.ratings.audience_score;
                movieInfo.mpaa_rating = movie.mpaa_rating;
                movieInfo.runtime = movie.runtime;
                movieInfo.poster = movie.posters.original;
                movieInfo.synopsis = movie.synopsis;
                movieInfo.index = index;
                movieInfo.actors = movie.abridged_cast;
                currentSearch.push(movieInfo);
                postMovie(movieInfo);
            });
        },
        error: function(error_response) {
            console.log(error_response);
        }
    });
});


// BUILD A MOVIE LISTING
var postMovie = function(movieInfo) {
    movieInfo = JSON.stringify(movieInfo);
    $.ajax({
        url: '/new_movie/',
        type: 'POST',
        dataType: 'html',
        data: movieInfo,
        success: function (movie_response) {
//            console.log('b'+ movie_response);
            $('.movieInfoContainer').append(movie_response);
        },
        error: function(error_response) {
            console.log(error_response);
        }
    });
};


// SHOW FAVORITES
$('#showFavorites').on('click', function() {
    $('#favoriteBox').toggle('slow');
    $(this).text(function(i, text){
        return text === "Show Favorites" ? "Hide Favorites" : "Show Favorites";
    });
});


// MORE INFO BUTTON
$(document).on('click', '#moreInfo', function() {
    $(this).siblings('.moreInfoBox').toggle('slow');
    $(this).text(function(i, text){
        return text === "More Information" ? "Hide Information" : "More Information";
    });
});

// SAVE FAVORITE
$(document).on('click', '#favorite', function() {
    var thisOne = $(this);
    var fave_index = thisOne.data('id');
    console.log('a'+ currentSearch);
    console.log('b'+ fave_index);
    console.log(currentSearch[fave_index]);
    movieInfo = JSON.stringify(currentSearch[fave_index]);
    $.ajax({
        url: '/favorite_movie/',
        type: 'POST',
        dataType: 'html',
        data: movieInfo,
        success: function (movie_response) {
            console.log(movie_response);
            thisOne.hide();
            thisOne.parent().parent().appendTo('#favoriteBox');
        }
    });
    $('#favoriteBox').show();
});

// REMOVE FAVORITE
$(document).on('click', '#removeFave', function() {
    movieTitle = $(this).parent().siblings('.col-md-7').find('h2').text();
    movieTitle = JSON.stringify(movieTitle);
    removeMe = $(this).parent().parent();
    $(removeMe).hide();
    $.ajax({
        url: '/remove_movie/',
        type: 'POST',
        dataType: 'jsonp',
        data: movieTitle,
        success: function (movie_response, removeMe) {
        },
        error: function(error_response) {
            console.log(error_response);
        }
    });
});


// TOGGLE SYNOPSIS
$(document).on('click', '.showhide', function() {
    $(this).toggleClass('synopsis');
});

// SHOW MULTI SAVE BUTTON
$(document).on('click', 'input:checkbox', function(){
    var input = $( "input:checkbox" );
    if (input.length > 1){
        $('#multi-save').show();
    } else {
        $('#multi-save').hide();
    }
});


// MULTI SAVE
$(document).on('click', '#multi-save', function(){
    var input = ($('input:checkbox'));
    var thisOne = $(this);
    $.each(input, function(index, value) {
        if (value.checked) {
            movieInfo = JSON.stringify(currentSearch[index]);
            $.ajax({
                url: '/favorite_movie/',
                type: 'POST',
                dataType: 'html',
                data: movieInfo,
                success: function (movie_response) {
                    $(value).hide();
                    $(value).parent().parent().parent().appendTo('#favoriteBox');
                }
            });
//            console.log(index);
//            console.log(value);
//            console.log(value.checked);
        }
    });
});


// GET MOVIE BUTTON = DEPRECATED
$('#getMovie').on('click', function() {
    $.ajax({
        url: 'http://api.rottentomatoes.com/api/public/v1.0/' +
              'movies.json?apikey=' + myApiKey + '&q=' +
               searchQuery + '&page_limit=' + pageLimit,
        type: 'GET',
        dataType: 'jsonp',
        success: function(movie_response) {
            console.log(movie_response);
            var movie = movie_response.movies[0];
            movieInfo.title = movie.title;
            movieInfo.rt_id = movie.id;
            movieInfo.release_year = movie.year;
            movieInfo.critic_rating = movie.ratings.critics_score;
            movieInfo.audience_score = movie.ratings.audience_score;
            movieInfo.mpaa_rating = movie.mpaa_rating;
            movieInfo.runtime = movie.runtime;
            movieInfo.poster = movie.posters.original;
            $('#gotTheMovie').html('<img src="'+movieInfo.poster+'"><h1>'+movieInfo.title+'</h1>');
            console.log(movieInfo);

            $('#saveMovie').show();
        },
        error: function(error_response) {
            console.log(error_response);
        }
    });
});

// SAVE MOVIE = UNUSED IN CURRENT VERSION
$('#saveMovie').on('click', function() {
    movieInfo = JSON.stringify(movieInfo);
    console.log(movieInfo);
    $.ajax({
        url: '/new_movie/',
        type: 'POST',
        dataType: 'html',
        data: movieInfo,
        success: function(movie_response) {
            console.log(movie_response);
            $('.movieInfoContainer').html(movie_response);
            $('#saveMovie').hide();
        },
        error: function(error_response) {
            console.log(error_response);
        }
    });
});



$(document).ready(function() {
	$("#slideshow").zAccordion({
		width: 700,
		height: 310,
		tabWidth: 100,
		invert: true
	});
});


});
