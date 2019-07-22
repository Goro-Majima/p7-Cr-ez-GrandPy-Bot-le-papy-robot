// Initialize and add the map
function initMap() {
    // The location of Uluru
    var uluru = {lat: -25.344, lng: 131.036};
    // The map, centered at Uluru
    var map = new google.maps.Map(
        document.getElementById('map'), {zoom: 4, center: uluru});
    // The marker, positioned at Uluru
    var marker = new google.maps.Marker({position: uluru, map: map});
  }

function afficher(response) {
    console.log(JSON.stringify(response));
}

// ajaxGet("http://127.0.0.1:5000", afficher);

form.addEventListener('submit', function(e){
    //remove for the view display
    e.preventDefault();
    var loader = document.getElementById( "loader" )
    var inputext = document.getElementById('inputext').value;
    var newchat = document.getElementById('chat');
    var gmap = document.getElementById('map');
    if(inputext === '') {
        newchat.textContent = 'PAS DE QUESTION RENSEIGNEE';
    }
    else {
        loader.style.display = "block";
        setTimeout( function() {loader.style.display = "none"}, 3000);
        setTimeout(function() {newchat.textContent = inputext},3000);
        setTimeout(function() {gmap.style.display = 'block'}, 3000);
    }
    // ajaxGet("http://127.0.0.1:5000/_api", afficher)
    
})




