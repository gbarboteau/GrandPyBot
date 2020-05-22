let button = $('#submit');
$("#image-answer").hide();

function initMap(lat, lng) {
  // The location of Uluru
  var uluru = {lat: lat, lng: lng};
  // The map, centered at Uluru
  var map = new google.maps.Map(
      document.getElementById('map'), {zoom: 10, center: uluru});
  // The marker, positioned at Uluru
  var marker = new google.maps.Marker({position: uluru, map: map});
}

button.on('click', function(event) {
    event.preventDefault();
    console.log("ok vu");
    $.ajax({
        url: '/search',
        data: $('form').serialize(),
        dataType : 'json',
        type: 'GET',
        success : function(search){
            console.log(search['MyDesc']);
            $("#image-answer").hide();
            $("#answers").empty();
            $("#image-answer").show();
            $("#answers").append('<p class="answer"><div>' + search['place_phrase'] + " L'adresse est le " + search['info_id'] + '<br>' +'</div></p>');
            $("#answers").append('<p class="answer"><div>' + search['wiki_phrase'] + " " + search['MyDesc']  + '<br>' + '</div></p>');
            // $("#image-answer").append('<div class="more-padding-top more-padding-bottom"><div id="map">' + '</div></div>');
            initMap(parseFloat(search['latitude']), parseFloat(search['longitude']));
        }
    })
});

