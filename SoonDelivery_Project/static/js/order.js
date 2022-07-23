const stuff_price = document.getElementById("stuff_price");

function checkNumber(){
  stuff_price.value = stuff_price.value.replace(/[^0-9.]/g, '').replace(/(\..*)\./g, '$1');
}

stuff_price.addEventListener("input", checkNumber);

