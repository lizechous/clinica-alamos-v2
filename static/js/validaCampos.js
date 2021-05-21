// SE VALIDA QUE TODOS LOS CAMPOS ESTÉN RELLENADOS 
$(function () {
    $('#id_formulario').validate({
        rules: {
            'txtTarjeta': 'required',
            'txtRut': 'required',
            'txtNombre': 'required',
            'txtFecha': 'required',
            'txtEmail': {
                required: true,
                email: true
            },
            'cmb_Residencia': 'required',
            'cmb_Trabajo': 'required'
        },
        messages: {
            'txtTarjeta': 'Falta ingresar N° de cuenta \n',
            'txtRut': 'Falta ingresar rut \n',
            'txtNombre': 'Falta ingresar nombre \n',
            'txtFecha': 'Falta ingresar fecha de nacimiento \n',

            'txtEmail': {
                required: 'Falta ingresar un correo electronico \n',
                email: 'Falta ingresar correo electronico con el formato correcto. \n'
            },
            'cmb_Residencia': 'Falta especificar comuna de residencia \n',
            'cmb_Trabajo': 'Falta especificar comuna de trabajo \n'
            
        },
        errorElement: "p",
        errorPlacement: function (error, element) {
            error.appendTo("#errors");
        }

    });//end validate
});//end anonymous function


