const diaDiv= document.querySelector('.dia');
const nocheDiv= document.querySelector('.noche');
const movimiento= document.querySelector('.btn-registrar a');
const cancelarBtn= document.querySelector('.btn-registrar-usuario');

movimiento.addEventListener('click', (event)=> {
    nocheDiv.classList.add('movimiento-derecha-dia');
    diaDiv.style.background= '#141414';
    nocheDiv.style.display= 'block';
    document.body.style.background= '#141414';
    diaDiv.style.display = 'none';
    event.preventDefault();
});

cancelarBtn.addEventListener('click', (event) =>{
    nocheDiv.style.display = 'none';
    document.body.style.background= '#0ea7db';
    diaDiv.style.background= '#fff';
    diaDiv.classList.add('movimiento-inicio-izquierda');
    diaDiv.style.display = 'block'; 
    event.preventDefault();
});

//Validacion del formulario 
var csrftoken = 'YOUR_CSRF_TOKEN_VALUE';
$(document).ready(function() {
    $('#registrar_usuario').submit(function(event) {
      event.preventDefault(); // Prevent default form submission

      var email_usuario= $("#email_usuario").val();
      var form = $(this);
      var csrftoken = form.find('input[name="csrfmiddlewaretoken"]').val();
  
      // Validate passwords and required fields
      if (!validarCamposRequeridos() || !validarPassword()) {
        return; // Prevent AJAX request if validation fails
      }
  
      // Send AJAX request to validate email on server
      $.ajax({
        url: '/login/', // URL of the 'validarCampos' view
        method: 'POST',
        data: {
          'csrfmiddlewaretoken': csrftoken,
          'email_usuario': email_usuario,
          'nombre_usuario': $('#nombre_usuario').val(),
          'fecha_nacimiento': $('#fecha_nacimiento').val(),
          'password1': $('#password1').val(),
          'password2': $('#password2').val(),
        },
        dataType: 'json',
        success: function(response) {
          if (response.valide === true) {
            console.log("si ejecuta envio")
            // aqui se presenta el mensaje cuando deberia mostrar el que funciona xd
            $('#alertaError').css('color', '#29A52D');
            $('#alertaError').text("Usuario creado correctamente!");
            $('#registrar_usuario').submit(); // Submit the form after a delay

          } else if (response.valide === false) {
            console.log("correo ya existe")
            // If there are errors, display them in the 'alertaError' label
            $('#alertaError').text("El correo electronico ya se encuentra en uso!");
          }
        },
        error: function(error) {
          console.error('Error al validar campos:', error);
        },
      });
    });
  });

  //validar que todos los campos no esten vacios
  function validarCamposRequeridos() {
    const requiredFields = ['email_usuario', 'nombre_usuario', 'fecha_nacimiento', 'password1', 'password2'];

  for (const field of requiredFields) {
    if (!$('#' + field).val()) {//de alguna forma '#' toma todas las ids
      $('#alertaError').text("Todos los campos son obligatorios.");
      return false;
    }
  }
  // Return true if all fields are filled
  return true;
  }


//validar password
function validarPassword(){
  const password1 = $('#password1').val();
  const password2 = $('#password2').val();
  const minimo= 8;

  if (password1 !== password2){
    $('#alertaError').text("Las contraseñas no coinciden");
    return false;
  }else if(password1 < minimo){
    $('#alertaError').text("La contraseña es muy corta debe ser de minimo 8 caracteres");
    return false;
  }

  return true;
}