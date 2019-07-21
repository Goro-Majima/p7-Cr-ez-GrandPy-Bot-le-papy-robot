var form = document.querySelector('form')
var inputext = document.getElementById('inputext')
var noinput = document.createElement('div')

form.addEventListener('submit', function(e){
    if(inputext.textContent === '') {
        noinput.textContent = 'PAS DE QUESTION RENSEIGNEE';
        form.appendChild(noinput);
    }
})
