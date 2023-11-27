function loadImage(url) {
    return new Promise(resolve => {
        const xhr = new XMLHttpRequest();
        xhr.open('GET', url, true);
        xhr.responseType = "blob";
        xhr.onload = function (e) {
            const reader = new FileReader();
            reader.onload = function(event) {
                const res = event.target.result;
                resolve(res);
            }
            const file = this.response;
            reader.readAsDataURL(file);
        }
        xhr.send();
    });
}


window.addEventListener('load', async () => {
    const form = document.querySelector('#form');
    form.addEventListener('submit', (e) => {
      e.preventDefault();

      let nombre = document.getElementById("nombre").value;
      let fechaActual = new Date();

// Función para formatear la fecha
        function formatearFechaCompleta(date) {
            const opcionesDeFormato = { day: 'numeric', month: 'long', year: 'numeric' };
            return date.toLocaleDateString('es-ES', opcionesDeFormato);
        }

        let fechaact = formatearFechaCompleta(fechaActual);
      

     generatePDF(nombre,fechaact);
  })

});




async function generatePDF(nombre,fechaact) {

  // modifique aqui 
  const image = await loadImage("../../static/documentos/renuncia1.jpg");
  console.log(image);
  // modifique aqui
  const pdf = new jsPDF('p', 'pt', 'letter');

  // el primer valor despues de los 0 es el ancho, el otro es el alto
  pdf.addImage(image, 'JPG', 0, 0, 612, 792);

  pdf.setFontSize(11);

  pdf.text(fechaact, 374, 82);

  pdf.setFontSize(14); // Tamaño de fuente
  pdf.setFontStyle('bold'); 
  pdf.text(nombre, 240, 480);

  pdf.save("Carta de renuncia.pdf");

}