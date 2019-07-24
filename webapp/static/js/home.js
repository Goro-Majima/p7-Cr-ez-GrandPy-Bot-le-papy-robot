// Initialize and add the map
function initMap(latitude, longitude) {
    // The location from the question
    var location = {lat: latitude, lng: longitude};
    // The map, centered at location
    var map = new google.maps.Map(
        document.getElementById('map'), {zoom: 15, center: location});
    // The marker, positioned at location
    var marker = new google.maps.Marker({position: location, map: map});
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
    var addressreturn = ''
    var storyreturn = ''
    var longitude = ''
    var latitude = ''
    if(inputext !== '') {
        loader.style.display = "block";
        questionSection.style.display= 'block';
        questionSection.textContent = inputext
        setTimeout(function() {loader.style.display = "none"}, 3000);  
         //Display the response from the view to the different section       
        ajaxGet('http://127.0.0.1:5000/_api', function(reponse){
            jsonreponse = JSON.parse(reponse)
            addressreturn = jsonreponse['papyanswer']+ ' ' + jsonreponse['address']
            storyreturn = jsonreponse["introstory"] + ' ' + jsonreponse["story"]
            latitude = jsonreponse['gps']['lat']
            longitude = jsonreponse['gps']['lng']
            if (jsonreponse['address'] === ''){
                setTimeout(function() {addressSection.style.display= 'block'}, 3000);
                setTimeout(function() {addressSection.textContent = addressreturn}, 3000); 
            }else{                
                setTimeout(function() {addressSection.style.display= 'block'}, 3000);
                setTimeout(function() {addressSection.textContent = addressreturn}, 3000);   
                setTimeout(function() {storySection.style.display= 'block'}, 3000);
                setTimeout(function() {storySection.textContent = storyreturn}, 3000);
                initMap(latitude, longitude)
                setTimeout(function() {gmap.style.display = 'block'}, 3000);
            }
            
        })        
    }
    else {
        questionSection.style.display= 'block';
        questionSection.textContent = 'PAS DE QUESTION RENSEIGNEE';
    }    
})




