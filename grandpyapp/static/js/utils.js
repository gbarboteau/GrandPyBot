let button = $('#submit');
$("#image-answer").hide();

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
            $("#answers").append('<p class="answer"><div class="speech-bubble">' + search['place_phrase'] + " L'adresse est le " + search['info_id'] + '<br>' +'</div></p>');
            $("#answers").append('<p class="answer"><div class="speech-bubble">' + search['wiki_phrase'] + " " + search['MyDesc']  + '<br>' + '</div></p>');
        }
    })
});

