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
      let llegada = document.getElementById("inicio").value;
      let hora1 = document.getElementById("hora1").value;
      let hora2 = document.getElementById("hora2").value;
      let fechaActual = new Date();
      let fecha = new Date(llegada);

// Función para formatear la fecha
        function formatearFechaCompleta(date) {
            const opcionesDeFormato = { day: 'numeric', month: 'long', year: 'numeric' };
            return date.toLocaleDateString('es-ES', opcionesDeFormato);
        }

        // Formatear la fecha
        let inicio = formatearFechaCompleta(fecha);
        let fechaact = formatearFechaCompleta(fecha);
      

     generatePDF(nombre, inicio, hora1,hora2,fechaact);
  })

});




async function generatePDF(nombre, inicio, hora1,hora2,fechaact) {

  // modifique aqui 
  const image = await loadImage("../../static/documentos/constancia1.jpg");
  console.log(image);
  // modifique aqui
  const pdf = new jsPDF('p', 'pt', 'letter');

  // el primer valor despues de los 0 es el ancho, el otro es el alto
  pdf.addImage(image, 'JPG', 0, 0, 612, 792);

  pdf.setFontSize(12);

  pdf.text(fechaact, 370, 100);
  pdf.text(nombre, 330, 242);
  pdf.text(inicio, 190, 257);
  pdf.text(hora1, 410, 273);
  pdf.text(hora2, 457, 273);

  pdf.save("Constancia laboral.pdf");

}