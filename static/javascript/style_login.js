const diaDiv= document.querySelector('.dia');
const nocheDiv= document.querySelector('.noche');
const movimiento= document.querySelector('.btn-registrar a');

movimiento.addEventListener('click', (event)=> {
    diaDiv.classList.add('movimiento-derecha-dia');
    diaDiv.style.background= '#141414';
    nocheDiv.style.display= 'block';
    nocheDiv.classList.add('registro-animacion')
    document.body.style.background= '#141414'
    event.preventDefault();
});