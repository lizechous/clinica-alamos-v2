function alphaOnly(event) {
    var key = event.keyCode;`enter code here`
    return ((key >= 65 && key <= 90) || key == 8);
  };

  function isNumberKey(evt){
    var charCode = (evt.which) ? evt.which : event.keyCode
    if (charCode > 31 && (charCode < 48 || charCode > 57))
        return false;
    return true;
};