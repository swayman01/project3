document.addEventListener('DOMContentLoaded', () => {
  //console.log("experimental code - amenuheader:",amenuheader)
});
function add_to_order(foodtype,foodnameID,foodname,foodprice){
  if (sessionStorage.length>0) {
    console.log("sessionStorage.length>0:", sessionStorage.length)
    add_next_item_to_order(foodtype,foodnameID,foodname,foodprice);
  }
  else {
    console.log("sessionStorage.length <1:", sessionStorage.length)
    initializeOrders(foodtype,foodnameID,foodname,foodprice);

  }
  var itemID = foodtype + '-' + foodnameID;
    document.getElementById(itemID+"-placeholder").style.display="inline-flex"
    document.getElementById(itemID+"-resetspan").style.display="inline-flex"
    document.getElementById(itemID).childNodes[1].classList.remove("btn-primary")
    document.getElementById(itemID).childNodes[1].classList.add("btn-success")


  /* TODO: Allow type in value for add button
  */

  /* Submit order
  Pass order to python
  Clear session storage
  Reset buttons and cart screen
  */

  /* Review Order button

  Allow login to save history
  */

  /*
  1. Change button to quantity, with +/- or enter number
  2. Add method to add to cart
  3. Add go to cart button if it isn't already there
  4. Pass order back to python
  */

  /* In Python
  Verify order against price to prevent hacking
  add to history
  */

  /* Clear session storage on submit order and cancel order*/

}

function initializeOrders(a,b,d,c) {
  var itemID = a + '-' + b;
  var qty = 1;
  // console.log(document.getElementById(itemID).childNodes[1].value);
  sessionStorage.clear();
  var orderARRAY = [];
  var itemDICT = {foodtype:a,foodnameID:b,foodname:d,foodprice:c,qty:qty};
  orderARRAY = [itemDICT];
  var orderSTR = JSON.stringify(orderARRAY);
  sessionStorage.setItem("order",orderSTR);
  document.getElementById(itemID).childNodes[1].value=qty;
}

function add_next_item_to_order(a,b,d,c) {
  var itemID = a + '-' + b;
  var orderARRAY = jsonSTR_to_array(sessionStorage.getItem("order"));
  console.log(orderARRAY)
  if (document.getElementById(itemID).childNodes[1].value=="Add to Order") {
    var qty =1;
    itemDICT = {foodtype:a,foodnameID:b,foodname:d,foodprice:c,qty:qty};
    orderARRAY.push(itemDICT);
    console.log(orderARRAY);
  }
  else {
    qty = parseInt(document.getElementById(itemID).childNodes[1].value) + 1
    var i;
    for (i = 0; i < orderARRAY.length; i++) {
      //console.log(orderARRAY[i])
      //console.log(i,"***",orderARRAY[i]["foodtype"]," *** ",orderARRAY[i]["foodnameID"])
      if ((orderARRAY[i]["foodtype"]==a)&&(orderARRAY[i]["foodnameID"]==b)) {
        orderARRAY[i]["qty"] = qty;
      }
    }
  }
  document.getElementById(itemID).childNodes[1].value=qty;
  //console.log(orderARRAY)
  sessionStorage.setItem("order",JSON.stringify(orderARRAY));
}

function reset_item(a,b,d,c) {
  console.log("115 a,b,d,c: ",a,b,d,c)
  var orderARRAY = jsonSTR_to_array(sessionStorage.getItem("order"));
  var i;
  for (i = 0; i < orderARRAY.length; i++) {
    if ((orderARRAY[i]["foodtype"]==a)&&(orderARRAY[i]["foodnameID"]==String(b))) {
      orderARRAY.splice(i,1);
    }
  }
  //console.log("124 orderArray: ",orderARRAY);
  //reset display
  var itemID = a + '-' + b;
  document.getElementById(itemID+"-placeholder").style.display="none"
  document.getElementById(itemID+"-resetspan").style.display="none"
  document.getElementById(itemID).childNodes[1].classList.remove("btn-success")
  document.getElementById(itemID).childNodes[1].classList.add("btn-primary")
  document.getElementById(itemID).childNodes[1].value="Add to Order"
  sessionStorage.setItem("order",JSON.stringify(orderARRAY));
}

function restore_menu() {
console.log("TODO: Restore Menu")
}

function cancel_order() {
  sessionStorage.clear();
  document.location.reload()
}
