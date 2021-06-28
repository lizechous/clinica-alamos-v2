document.addEventListener("DOMContentLoaded", () => {
    // Escuchamos el click del botón
    const $boton = document.querySelector("#btnCrearPdf");
    $boton.addEventListener("click", () => {
        // Obtengo la tabla con los valores para el pdf
        var divTablaPagos = document.getElementById('divTablaPagos');
        // Clono el objeto, ya que necesito ocultar la columna de los botones 
        // sin afectar a la tabla original
        var divTablaPagosClonado = divTablaPagos.cloneNode(true); 
        var tablaPagosClonado = divTablaPagosClonado.getElementsByTagName("table")[0];
        // Getting the rows in table.
        var row = tablaPagosClonado.rows;  

        // Elimino las columnas editar y eliminar.  
        for (var j = 1; j < row.length-1; j++) {
            // Elimino las últimas dos celdas
            row[j].deleteCell(row[j].cells.length-1);
            row[j].deleteCell(row[j].cells.length-1);
        }
        html2pdf()
            .set({
                margin: 1,
                filename: 'documento.pdf',
                image: {
                    type: 'jpeg',
                    quality: 0.98
                },
                html2canvas: {
                    scale: 3, // A mayor escala, mejores gráficos, pero más peso
                    letterRendering: true,
                },
                jsPDF: {
                    unit: "in",
                    format: "a3",
                    orientation: 'portrait' // landscape o portrait
                }
            })
            .from(divTablaPagosClonado)
            .save()
            .catch(err => console.log(err));
    });
});