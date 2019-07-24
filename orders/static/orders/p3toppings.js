document.addEventListener('DOMContentLoaded', () => {
});
var qtysmallpizza=0;
var qtylargepizza=0;
var add_to_order_flag=false
// Toggle Buttons
function toggleselecttopping(toppingID,numtoppings){
  if (document.getElementById(toppingID).childNodes[1].value=="Select") {
    if (document.getElementById(toppingID).childNodes[1].classList.contains("disabled")==false) {
      document.getElementById(toppingID).childNodes[1].value="Deselect"
      document.getElementById(toppingID).childNodes[1].classList.add('btn-info')
      document.getElementById(toppingID).childNodes[1].classList.remove('btn-default')
    }
  }
  else {
    document.getElementById(toppingID).childNodes[1].value="Select"
    document.getElementById(toppingID).childNodes[1].classList.add('btn-default')
    document.getElementById(toppingID).childNodes[1].classList.remove('btn-info')
    document.getElementById(toppingID).childNodes[1].classList.remove('disabled')
  }
  // Count selected toppins and compare
  selectedtoppingcount = countselectedtoppings();
  if (selectedtoppingcount==numtoppings) {
    document.getElementById("add_to_order").classList.remove('disabled')
    document.getElementById("add_to_order").classList.remove('btn-default')
    document.getElementById("add_to_order").classList.add('btn-primary')
    add_to_order_flag=true
  }
  //when limit is reached don't allow more
  var toppingLIST = document.getElementsByClassName("selectbutton");
  if (selectedtoppingcount>numtoppings) {
    alert("You have exceeded your topping limit. Either deselect a topping or proceed with the order");
    var i;
    for (i = 0; i < toppingLIST.length; i++) {
      if (toppingLIST[i].value=="Select") {
        toppingLIST[i].classList.add("disabled");
      }
    }
    document.getElementById("add_to_order").classList.add('disabled')
    document.getElementById("add_to_order").classList.remove('btn-primary')
    document.getElementById("add_to_order").classList.add('btn-default')
    return
  }
  if ((selectedtoppingcount<numtoppings)&&(add_to_order_flag)
  &&(!(document.getElementById("add_to_order").classList.contains('disabled')))){
    //when if deselect reduces the number of toppings deselect
    document.getElementById("add_to_order").classList.add('disabled')
    document.getElementById("add_to_order").classList.remove('btn-primary')
    document.getElementById("add_to_order").classList.add('btn-default')
    for (i = 0; i < toppingLIST.length; i++) {
    toppingLIST[i].classList.remove("disabled");
    }
    add_to_order_flag=false;
    return
  }
}

function countselectedtoppings() {
  //select top node
  let selectedtoppingcount = 0;
  let toppingLIST = document.getElementsByClassName("selectbutton");
  //loop through childNodes and count
  var i;
  for (i = 0; i < toppingLIST.length; i++) {
    if (toppingLIST[i].value=="Deselect") {
      selectedtoppingcount++;
    }
  }
  return selectedtoppingcount;
}
//deactivate buttons when limit is reached, activate checkout button

$('.qty').click(function() {
  var $t = $(this),
  $in = $('input[name="' + $t.data('field') + '"]'),
  val = parseInt($in.val()),
  valMax = 9,
  valMin = 0;

  // Check if a number is in the field first
  if (isNaN(val) || val < valMin) {
    // If field value is NOT a number, or
    // if field value is less than minimum,
    // ...set value to 0 and exit function
    $in.val(valMin);
    return false;
  }
  else if (val > valMax) {
    // If field value exceeds maximum,
    // ...set value to max
    $in.val(valMax);
    return false;
  }

  // Perform increment or decrement logic
  if ($t.data('func') == 'plus') {
    if (val < valMax) $in.val(val + 1);
  }
  else {
    if (val > valMin) $in.val(val - 1);
  }
  if ($t.data("field")=="field1") {
    qtysmallpizza = parseInt($in.val());
    if (qtysmallpizza > 0) {
      document.getElementById("qtysmallpizza").classList.add('btn-info')
      document.getElementById("qtysmallpizza").classList.remove('btn-default')
    }
    else {
      document.getElementById("qtysmallpizza").classList.add('btn-default')
      document.getElementById("qtysmallpizza").classList.remove('btn-info')
    }
  }
  if ($t.data("field")=="field2") {
    qtylargepizza = parseInt($in.val());
    if (qtylargepizza > 0) {
      document.getElementById("qtylargepizza").classList.add('btn-info')
      document.getElementById("qtylargepizza").classList.remove('btn-default')
    }
    else {
      document.getElementById("qtylargepizza").classList.add('btn-default')
      document.getElementById("qtylargepizza").classList.remove('btn-info')
    }
  }
});

