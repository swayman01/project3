document.addEventListener('DOMContentLoaded', () => {
  document.getElementById("pagetitle").innerHTML = "Order Placed"
});

console.log("in p3checkout");
if (sessionStorage.length<1) {
  alert("Nothing Ordered");
  window.history.go(-1);
}



//Populate review_order_html, update for confirm order

// for (i = 0; i < orderARRAY.length; i++) {
//   //Column 1: Item and price
//   let tr = document.createElement("tr");
//   tr.setAttribute("class","orderitem")
//   let item_name = document.createTextNode(orderARRAY[i].foodname);
//   let item_price = document.createTextNode(" $ " + orderARRAY[i].foodprice);
//   let tdname = document.createElement("td");
//   let tdprice = document.createElement("td");
//   tdname.appendChild(item_name);
//   tdprice.appendChild(item_price);
//   tr.appendChild(tdname);
//   tr.appendChild(tdprice);
//   // Column 2: Quantity buttons
//   td_id = "order_"+i;
//   td_id = orderARRAY[i].foodtype + "_" +orderARRAY[i].foodnameID;
//   //td1.setAttribute("id",td_id_prefix+i);
//   //TODO assign tr internally
//   qty_plus_minus_buttons(td_id,orderARRAY[i].qty,i,tr);
//   // Column 3: Delete Button
//   let td2 = document.createElement("td");
//   td2.appendChild(document.createTextNode("Delete"));
//   tr.appendChild(td2);
//   orderlist.appendChild(tr);
//   di = "delete_item("+(i+1)+")";
//   //SOMEDAY: Replace with ID
//   orderlist.childNodes[i+1].childNodes[3].setAttribute("class","btn btn-primary");
//   orderlist.childNodes[i+1].childNodes[3].setAttribute("onclick",di);
//   // TODO Erase session storage when last item is delete
// }



/* Submit order
Pass order to python
Clear session storage
Reset buttons and cart screen
*/

/* Checkout button
TODO: Allow login to save history
*/

/* Define item to return
Look at project 2
{"foodprice":foodprice, "key":User.id+"-"+itemDICT.id}
Convert to JSON?
*/

/* In Python
Accumulate items
Shopping cart with modify, login for history

*/

/* Clear session storage on submit order */
