document.getElementById("pagetitle").innerHTML = "My Order"
//TODO Change to My Orders if not the most recent order

if ((sessionStorage.getItem("order")==null)||(sessionStorage.getItem("order").length<3)) {
  alert("Nothing Ordered");
  gohome()
  //window.history.go(-1);
}

function get_orderJS() {
  // Prepares JSON Object to submit to Python
  if ((sessionStorage.getItem("order")==null)||(sessionStorage.getItem("order").length<3)) {
    var orderJSON = ""
  }
  else {
    orderARRAY = jsonSTR_to_array(sessionStorage.getItem("order"))
    orderJSON = JSON.stringify(orderARRAY);
    document.getElementById('orderdataJSON').innerText=orderJSON
  }
}

if ((sessionStorage.getItem("order")==null)||(sessionStorage.getItem("order").length<3)) {
  var orderARRAY = []
}
else{
  var orderARRAY = jsonSTR_to_array(sessionStorage.getItem("order"));
}
let orderlist = document.getElementById("order");
//Populate review_order_html
var order_price=0.
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
  qty_plus_minus_buttons(td_id,orderARRAY[i].qty,i,tr);
  // Column 3: Delete Button
  let td2 = document.createElement("td");
  td2.appendChild(document.createTextNode("Delete"));
  tr.appendChild(td2);
  //Column 4: Line Item Price
  //TODO: update price when quantity is updated
  let td3 = document.createElement("td");
  let price = orderARRAY[i].foodprice*orderARRAY[i].qty
  order_price = order_price + price;
  td3.appendChild(document.createTextNode(" $ " + price.toFixed(2)));
  tdprice.setAttribute("class","item_price Total");
  tr.appendChild(td3);
  orderlist.appendChild(tr);
  di = "delete_item("+(i+1)+")";
  td_id_price = td_id + "_PRICE";
  orderlist.childNodes[i+1].childNodes[3].setAttribute("class","btn btn-primary");
  orderlist.childNodes[i+1].childNodes[3].setAttribute("onclick",di);
  orderlist.childNodes[i+1].childNodes[4].setAttribute("id",td_id_price);
  orderlist.childNodes[i+1].childNodes[4].setAttribute("class","line_item_price");
}
let tr = document.createElement("tr");
let tdname = document.createElement("td");
tdname.setAttribute("colspan","4");
tdname.appendChild(document.createTextNode("Total:"));
let td_order_price = document.createElement("td");
td_order_price.setAttribute("class","line_item_price boldText");
td_order_price.appendChild(document.createTextNode(" $ " + order_price.toFixed(2)));
tr.appendChild(tdname)
tr.appendChild(td_order_price);
orderlist.appendChild(tr);
orderlist.childNodes[1].setAttribute("class","noborders");
y=document.getElementById('orderdataJSON');  //For debugging
get_orderJS() //TODO: see if we need to repeat after changes to order

function add_more_to_order(){
    //check for first item
  if((sessionStorage.getItem("order")!=null)&&(sessionStorage.getItem("order").length>2)) {
    update_orderARRAY();
  }
  console.log(window.history.go(-1));
}

$('.login_or_guest').click(function(){
  let user_id = document.getElementById('user_id').innerText
  console.log("user_id")
  if (user_id=="None") {
    //console.log("button is place_order")
  }
  else {
    console.log("button is order list")
  }
});

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
  //reset display
  var itemID = a + '-' + b;
  document.getElementById(itemID+"-placeholder").style.display="none"
  document.getElementById(itemID+"-resetspan").style.display="none"
  document.getElementById(itemID).childNodes[1].classList.remove("btn-success")
  document.getElementById(itemID).childNodes[1].classList.add("btn-primary")
  document.getElementById(itemID).childNodes[1].value="Add to Order"
  sessionStorage.setItem("order",JSON.stringify(orderARRAY));
}
