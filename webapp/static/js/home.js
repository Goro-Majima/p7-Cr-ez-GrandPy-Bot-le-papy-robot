form.addEventListener('submit', function(e){
    var loader = document.getElementById( "loader" )
    var inputext = document.getElementById('inputext').value;
    var newchat = document.getElementById('chat');
    if(inputext === '') {
        newchat.textContent = 'PAS DE QUESTION RENSEIGNEE';
    }
    else {
        loader.style.display = "block";
        setTimeout( function() {loader.style.display = "none"}, 3000);
        setTimeout(function() {newchat.textContent = inputext},3000);
        
    }
    //remove for the view display
    e.preventDefault();
})


