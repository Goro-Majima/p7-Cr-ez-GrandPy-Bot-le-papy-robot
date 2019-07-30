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

  function initmapdiv(){
    var newgmapSection = document.createElement("div");
    newgmapSection.setAttribute("id", "map");
    newgmapSection.classList.add("map");
  }

form.addEventListener('submit', function(e){
    //remove for the view display to /_api
    e.preventDefault();  
    var loader = document.getElementById( "loader" )
    var inputext = document.getElementById('inputext').value;
    //create elements in order to parse the answer 
    var question = new FormData();
    question.append("usertext", inputext);
    var newquestionSection = document.createElement("div");
    var newaddressSection = document.createElement("div");
    // set attribute in order to get the css
    newquestionSection.setAttribute("id", "question"); 
    newaddressSection.setAttribute("id", "address");
    //get the chat section
    var currentDiv = document.getElementById('chat');
    currentDiv.appendChild(newquestionSection);
    currentDiv.appendChild(newaddressSection);

    var addressreturn = '';
    var storyreturn = '';
    var longitude = '';
    var latitude = '';
    if(inputext !== '') {
        loader.style.display = "block";
        newquestionSection.style.display= 'block';
        newquestionSection.textContent = inputext;
        setTimeout(function() {loader.style.display = "none"}, 3000);  
         //Display the response from the view to the different section  
        ajaxPost('/_api',question, function(reponse){
            jsonreponse = JSON.parse(reponse);
            addressreturn = jsonreponse['papyanswer']+ ' ' + jsonreponse['address'];
            storyreturn = jsonreponse["introstory"] + ' ' + jsonreponse["story"];
            latitude = jsonreponse['gps']['lat'];
            longitude = jsonreponse['gps']['lng'];
            if (jsonreponse['address'] === ''){
                setTimeout(function() {newaddressSection.style.display= 'block'}, 1000);
                setTimeout(function() {newaddressSection.textContent = addressreturn}, 1000); 
            }else if(jsonreponse['story']!==''){
                var newgmapSection = document.createElement("div");
                var newstorySection = document.createElement("div");
                newgmapSection.setAttribute("id", "map");
                newgmapSection.classList.add("map");
                newstorySection.setAttribute("id", "story");  
                currentDiv.appendChild(newgmapSection);
                currentDiv.appendChild(newstorySection);
                setTimeout(function() {newaddressSection.style.display= 'block'}, 1000);
                setTimeout(function() {newaddressSection.textContent = addressreturn}, 1000);
                setTimeout(function() {newgmapSection.style.display = 'block'}, 1000);
                initMap(latitude, longitude);
                document.getElementById('map').setAttribute('id','map1');
                setTimeout(function() {newstorySection.style.display= 'block'}, 1000);
                setTimeout(function() {newstorySection.textContent = storyreturn}, 1000);                
            } else{
                setTimeout(function() {newaddressSection.style.display= 'block'}, 1000);
                setTimeout(function() {newaddressSection.textContent = addressreturn}, 1000);
                var newgmapSection = document.createElement("div");
                newgmapSection.setAttribute("id", "map");
                newgmapSection.classList.add("map");
                currentDiv.appendChild(newgmapSection);
                setTimeout(function() {newgmapSection.style.display = 'block'}, 1000);
                initMap(latitude, longitude);
                document.getElementById('map').setAttribute('id','map1');
            }
        })        
    }
    else {
        newquestionSection.style.display= 'block';
        newquestionSection.textContent = 'PAS DE QUESTION RENSEIGNEE';
    }    
})




