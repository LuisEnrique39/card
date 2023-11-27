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
      let entrada = document.getElementById("dia-entrada").value;
      let salida = document.getElementById("dia-salida").value;
      let salariom = document.getElementById("salariom").value;
      let salariod = document.getElementById("salariod").value;
      let devengado = document.getElementById("devengado").value;
      let devenimp = document.getElementById("importe-devengado").value;
      let vacaciones = document.getElementById("pendientes").value;
      let vacaimp = document.getElementById("importe-vacaciones").value;
      let prima = document.getElementById("prima-vacacional").value;
      let diasagui = document.getElementById("parte-aguinaldo").value;
      let aguinaldo = document.getElementById("aguinaldo").value;
      let total = document.getElementById("total").value;
      let fechaActual = new Date();

// Función para formatear la fecha
        function formatearFechaCompleta(date) {
            const opcionesDeFormato = { day: 'numeric', month: 'long', year: 'numeric' };
            return date.toLocaleDateString('es-ES', opcionesDeFormato);
        }

        let fechaact = formatearFechaCompleta(fechaActual);
      

     generatePDF(fechaact, entrada, salida,salariom,salariod,devengado,devenimp,vacaciones,vacaimp,prima,diasagui,aguinaldo,total,nombre);
  })

});




async function generatePDF(fechaact,entrada, salida,salariom,salariod,devengado,devenimp,vacaciones,vacaimp,prima,diasagui,aguinaldo,total,nombre) {

  // modifique aqui 
  const image = await loadImage("../../static/documentos/finiquito1.jpg");
  console.log(image);
  // modifique aqui
  const pdf = new jsPDF('p', 'pt', 'letter');

  // el primer valor despues de los 0 es el ancho, el otro es el alto
  pdf.addImage(image, 'JPG', 0, 0, 612, 792);

  pdf.setFontSize(11);

  pdf.text(fechaact, 198, 83);
  pdf.text(entrada, 250, 278);
  pdf.text(salida, 490, 278);
  pdf.text(salariom, 270, 300);
  pdf.text(salariod, 490, 300);
  pdf.text(devengado, 290, 324);
  pdf.text(devenimp, 490, 324);
  pdf.text(vacaciones, 290, 348);
  pdf.text(vacaimp, 490, 348);
  pdf.text(prima, 490, 371);
  pdf.text(diasagui, 282, 392);
  pdf.text(aguinaldo, 490, 392);

  pdf.setFontStyle('bold'); 
  pdf.text(total, 490, 417);
  pdf.text(nombre, 240, 540);

  pdf.save("Recibo finiquito.pdf");

}