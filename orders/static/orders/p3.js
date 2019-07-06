document.addEventListener('DOMContentLoaded', () => {
});
function add_to_order(foodtype,foodnameID,foodprice){
  if (document.getElementById('menutdheaderright').innerHTML=='initial') {
    document.getElementById('menutdheaderright').innerHTML='Add Checkout Button';
    document.getElementById('menutdheaderright').style.color='white';
    initializeOrders(foodtype,foodnameID,foodprice);
  }
  else {
    add_next_item_to_order(foodtype,foodnameID,foodprice);
  }
  var itemID = foodtype + '-' + foodnameID;
    console.log(itemID+"-placeholder")
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

  /* Checkout button
  Open screen with summary of order
  Allow editing, deleting, return to menu for update
  Allow login to save history
  */

  /*
  1. Change button to quantity, with +/- or enter number
  2. Add method to add to cart
  3. Add go to cart button if it isn't already there
  4. Pass order back to python
  */

  /* Define item to return
  Look at project 2
  {"foodprice":foodprice, "key":User.id+"-"+orderitem.id}
  Convert to JSON?
  */

  /* In Python
  Accumulate items
  Shopping cart with modify, login for history

  */

  /* Clear session storage on submit order */

}
function initializeOrders(a,b,c) {
  var itemID = a + '-' + b;
  var qty = 1;
  // console.log(document.getElementById(itemID).childNodes[1].value);
  sessionStorage.clear();
  var orderARRAY = [];
  var itemDICT = {foodtype:a,foodnameID:b,foodprice:c,qty:qty};
  orderARRAY = [itemDICT];
  var orderSTR = JSON.stringify(orderARRAY);
  sessionStorage.setItem("order",orderSTR);
  document.getElementById(itemID).childNodes[1].value=qty;
  // test = sessionStorage.getItem("order");
  // console.log(test);
  // test = jsonSTR_to_array(test);
  // console.log(test);
}

function add_next_item_to_order(a,b,c) {
  var itemID = a + '-' + b;
  var orderARRAY = jsonSTR_to_array(sessionStorage.getItem("order"));
  console.log(orderARRAY)
  if (document.getElementById(itemID).childNodes[1].value=="Add to Order") {
    var qty =1;
    itemDICT = {foodtype:a,foodnameID:b,foodprice:c,qty:qty};
    orderARRAY.push(itemDICT);
    console.log(orderARRAY);
  }
  else {
    qty = parseInt(document.getElementById(itemID).childNodes[1].value) + 1
    //itemDICT = {foodtype:a,foodnameID:b,foodprice:c,qty:qty};
    var i;
    for (i = 0; i < orderARRAY.length; i++) {
      console.log(i,"***",orderARRAY[i]["foodtype"]," *** ",orderARRAY[i]["foodname"])
      if ((orderARRAY[i]["foodtype"]==a)&&(orderARRAY[i]["foodnameID"]==b)) {
        orderARRAY[i]["qty"] = qty;
      }
    }
  }
  document.getElementById(itemID).childNodes[1].value=qty;
  console.log(orderARRAY)
  sessionStorage.setItem("order",JSON.stringify(orderARRAY));
}

function reset_item(a,b,c) {
  //remove time from array
  console.log("115 a,b,c: ",a,b,c)
  var orderARRAY = jsonSTR_to_array(sessionStorage.getItem("order"));
  var i;
  for (i = 0; i < orderARRAY.length; i++) {odnameID"])
    if ((orderARRAY[i]["foodtype"]==a)&&(orderARRAY[i]["foodnameID"]==String(b))) {
      orderARRAY.splice(i,1);
    }
  }
  console.log("124 orderArray: ",orderARRAY);
  //reset display
  var itemID = a + '-' + b;
  document.getElementById(itemID+"-placeholder").style.display="none"
  document.getElementById(itemID+"-resetspan").style.display="none"
  document.getElementById(itemID).childNodes[1].classList.remove("btn-success")
  document.getElementById(itemID).childNodes[1].classList.add("btn-primary")
  document.getElementById(itemID).childNodes[1].value="Add to Order"
  sessionStorage.setItem("order",JSON.stringify(orderARRAY));
}
