document.addEventListener('DOMContentLoaded', () => {
  document.getElementById("pagetitle").innerHTML = "Place Your Order"
});

console.log("in p3place_order");
if (sessionStorage.length<1) {
  alert("Nothing Ordered");
  window.history.go(-1);
}

var orderARRAY = jsonSTR_to_array(sessionStorage.getItem("order"));
orderJSON = JSON.stringify(orderARRAY);
document.getElementById('orderdataJSON').innerText=orderJSON
