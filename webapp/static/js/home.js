form.addEventListener('submit', function(e){
    var form = document.querySelector('form')
    var inputext = document.getElementById('inputext').value;
    var newchat = document.createElement('div')
    if(inputext === '') {
        newchat.textContent = 'PAS DE QUESTION RENSEIGNEE';
    }
    else {
        newchat.textContent = inputext;
    }
    form.appendChild(newchat);
})
