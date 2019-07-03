// // Affiche de toutes les données saisies ou choisies
// form.addEventListener("submit", function (e) {
//     var question = form.elements.pseudo.value;
    
//     console.log(question)
    
// });

//Use of JQuery to display messages and google map without updating the entire page with ajax function.

$(document).ready(function(){

    $('form').bind('submit', function(event){
        $.getJSON($SCRIPT_ROOT, 
        usertext = $('input[name="usertext"]').val(),
        function(data) {
            $('#papyanswer').text(data.response);
        });
        $('#papyanswer').html('ok')
    });
});
