
// Function for generating the PDF
$('#generarPDF').click(function () {

    // Obtener los valores de los campos de formulario
    // Obtener los valores de los campos de formulario
    var nombre = $('#nombreInput').val();
    var departamento = $('#departamento').val();
    var ingreso = $('#ingreso').val();
    var anios = $('#anios').val();
    var dias = $('#dias').val();
    var dias_a_gozar = $('#dias_a_gozar').val();
    var dias_pendientes = $('#dias_pendientes').val();
    var inicio = $('#inicio').val();
    var final = $('#final').val();
    var renaudar = $('#renaudar').val();
    var ejemplo = $('#ejemplo').val();
    var id = $('#id').val();
    var persona = $('#persona').val();
    var tipo = $('#tipo').val();


    // Crear un nuevo documento PDF
    var pdf = new jsPDF();




    // Configurar el tamaño de la fuente por defecto
    pdf.setFontSize(12);
    $width = 85; // Anchura del rectángulo
    $height = 7; // Altura del rectángulo
    $x = 105 - $width / 2; // Calcula la coordenada x centrada
    $y = 20 - $height / 2; // Calcula la coordenada y centrada
    pdf.setFillColor(255, 255, 255);
    pdf.rect($x, $y, $width, $height, 'F');
    // Dibujar el contorno del rectángulo
    pdf.rect($x, $y, $width, $height, 'D');
    pdf.setDrawColor(0, 0, 0);

    pdf.text("TESCA BUSINESS WIN WIN S.A.S", 105, 20, 'center');


    // Agregar un subtítulo con fondo azul claro
    $width = 85; // Anchura del rectángulo
    $height = 8; // Altura del rectángulo
    $x = 105 - $width / 2; // Calcula la coordenada x centrada
    $y = 27 - $height / 2; // Calcula la coordenada y centrada
    pdf.setFillColor(32, 55, 100);
    pdf.rect($x, $y, $width, $height, 'F');
    pdf.setTextColor(255, 255, 255); // Establecer color del texto a blanco
    pdf.rect($x, $y, $width, $height, 'D');
    pdf.setDrawColor(0, 0, 0);

    pdf.text("SOLICITUD DE VACACIONES", 105, 27, 'center');
    pdf.setTextColor(0, 0, 0); // Establecer color del texto a blanco

    // Configurar el tamaño de la fuente para el contenido
    pdf.setFontSize(11);

    // Agregar contenido con estilo

    pdf.setFont('normal');
    $width = 23; // Anchura del rectángulo
    $height = 8; // Altura del rectángulo
    $x = 25 - $width / 2; // Calcula la coordenada x centrada
    $y = 40 - $height / 2; // Calcula la coordenada y centrada

    // Establecer el color de relleno
    pdf.setFillColor(173, 216, 230);
    // Dibujar un rectángulo relleno
    pdf.rect($x, $y, $width, $height, 'F');
    // Establecer el color de contorno (negro en este caso)
    pdf.setDrawColor(0, 0, 0);
    // Dibujar el contorno del rectángulo
    pdf.rect($x, $y, $width, $height, 'D');
    // Establecer el color del texto (negro en este caso)
    pdf.setTextColor(0, 0, 0);
    // Agregar el texto "DEPTO" en la posición (20, 50)
    pdf.text("DEPTO", 20, 40);



    $width = 22; // Anchura del rectángulo
    $height = 8; // Altura del rectángulo
    $x = 47 - $width / 2; // Calcula la coordenada x centrada
    $y = 40 - $height / 2; // Calcula la coordenada y centrada
    // Establecer el color de relleno
    pdf.setFillColor(255, 255, 255);
    // Dibujar un rectángulo relleno
    pdf.rect($x, $y, $width, $height, 'F');
    // Establecer el color de contorno (negro en este caso)
    pdf.setDrawColor(0, 0, 0);
    // Dibujar el contorno del rectángulo
    pdf.rect($x, $y, $width, $height, 'D');
    pdf.text("AGUA", 40, 40);

    $width = 22; // Anchura del rectángulo
    $height = 8; // Altura del rectángulo
    $x = 67 - $width / 2; // Calcula la coordenada x centrada
    $y = 40 - $height / 2; // Calcula la coordenada y centrada
    // Establecer el color de relleno
    pdf.setFillColor(173, 216, 230);
    // Dibujar un rectángulo relleno
    pdf.rect($x, $y, $width, $height, 'F');
    // Establecer el color de contorno (negro en este caso)
    pdf.setDrawColor(0, 0, 0);
    // Dibujar el contorno del rectángulo
    pdf.rect($x, $y, $width, $height, 'D');
    pdf.text("ÁREA", 60, 40);
    $width = 22; // Anchura del rectángulo
    $height = 8; // Altura del rectángulo
    $x = 87 - $width / 2; // Calcula la coordenada x centrada
    $y = 40 - $height / 2; // Calcula la coordenada y centrada
    // Establecer el color de relleno
    pdf.setFillColor(255, 255, 255);
    // Dibujar un rectángulo relleno
    pdf.rect($x, $y, $width, $height, 'F');
    // Establecer el color de contorno (negro en este caso)
    pdf.setDrawColor(0, 0, 0);
    // Dibujar el contorno del rectángulo
    pdf.rect($x, $y, $width, $height, 'D');
    pdf.text("LEGAL", 80, 40);
    $width = 22; // Anchura del rectángulo
    $height = 8; // Altura del rectángulo
    $x = 107 - $width / 2; // Calcula la coordenada x centrada
    $y = 40 - $height / 2; // Calcula la coordenada y centrada
    // Establecer el color de relleno
    pdf.setFillColor(173, 216, 230);
    // Dibujar un rectángulo relleno
    pdf.rect($x, $y, $width, $height, 'F');
    // Establecer el color de contorno (negro en este caso)
    pdf.setDrawColor(0, 0, 0);
    // Dibujar el contorno del rectángulo
    pdf.rect($x, $y, $width, $height, 'D');
    pdf.text("CODIGO", 100, 40);
    $width = 40; // Anchura del rectángulo
    $height = 8; // Altura del rectángulo
    $x = 127 - $width / 2 + 10; // Calcula la coordenada x centrada
    $y = 40 - $height / 2; // Calcula la coordenada y centrada
    // Establecer el color de relleno
    pdf.setFillColor(255, 255, 255);
    // Dibujar un rectángulo relleno
    pdf.rect($x, $y, $width, $height, 'F');
    // Establecer el color de contorno (negro en este caso)
    pdf.setDrawColor(0, 0, 0);
    // Dibujar el contorno del rectángulo
    pdf.rect($x, $y, $width, $height, 'D');
    pdf.text("FR1-LE-SV-01", 120, 40);
    $width = 22; // Anchura del rectángulo
    $height = 8; // Altura del rectángulo
    $x = 157 - $width / 2; // Calcula la coordenada x centrada
    $y = 40 - $height / 2; // Calcula la coordenada y centrada
    // Establecer el color de relleno
    pdf.setFillColor(173, 216, 230);
    // Dibujar un rectángulo relleno
    pdf.rect($x, $y, $width, $height, 'F');
    // Establecer el color de contorno (negro en este caso)
    pdf.setDrawColor(0, 0, 0);
    // Dibujar el contorno del rectángulo
    pdf.rect($x, $y, $width, $height, 'D');
    pdf.text("Versión", 150, 40);
    $width = 22; // Anchura del rectángulo
    $height = 8; // Altura del rectángulo
    $x = 177 - $width / 2; // Calcula la coordenada x centrada
    $y = 40 - $height / 2; // Calcula la coordenada y centrada
    // Establecer el color de relleno
    pdf.setFillColor(255, 255, 255);
    // Dibujar un rectángulo relleno
    pdf.rect($x, $y, $width, $height, 'F');
    // Establecer el color de contorno (negro en este caso)
    pdf.setDrawColor(0, 0, 0);
    // Dibujar el contorno del rectángulo
    pdf.rect($x, $y, $width, $height, 'D');


    pdf.text("0", 170, 40);
    $width = 50; // Anchura del rectángulo
    $height = 6; // Altura del rectángulo
    $x = 188 - $width / 2 - 3; // Calcula la coordenada x centrada
    $y = 53 - $height / 2 - 1; // Calcula la coordenada y centrada
    // Establecer el color de relleno
    pdf.setFillColor(255, 255, 255);
    // Dibujar un rectángulo relleno
    pdf.rect($x, $y, $width, $height, 'F');
    // Establecer el color de contorno (negro en este caso)
    pdf.setDrawColor(0, 0, 0);
    // Dibujar el contorno del rectángulo
    pdf.rect($x, $y, $width, $height, 'D');
    // Establecer el color de contorno (negro en este caso)
    pdf.setDrawColor(0, 0, 0);
    var fechaActual = new Date();
    let fechaact = formatearFechaCompleta(fechaActual);
    $width = 11; // Anchura del rectángulo
    $height = 6; // Altura del rectángulo
    $x = 167 - $width / 2 - 3; // Calcula la coordenada x centrada
    $y = 53 - $height / 2 - 1; // Calcula la coordenada y centrada
    // Establecer el color de relleno
    pdf.setFillColor(173, 216, 230);
    // Dibujar un rectángulo relleno
    pdf.rect($x, $y, $width, $height, 'F');

    // Establecer el color de contorno (negro en este caso)
    pdf.setDrawColor(0, 0, 0);
    pdf.rect($x, $y, $width, $height, 'D');

    pdf.text("fecha " + fechaact, 160, 53);

    $width = 280; // Anchura del rectángulo
    $height = 8 - 2; // Altura del rectángulo
    $x = 96 - $width / 2 + 10; // Calcula la coordenada x centrada
    $y = 60 - $height / 2; // Calcula la coordenada y centrada
    pdf.setFillColor(32, 55, 100);
    pdf.rect($x, $y, $width, $height, 'F');
    pdf.setDrawColor(0, 0, 0);
    pdf.rect($x, $y, $width, $height, 'D');
    pdf.setTextColor(255, 255, 255); // Establecer color del texto a blanco

    pdf.text("DATOS DEL SOLICITANTE", 83, 60);
    pdf.setTextColor(0, 0, 0); // Establecer color del texto a blanco

    $width = 18; // Anchura del rectángulo
    $height = 4.5; // Altura del rectángulo
    $x = 5 - $width / 2; // Calcula la coordenada x centrada
    $y = 70 - $height / 2 - 1; // Calcula la coordenada y centrada
    pdf.setFillColor(173, 216, 230);
    pdf.rect($x, $y, $width, $height, 'F');
    pdf.setDrawColor(0, 0, 0);
    pdf.rect($x, $y, $width, $height, 'D');

    pdf.text("Nombre : ", 0, 70);

    $width = 90; // Anchura del rectángulo
    $height = 4.5; // Altura del rectángulo
    $x = 18 - $width / 2 + 40; // Calcula la coordenada x centrada
    $y = 70 - $height / 2 - 1; // Calcula la coordenada y centrada
    pdf.setFillColor(255, 255, 255);
    pdf.rect($x, $y, $width, $height, 'F');
    pdf.setDrawColor(0, 0, 0);
    pdf.rect($x, $y, $width, $height, 'D');
    pdf.text(nombre, 18, 70);
    // Resto del código...


    // Resto del código...

    $width = 65; // Anchura del rectángulo
    $height = 4.5; // Altura del rectángulo
    $x = 120 - $width / 2; // Calcula la coordenada x centrada
    $y = 70 - $height / 2 - 1; // Calcula la coordenada y centrada
    pdf.setFillColor(173, 216, 230);
    pdf.rect($x, $y, $width, $height, 'F');
    pdf.setDrawColor(0, 0, 0);
    pdf.rect($x, $y, $width, $height, 'D');

    pdf.text("No. de empleado : ", 90, 70);
    $width = 65; // Anchura del rectángulo
    $height = 4.5; // Altura del rectángulo
    $x = 175 - $width / 2 + 3; // Calcula la coordenada x centrada
    $y = 70 - $height / 2 - 1; // Calcula la coordenada y centrada
    pdf.setFillColor(255, 255, 255);
    pdf.rect($x, $y, $width, $height, 'F');
    pdf.setDrawColor(0, 0, 0);
    pdf.rect($x, $y, $width, $height, 'D');

    pdf.text(id, 165, 70);


    $width = 18; // Anchura del rectángulo
    $height = 6; // Altura del rectángulo
    $x = 1 - $width / 2 + 5; // Calcula la coordenada x centrada
    $y = 75 - $height / 2 - .7; // Calcula la coordenada y centrada
    pdf.setFillColor(173, 216, 230);
    pdf.rect($x, $y, $width, $height, 'F');
    pdf.setDrawColor(0, 0, 0);
    pdf.rect($x, $y, $width, $height, 'D');

    pdf.text("Área   ", 1, 75);

    $width = 74.4; // Anchura del rectángulo
    $height = 6; // Altura del rectángulo
    $x = 40 - $width / 2 + 10.2; // Calcula la coordenada x centrada
    $y = 75 - $height / 2 - .7; // Calcula la coordenada y centrada
    pdf.setFillColor(255, 255, 255);
    pdf.rect($x, $y, $width, $height, 'F');
    pdf.setDrawColor(0, 0, 0);
    pdf.rect($x, $y, $width, $height, 'D');
    pdf.text(departamento, 40, 75);

    $width = 58; // Anchura del rectángulo
    $height = 6; // Altura del rectángulo
    $x = 120 - $width / 2 - 3.6; // Calcula la coordenada x centrada
    $y = 75 - $height / 2 - .7; // Calcula la coordenada y centrada
    pdf.setFillColor(173, 216, 230);
    pdf.rect($x, $y, $width, $height, 'F');
    pdf.setDrawColor(0, 0, 0);
    pdf.rect($x, $y, $width, $height, 'D');
    pdf.text("Tipo de contrato", 90, 75);

    pdf.text(persona, 165, 75);

    $width = 27; // Anchura del rectángulo
    $height = 5; // Altura del rectángulo
    $x = 1 - $width / 2 + 12; // Calcula la coordenada x centrada
    $y = 82 - $height / 2 - 2; // Calcula la coordenada y centrada
    pdf.setFillColor(173, 216, 230);
    pdf.rect($x, $y, $width, $height, 'F');
    pdf.setDrawColor(0, 0, 0);
    pdf.rect($x, $y, $width, $height, 'D');
    pdf.text("Jefe inmediato", 1, 82);


    $width = 190; // Anchura del rectángulo
    $height = 5; // Altura del rectángulo
    $x = 89 - $width / 2 + 30; // Calcula la coordenada x centrada
    $y = 82 - $height / 2 - 2; // Calcula la coordenada y centrada
    pdf.setFillColor(255, 255, 255);
    pdf.rect($x, $y, $width, $height, 'F');
    pdf.setDrawColor(0, 0, 0);
    pdf.rect($x, $y, $width, $height, 'D');
    pdf.text(ejemplo, 30, 82);


    $width = 60; // Anchura del rectángulo
    $height = 15; // Altura del rectángulo
    $x = 1 - $width / 2 + 17; // Calcula la coordenada x centrada
    $y = 80 - $height / 2 + 10; // Calcula la coordenada y centrada
    pdf.setFillColor(173, 216, 230);
    pdf.rect($x, $y, $width, $height, 'F');
    pdf.setDrawColor(0, 0, 0);
    pdf.rect($x, $y, $width, $height, 'D');


    pdf.text("Persona que queda a cargo de \nsus actividades en su ausencia ", 1, 88);
    pdf.text(tipo, 50, 91);


    $width = 30; // Anchura del rectángulo
    $height = 8; // Altura del rectángulo
    $x = 0 - $width / 2 + 13; // Calcula la coordenada x centrada
    $y = 104 - $height / 2 - 2.2; // Calcula la coordenada y centrada
    pdf.setFillColor(173, 216, 230);
    pdf.rect($x, $y, $width, $height, 'F');
    pdf.setDrawColor(0, 0, 0);
    pdf.rect($x, $y, $width, $height, 'D');
    pdf.text("Fecha de Ingreso: ", 0, 104);
    $width = 60; // Anchura del rectángulo
    $height = 8; // Altura del rectángulo
    $x = 46.5 - $width / 2 + 11.8; // Calcula la coordenada x centrada
    $y = 104 - $height / 2 - 2.2; // Calcula la coordenada y centrada
    pdf.setFillColor(255, 255, 255);
    pdf.rect($x, $y, $width, $height, 'F');
    pdf.setDrawColor(0, 0, 0);
    pdf.rect($x, $y, $width, $height, 'D');

    pdf.text(ingreso, 46.5, 104);


    $width = 35; // Anchura del rectángulo
    $height = 8; // Altura del rectángulo
    $x = 88 - $width / 2 + 18; // Calcula la coordenada x centrada
    $y = 103 - $height / 2 - 1.2; // Calcula la coordenada y centrada
    pdf.setFillColor(173, 216, 230);
    pdf.rect($x, $y, $width, $height, 'F');
    pdf.setDrawColor(0, 0, 0);
    pdf.rect($x, $y, $width, $height, 'D');

    pdf.text("Años de antigüedad   ", 88.7, 103);


    $width = 90; // Anchura del rectángulo
    $height = 8; // Altura del rectángulo
    $x = 160 - $width / 2 + 8; // Calcula la coordenada x centrada
    $y = 103 - $height / 2 - 1.2; // Calcula la coordenada y centrada
    pdf.setFillColor(255, 255, 255);
    pdf.rect($x, $y, $width, $height, 'F');
    pdf.setDrawColor(0, 0, 0);
    pdf.rect($x, $y, $width, $height, 'D');

    pdf.text(anios + ' años', 160, 103);

    // Agregar detalles de la solicitud de vacaciones
    const width = 220; // Anchura del rectángulo
    const height = 8 - 2; // Altura del rectángulo
    const x = 105 - width / 2; // Calcula la coordenada x centrada
    const y = 120 - height / 2; // Calcula la coordenada y centrada
    pdf.setFillColor(32, 55, 100);
    pdf.rect(x, y, width, height, 'F');
    pdf.setDrawColor(0, 0, 0);
    pdf.rect(x, y, width, height, 'D');
    pdf.setTextColor(255, 255, 255); // Establecer color del texto a blanco

    pdf.text("DATOS DE SOLICITUD DE VACACIONES", 105, 120, 'center');
    pdf.setFontSize(13);
    pdf.setTextColor(0, 0, 0); // Establecer color del texto a blanco


    $width = 40; // Anchura del rectángulo
    $height = 7; // Altura del rectángulo
    $x = 40 - $width / 2; // Calcula la coordenada x centrada
    $y = 130 - $height / 2 - 1; // Calcula la coordenada y centrada
    pdf.setFillColor(173, 216, 230);
    pdf.rect($x, $y, $width, $height, 'F');
    pdf.setDrawColor(0, 0, 0);
    pdf.rect($x, $y, $width, $height, 'D');

    pdf.text("Tipos de vacaciones", 40, 130, 'center');

    $width = 40; // Anchura del rectángulo
    $height = 13; // Altura del rectángulo
    $x = 40 - $width / 2; // Calcula la coordenada x centrada
    $y = 140 - $height / 2 - 1; // Calcula la coordenada y centrada
    pdf.setFillColor(255, 255, 255);
    pdf.rect($x, $y, $width, $height, 'F');
    pdf.setDrawColor(0, 0, 0);
    pdf.rect($x, $y, $width, $height, 'D');
    pdf.text("Reglamentarias", 40, 140, 'center');


    pdf.setFontSize(11);
    $width = 110; // Anchura del rectángulo
    $height = 7; // Altura del rectángulo
    $x = 125 - $width / 2 + 30; // Calcula la coordenada x centrada
    $y = 130 - $height / 2 - 1; // Calcula la coordenada y centrada
    pdf.setFillColor(173, 216, 230);
    pdf.rect($x, $y, $width, $height, 'F');
    pdf.setDrawColor(0, 0, 0);
    pdf.rect($x, $y, $width, $height, 'D');

    pdf.text("  Periodo Vacacional  ", 125, 130);


    $width = 16; // Anchura del rectángulo
    $height = 7; // Altura del rectángulo
    $x = 100 - $width / 2 + 8; // Calcula la coordenada x centrada
    $y = 138 - $height / 2 - 1; // Calcula la coordenada y centrada
    pdf.setFillColor(173, 216, 230);
    pdf.rect($x, $y, $width, $height, 'F');
    pdf.setDrawColor(0, 0, 0);
    pdf.rect($x, $y, $width, $height, 'D');
    pdf.text("Desde ", 100, 138);
    $width = 50; // Anchura del rectángulo
    $height = 7; // Altura del rectángulo
    $x = 115 - $width / 2 + 24.3; // Calcula la coordenada x centrada
    $y = 138 - $height / 2 - 1; // Calcula la coordenada y centrada
    pdf.setFillColor(255, 255, 255);
    pdf.rect($x, $y, $width, $height, 'F');
    pdf.setDrawColor(0, 0, 0);
    pdf.rect($x, $y, $width, $height, 'D');

    pdf.text(inicio, 115, 138);

    $width = 15.7; // Anchura del rectángulo
    $height = 7; // Altura del rectángulo
    $x = 100 - $width / 2 + 7.9; // Calcula la coordenada x centrada
    $y = 145 - $height / 2 - 1; // Calcula la coordenada y centrada
    pdf.setFillColor(173, 216, 230);
    pdf.rect($x, $y, $width, $height, 'F');
    pdf.setDrawColor(0, 0, 0);
    pdf.rect($x, $y, $width, $height, 'D');
    pdf.text("Al: ", 100, 145);
    $width = 49.6; // Anchura del rectángulo
    $height = 7; // Altura del rectángulo
    $x = 116 - $width / 2 + 23.5; // Calcula la coordenada x centrada
    $y = 145 - $height / 2 - 1; // Calcula la coordenada y centrada
    pdf.setFillColor(255, 255, 255);
    pdf.rect($x, $y, $width, $height, 'F');
    pdf.setDrawColor(0, 0, 0);
    pdf.rect($x, $y, $width, $height, 'D');

    pdf.text(final, 116, 145);
    $width = 35; // Anchura del rectángulo
    $height = 10; // Altura del rectángulo
    $x = 180 - $width / 2 + 11; // Calcula la coordenada x centrada
    $y = 145 - $height / 2 + 1; // Calcula la coordenada y centrada
    pdf.setFillColor(255, 255, 255);
    pdf.rect($x, $y, $width, $height, 'F');
    pdf.setDrawColor(0, 0, 0);
    pdf.rect($x, $y, $width, $height, 'D');


    pdf.text("Tipo de jornada \n    de  L A V", 180, 145);
    pdf.text(final, 116, 145);

    $width = 19; // Anchura del rectángulo
    $height = 10; // Altura del rectángulo
    $x = 101 - $width / 2 + 8.6; // Calcula la coordenada x centrada
    $y = 158 - $height / 2 - 1; // Calcula la coordenada y centrada
    pdf.setFillColor(173, 216, 230);
    pdf.rect($x, $y, $width, $height, 'F');
    pdf.setDrawColor(0, 0, 0);
    pdf.rect($x, $y, $width, $height, 'D');
    pdf.text("Reingreso  ", 101, 158);


    $width = 47; // Anchura del rectángulo
    $height = 10; // Altura del rectángulo
    $x = 130 - $width / 2 + 11; // Calcula la coordenada x centrada
    $y = 158 - $height / 2 - 1; // Calcula la coordenada y centrada
    pdf.setFillColor(255, 255, 255);
    pdf.rect($x, $y, $width, $height, 'F');
    pdf.setDrawColor(0, 0, 0);
    pdf.rect($x, $y, $width, $height, 'D');
    pdf.text(renaudar, 120, 158);

    $width = 30; // Anchura del rectángulo
    $height = 7; // Altura del rectángulo
    $x = 165 - $width / 2 + 12.5; // Calcula la coordenada x centrada
    $y = 170 - $height / 2 - 1; // Calcula la coordenada y centrada
    pdf.setFillColor(173, 216, 230);
    pdf.rect($x, $y, $width, $height, 'F');
    pdf.setDrawColor(0, 0, 0);
    pdf.rect($x, $y, $width, $height, 'D');

    pdf.text("Días Solicitados: ", 165, 170);
    $width = 15; // Anchura del rectángulo
    $height = 7; // Altura del rectángulo
    $x = 200 - $width / 2; // Calcula la coordenada x centrada
    $y = 170 - $height / 2 - 1; // Calcula la coordenada y centrada
    pdf.setFillColor(32, 55, 100);
    pdf.rect($x, $y, $width, $height, 'F');
    pdf.setDrawColor(0, 0, 0);

    pdf.rect($x, $y, $width, $height, 'D');
    pdf.setTextColor(255, 255, 255);

    pdf.text(dias_a_gozar, 200, 170);
    pdf.setTextColor(0, 0, 0);

    $width = 80; // Anchura del rectángulo
    $height = 7; // Altura del rectángulo
    $x = 5 - $width / 2 + 3; // Calcula la coordenada x centrada
    $y = 180 - $height / 2 - 1; // Calcula la coordenada y centrada
    pdf.setFillColor(32, 55, 100);
    pdf.rect($x, $y, $width, $height, 'F');
    pdf.setDrawColor(0, 0, 0);
    pdf.rect($x, $y, $width, $height, 'D');

    pdf.text("Días Que Corresponden: ", 5, 180);


    $width = 50; // Anchura del rectángulo
    $height = 7; // Altura del rectángulo
    $x = 70 - $width / 2 + 2; // Calcula la coordenada x centrada
    $y = 180 - $height / 2 - 1; // Calcula la coordenada y centrada

    // Establece el color de relleno del rectángulo
    pdf.setFillColor(255, 255, 255);
    pdf.rect($x, $y, $width, $height, 'F');

    // Establece el color de borde del rectángulo
    pdf.setDrawColor(0, 0, 0);
    pdf.rect($x, $y, $width, $height, 'D');

    // Establece el color del texto a blanco
    pdf.setTextColor(255, 255, 255);

    // Dibuja el texto con el nuevo color
    pdf.text("Días Que Corresponden: ", 5, 180);
    pdf.setTextColor(0, 0, 0);

    pdf.text(dias, 70, 180);
    $width = 80; // Anchura del rectángulo
    $height = 7; // Altura del rectángulo
    $x = 130 - $width / 2 + 3; // Calcula la coordenada x centrada
    $y = 180 - $height / 2 - 1; // Calcula la coordenada y centrada
    pdf.setFillColor(32, 55, 100);
    pdf.rect($x, $y, $width, $height, 'F');
    pdf.setDrawColor(0, 0, 0);
    pdf.rect($x, $y, $width, $height, 'D');
    pdf.setTextColor(255, 255, 255);

    pdf.text("Días Pendientes: ", 130, 180);
    pdf.setTextColor(0, 0, 0);

    $width = 50; // Anchura del rectángulo
    $height = 7; // Altura del rectángulo
    $x = 190 - $width / 2 + 2; // Calcula la coordenada x centrada
    $y = 180 - $height / 2 - 1; // Calcula la coordenada y centrada
    pdf.setFillColor(255, 255, 255);
    pdf.rect($x, $y, $width, $height, 'F');
    pdf.setDrawColor(0, 0, 0);
    pdf.rect($x, $y, $width, $height, 'D');

    pdf.text(dias_pendientes, 170, 180);

    // Agregar detalles finales y firma
    pdf.setFontSize(9);

    pdf.text("POR EL PRESENTE EXPRESO MI CONFORMIDAD DE SOLICITAR Y GOZAR MIS VACACIONES DE ACUERDO A LO QUE ESTABLECE EL \nARTÍCULO 76 DE LA LEY FEDERAL DEL TRABAJO, CONSIDERANDO LOS SIGUIENTES DATOS:", 105, 190, 'center');

    pdf.setFontSize(8);
    //firma
    $width = 105; // Anchura del rectángulo
    $height = 16; // Altura del rectángulo
    $x = 52.9 - $width / 2; // Calcula la coordenada x centrada
    $y = 210 - $height / 2 - 1; // Calcula la coordenada y centrada
    pdf.setFillColor(255, 255, 255);
    pdf.rect($x, $y, $width, $height, 'F');
    pdf.setDrawColor(0, 0, 0);
    pdf.rect($x, $y, $width, $height, 'D');

    $width = 104.2; // Anchura del rectángulo
    $height = 7; // Altura del rectángulo
    $x = 49.5 - $width / 2 + 3; // Calcula la coordenada x centrada
    $y = 221.5 - $height / 2 - 1; // Calcula la coordenada y centrada
    pdf.setFillColor(255, 255, 255);
    pdf.rect($x, $y, $width, $height, 'F');
    pdf.setDrawColor(0, 0, 0);
    pdf.rect($x, $y, $width, $height, 'D');
    pdf.text("NOMBRE Y FIRMA DEL SOLICITANTE", 25, 221.5);

    $width = 105; // Anchura del rectángulo
    $height = 16; // Altura del rectángulo
    $x = 156.9 - $width / 2; // Calcula la coordenada x centrada
    $y = 210 - $height / 2 - 1; // Calcula la coordenada y centrada
    pdf.setFillColor(255, 255, 255);
    pdf.rect($x, $y, $width, $height, 'F');
    pdf.setDrawColor(0, 0, 0);
    pdf.rect($x, $y, $width, $height, 'D');

    $width = 105; // Anchura del rectángulo
    $height = 7; // Altura del rectángulo
    $x = 154 - $width / 2 + 3; // Calcula la coordenada x centrada
    $y = 221.5 - $height / 2 - 1; // Calcula la coordenada y centrada
    pdf.setFillColor(255, 255, 255);
    pdf.rect($x, $y, $width, $height, 'F');
    pdf.setDrawColor(0, 0, 0);
    pdf.rect($x, $y, $width, $height, 'D');
    pdf.text("NOMBRE Y FIRMA DE LÍDER DE DEPARTAMENTO ", 125, 221.5);
    $width = 104.0001; // Anchura del rectángulo
    $height = 16; // Altura del rectángulo
    $x = 52.9 - $width / 2 - .5; // Calcula la coordenada x centrada
    $y = 233 - $height / 2 - 1; // Calcula la coordenada y centrada
    pdf.setFillColor(255, 255, 255);
    pdf.rect($x, $y, $width, $height, 'F');
    pdf.setDrawColor(0, 0, 0);
    pdf.rect($x, $y, $width, $height, 'D');

    $width = 104.2; // Anchura del rectángulo
    $height = 7; // Altura del rectángulo
    $x = 49.5 - $width / 2 + 3; // Calcula la coordenada x centrada
    $y = 244.5 - $height / 2 - 1; // Calcula la coordenada y centrada
    pdf.setFillColor(255, 255, 255);
    pdf.rect($x, $y, $width, $height, 'F');
    pdf.setDrawColor(0, 0, 0);
    pdf.rect($x, $y, $width, $height, 'D');
    pdf.text(" NOMBRE Y FIRMA DE ÁREA LEGAL", 25, 244.5);


    $width = 105; // Anchura del rectángulo
    $height = 16; // Altura del rectángulo
    $x = 156.9 - $width / 2; // Calcula la coordenada x centrada
    $y = 233 - $height / 2 - 1; // Calcula la coordenada y centrada
    pdf.setFillColor(255, 255, 255);
    pdf.rect($x, $y, $width, $height, 'F');
    pdf.setDrawColor(0, 0, 0);
    pdf.rect($x, $y, $width, $height, 'D');
    $width = 105; // Anchura del rectángulo
    $height = 7; // Altura del rectángulo
    $x = 154 - $width / 2 + 3; // Calcula la coordenada x centrada
    $y = 244.5 - $height / 2 - 1; // Calcula la coordenada y centrada
    pdf.setFillColor(255, 255, 255);
    pdf.rect($x, $y, $width, $height, 'F');
    pdf.setDrawColor(0, 0, 0);
    pdf.rect($x, $y, $width, $height, 'D');
    pdf.text("NOMBRE Y FIRMA DE   DPTO. AGUA ", 130, 244.5);


    var image1 = new Image();
    // Utiliza una ruta relativa desde la ubicación del script en el servidor local
    image1.src = "../../static/documentos/h.jpg";

    image1.onload = function () {
        pdf.addImage(image1, 'JPEG', 22, 1, 30, 30);

        // Resto del contenido del PDF

    };
    var image2 = new Image();
    // Utiliza una ruta relativa desde la ubicación del script en el servidor local
    image2.src = " ../../static/documentos/a.jpg";


    image2.onload = function () {
        pdf.addImage(image2, 'JPEG', 160, 1, 30, 30);

        // Resto del contenido del PDF


        pdf.save('solicitud_de_vacaciones.pdf');
    };
});

function formatearFechaCompleta(date) {
    const opcionesDeFormato = { day: 'numeric', month: 'long', year: 'numeric' };
    return date.toLocaleDateString('es-ES', opcionesDeFormato);
}