function add_pizza(pizzaID,pizzatype,numtoppings,smallprice,largeprice){
  //gather data
  // console.log("128 pizzatype:",pizzaID, pizzatype,numtoppings,smallprice,largeprice);
  // console.log("129 arguments",arguments[0],arguments[1],arguments[2],arguments[3],arguments[4]);
  pizzaID = arguments[0];
  pizzatype = arguments[1];
  numtoppings = arguments[2];
  smallprice = arguments[3];
  largeprice = arguments[4];
  // console.log("135 pizzatype:",pizzaID, pizzatype,numtoppings,smallprice,largeprice);
  //check for qtylargepizza or qtysmallpizza >0
  qtysmallpizza = parseInt(document.getElementById("qtysmallpizza").value);
  qtylargepizza = parseInt(document.getElementById("qtylargepizza").value);
  if((qtysmallpizza>0)||(qtylargepizza>0)) {}
  else {
    alert("Select the number of small and/or large pizzas with these toppings");
    return
  }

console.log(pizzatype);
var toppingLIST = document.getElementsByClassName("selectbutton");
  //gather info here
  if(parseInt(pizzatype)==0) {
    pizzatypeSTR = "Regular Pizza";
  }
  if(pizzatype==1) {
    pizzatypeSTR = "Sicilian Pizza";
  }
  if(pizzatype==2) {
    pizzatypeSTR = "Special Regular Pizza";
  }
  if(pizzatype==4) {
    pizzatypeSTR = "Special Sicilian Pizza";
  }

  //extract toppings
  var toppings =[]
  var toppingLIST = document.getElementsByClassName("selectbutton");
    var i;
    for (i = 0; i < toppingLIST.length; i++) {
      if (toppingLIST[i].value=="Deselect") {
        //console.log(toppingLIST[i].parentElement.parentElement.parentElement.childNodes[1].innerText);
        toppings.push(toppingLIST[i].parentElement.parentElement.parentElement.childNodes[1].innerText);
      }
    }
    var itemDICT = {}
  if (qtysmallpizza>0){
    itemDICT = {"foodtype":"Small "+pizzatypeSTR,"foodnameID":pizzaID,"foodprice":smallprice,"qty":qtysmallpizza,
    toppings:toppings};
    console.log("itemDICT:",itemDICT)
    //if (firstitem)
    add_pizza_to_order(itemDICT)

  }
  if (qtylargepizza>0){
    itemDICT = {"foodtype":"Large "+pizzatypeSTR,"foodnameID":pizzaID,"foodprice":largeprice,"qty":qtylargepizza,
    toppings:toppings};
    console.log("itemDICT:",itemDICT)
  }

  /*

  //enable shopping  button
  */

  // if (document.getElementById('menutdheaderright').innerHTML=='initial') {
  //   document.getElementById('menutdheaderright').innerHTML='Add Checkout Button';
  //   document.getElementById('menutdheaderright').style.color='white';
  //   initializeOrderWithPizza(pizzaID);
  // }
  // else {
  //   add_pizza_to_order(pizzaID);
  // }
}
function initializeOrderWithPizza(pizzaID){
  //var itemID = a + '-' + b;
  //var qty = 1;
  // console.log(document.getElementById(itemID).childNodes[1].value);
  sessionStorage.clear();
  var orderARRAY = [];
  console.log("create orderARRAY here")
  // var orderSTR = JSON.stringify(orderARRAY);
  // sessionStorage.setItem("order",orderSTR);
  // document.getElementById(itemID).childNodes[1].value=qty;
  // console.log(itemID)
  // console.log("TODO: Write code for pizza as first item");
  // TODO Open Pizza html
}
function add_pizza_to_order(itemDICT) {
  console.log(itemDICT)
  if (document.getElementById('menutdheaderright').innerHTML=='initial') {
    document.getElementById('menutdheaderright').innerHTML='Add Checkout Button';
    document.getElementById('menutdheaderright').style.color='white';
    var orderARRAY = [];
    orderARRAY = [itemDICT];
    let orderSTR = JSON.stringify(orderARRAY);
    sessionStorage.setItem("order",orderSTR);
  }
  else {
    let a = "test"
    //let itemID = a + "-" + pizzaID;
    let orderARRAY = jsonSTR_to_array(sessionStorage.getItem("order"));
    console.log(orderARRAY)
    orderARRAY.push(itemDICT);
    sessionStorage.setItem("order",JSON.stringify(orderARRAY));
  }
  console.log(window.location.pathname)
  //add_pizza("GET")
  //$.get("/orders/templates/orders/add_pizza.html")
}
