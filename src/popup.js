// Obtenemos los elementos del DOM que vamos a utilizar
const mensajeACifrar = document.getElementById("mensaje-a-cifrar");
const mensajeDescifrado = document.getElementById("mensaje-descifrado");
const mensajeADescifrar = document.getElementById("mensaje-a-descifrar");
const botonCifrar = document.getElementById("boton-cifrar");
const botonDescifrar = document.getElementById("boton-descifrar");

// Definimos la función que se ejecutará cuando el usuario haga clic en el botón "Cifrar"
botonCifrar.onclick = function() {
  // Obtenemos el mensaje a cifrar del área de texto
  const mensaje = mensajeACifrar.value;
  // Enviamos el mensaje al script de Python utilizando la API de mensajes nativa de Chrome
  chrome.runtime.sendMessage({cifrar: mensaje}, function(respuesta) {
    // Actualizamos el área de texto del mensaje cifrado con la respuesta del script de Python
    mensajeDescifrado.value = respuesta.cifrado;
  });
};

// Definimos la función que se ejecutará cuando el usuario haga clic en el botón "Descifrar"
botonDescifrar.onclick = function() {
  // Obtenemos el mensaje cifrado del área de texto
  const mensajeCifrado = mensajeADescifrar.value;
  // Enviamos el mensaje cifrado al script de Python utilizando la API de mensajes nativa de Chrome
  chrome.runtime.sendMessage({descifrar: mensajeCifrado}, function(respuesta) {
    // Actualizamos el área de texto del mensaje descifrado con la respuesta del script de Python
    mensajeACifrar.value = respuesta.descifrado;
  });
};
