document.getElementById("pagetitle").innerHTML = "My Order"
console.log("in p3review_order");
if (sessionStorage.length<1) {//TODO Change check to "order"
  alert("Nothing Ordered");
  window.history.go(-1);
}

function get_orderJS() {
  // Prepares JSON Object to submit to Python
  orderARRAY = jsonSTR_to_array(sessionStorage.getItem("order"))
  orderJSON = JSON.stringify(orderARRAY);
  console.log(orderARRAY,"\n",orderJSON)
  document.getElementById('orderdataJSON').innerText=orderJSON
}


var orderARRAY = jsonSTR_to_array(sessionStorage.getItem("order"));
//console.log(orderARRAY);
let orderlist = document.getElementById("order");
//Populate review_order_html
for (i = 0; i < orderARRAY.length; i++) {
  //Column 1: Item and price
  let tr = document.createElement("tr");
  tr.setAttribute("class","orderitem")
  let item_name = document.createTextNode(orderARRAY[i].foodname);
  let unitprice = parseFloat(orderARRAY[i].foodprice)
  let item_price = document.createTextNode(" $ " + unitprice.toFixed(2));
  let tdname = document.createElement("td");
  let tdprice = document.createElement("td");
  tdname.appendChild(item_name);
  tdprice.appendChild(item_price);
  tr.appendChild(tdname);
  tr.appendChild(tdprice);
  // Column 2: Quantity buttons
  td_id = "order_"+i;
  td_id = orderARRAY[i].foodtype + "_" +orderARRAY[i].foodnameID;
  //td1.setAttribute("id",td_id_prefix+i);
  //TODO assign tr internally
  qty_plus_minus_buttons(td_id,orderARRAY[i].qty,i,tr);
  // Column 3: Delete Button
  let td2 = document.createElement("td");
  td2.appendChild(document.createTextNode("Delete"));
  tr.appendChild(td2);
  //Column 4: Price
  //TODO: update price when quantity is updated
  let td3 = document.createElement("td");
  let price = orderARRAY[i].foodprice*orderARRAY[i].qty
  td3.appendChild(document.createTextNode(" $ " + price.toFixed(2)));
  tr.appendChild(td3);
  orderlist.appendChild(tr);
  di = "delete_item("+(i+1)+")";
  //SOMEDAY: Replace with ID
  td_id_price = td_id + "_PRICE";
  orderlist.childNodes[i+1].childNodes[3].setAttribute("class","btn btn-primary");
  orderlist.childNodes[i+1].childNodes[3].setAttribute("onclick",di);
  orderlist.childNodes[i+1].childNodes[4].setAttribute("id",td_id_price);
  // TODO Erase session storage when last item is delete
}
y=document.getElementById('orderdataJSON')  //For debugging
get_orderJS() //TODO: see if we need to repeat after changes to order
// Moved to common.js 11/16/19
//TODO run as part of update_orderARRAY or another function
// function delete_item(index) {
//   // update in case an item was changed
//   update_orderARRAY();
//   // offset index for header
//   index = index - 1;
//   orderARRAY.splice(index,1);
//   sessionStorage.setItem("order",JSON.stringify(orderARRAY));
//   location.reload();
// }

function add_more_to_order(){
  update_orderARRAY();
  console.log(window.history.go(-1));
}

$('.login_or_guest').click(function(){
  let user_id = document.getElementById('user_id').innerText
  console.log("user_id")
  if (user_id=="None") {
    console.log("button is place_order")
    // make button like this:
    // <td class="login_guest">
    //   <span class="btn btn-primary" style="color:white">
    //     <a class="Order_list" href="{% url 'order_list' %}" >
    //       Order_list {% url 'order_list'%}: Kluge: Use after Retrieve Order</a>
    //     </span>
    //   </td>
  }
  else {
    console.log("button is order list")
  }
});

/* Submit order
Pass order to python
Clear session storage
Reset buttons and cart screen
*/

/* Checkout button
TODO: Allow login to save history
*/

/* Clear session storage on submit order */

function reset_item(a,b,c) {
  //remove time from array
  console.log("115 a,b,c: ",a,b,c)
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
