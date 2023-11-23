$('#generarPDF').click(function () {
    // Obtener los valores de los campos de formulario
    var Nombre = $('#Nombre').val();
    var nacio = $('#nacio').val();
    var originario = $('#originario').val();
    var nacionalidad = $('#nacionalidad').val();
    var Sexo = $('#Sexo').val();
    var domicilio = $('#domicilio').val();
    var CURP = $('#CURP').val();
    var RFC = $('#RFC').val();
    var Declara = $('#Declara').val();
    var Sociedad = $('#Sociedad').val();
    var domicilios = $('#domicilios').val();
    var actividades = $('#actividades').val();
    var RFCS = $('#RFCS').val();
    var civil = $('#civil').val();
    var partes = $('#partes').val();
    var eventual = $('#eventual').val();
    var precisamente = $('#precisamente').val();
    var consistirán = $('#consistirán').val();
    var mensual = $('#mensual').val();
    var primer = $('#primer').val();
    var primerr = $('#primerr').val();
    var segundo = $('#segundo').val();
    var segundos = $('#segundos').val();
    var tercers = $('#tercers').val();
    var terceros = $('#terceros').val();
    var terminos = $('#terminos').val();
    var de = $('#de').val();
    var del = $('#del').val();

    // Crear un nuevo documento PDF
    var pdf = new jsPDF();


    // Página 1
    var image1 = new Image();
    image1.src = "../../static/documentos/uno.jpg";
    image1.onload = function () {
        pdf.addImage(image1, 'JPG', 0, 0, 200, 300);
        // Agregar contenido adicional para la primera página
        // Set font size and type
        pdf.setFontSize(9.5);
        pdf.setFont("calibri");
        pdf.setFont("helvetica", "bold"); // Set font to bold

        pdf.text(Nombre, 80, 32.8);
        pdf.text(Nombre, 53, 66.3);
        pdf.text(':' + originario, 58, 74.4);
        pdf.text(':' + nacio, 47, 78.5);
        pdf.text(': ' + nacionalidad, 58, 82.9);
        pdf.text(': ' + civil, 51, 86.9);
        pdf.text(': ' + Sexo, 41, 90.9);
        pdf.text(': ' + domicilio, 59, 95.4);
        pdf.text(': ' + CURP, 42, 99.4);
        pdf.text(': ' + RFC, 42, 103.4);
        pdf.text(Declara, 46, 112.2);
        pdf.text(': ' + Sociedad, 75, 120.4);
        pdf.text(': ' + domicilios, 73, 124.4);
        pdf.text(': ' + actividades, 82, 128.8);
        pdf.text(': ' + RFCS, 45, 132.8);
        pdf.text(partes, 28, 220.7);
        pdf.text(eventual, 28, 224.7);
        pdf.text(precisamente, 128, 274.9);





        // Página 2
        var image2 = new Image();
        image2.src = "../../static/documentos/dos.jpg";
        image2.onload = function () {
            pdf.addPage(); // Agregar una nueva página
            pdf.addImage(image2, 'JPG', 0, 0, 200, 300);
            pdf.setFont("helvetica", "bold"); // Set font to bold

            pdf.text(consistirán, 112, 24);
            pdf.text(mensual, 120, 174.9);

            // Página 3
            var image3 = new Image();
            image3.src = "../../static/documentos/tres.jpg";
            image3.onload = function () {
                pdf.addPage(); // Agregar una nueva página
                pdf.addImage(image3, 'JPG', 0, 0, 200, 300);
                pdf.setFont("helvetica", "bold"); // Set font to bold

                pdf.text(primer, 33, 167);
                pdf.text(primerr, 107, 167);
                pdf.text(segundo, 33, 171);
                pdf.text(segundos, 107, 171);

                pdf.text(tercers, 33, 175);
                pdf.text(terceros, 107, 175);
                pdf.text('23', 63, 234);
                pdf.text('noviembre', 100, 234);
                pdf.text('2023', 130, 234);






                pdf.save('CONTRATO_INDIVIDUAL_DE_TRABAJO_POR_TIEMPO_DETERMINADO.pdf');
            };
        };
    };

});


