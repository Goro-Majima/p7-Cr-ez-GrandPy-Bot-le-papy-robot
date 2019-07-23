// Initialize and add the map
function initMap() {
    // The location from the question
    var location = {lat: -25.344, lng: 131.036};
    // The map, centered at location
    var map = new google.maps.Map(
        document.getElementById('map'), {zoom: 4, center: location});
    // The marker, positioned at location
    var marker = new google.maps.Marker({position: location, map: map});
  }

function afficher(response) {
    console.log(response);
}

form.addEventListener('submit', function(e){
    //remove for the view display
    e.preventDefault();
    var loader = document.getElementById( "loader" )
    var inputext = document.getElementById('inputext').value;
    var questionSection = document.getElementById('question');
    var addressSection = document.getElementById('address');
    var storySection = document.getElementById('story');
    var gmap = document.getElementById('map');
    if(inputext !== '') {
        loader.style.display = "block";
        questionSection.style.display= 'block';
        questionSection.textContent = inputext
        setTimeout(function() {loader.style.display = "none"}, 3000);        
        setTimeout(function() {addressSection.style.display= 'block'}, 3000);

        //Display the response from the view to the different section 
        ajaxGet("http://127.0.0.1:5000/_api", afficher);
        setTimeout(function() {addressSection.textContent = 'adress section'}, 3000);
        setTimeout(function() {storySection.style.display= 'block'}, 3000);
        setTimeout(function() {storySection.textContent = "story section:Le Lorem Ipsum est simplement du faux texte employé dans la composition et la mise en page avant impression. Le Lorem Ipsum est le faux texte standard de l'imprimerie depuis les années 1500, quand un imprimeur anonyme assembla ensemble des morceaux de texte pour réaliser un livre spécimen de polices de texte. Il n'a pas fait que survivre cinq siècles, mais s'est aussi adapté à la"}, 3000);
        setTimeout(function() {gmap.style.display = 'block'}, 3000);
        
    }
    else {
        questionSection.style.display= 'block';
        questionSection.textContent = 'PAS DE QUESTION RENSEIGNEE';
    }    
})




