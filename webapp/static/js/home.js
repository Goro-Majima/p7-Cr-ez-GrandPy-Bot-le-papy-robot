function afficher(response) {
    console.log(response);
}

ajaxGet("http://127.0.0.1:5000", afficher);

form.addEventListener('submit', function(e){
    //remove for the view display
    e.preventDefault();
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
        ajaxGet("http://127.0.0.1:5000/_api", afficher)
    }
    
    
})




