document.getElementById("pagetitle").innerHTML = "My Order"

if ((sessionStorage.getItem("order")==null)||(sessionStorage.getItem("order").length<3)) {
  alert("Nothing Ordered");
  gohome()
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

function qty_plus_minus(td_id,j) {
  //This function increments quantities when clicking on the plus or minus keys
  // j of 1 signifies +, j of -1 signifies -

  //SOMEDAY: Learn $(this)
  let valMax = 9, valMin = 0;
  let val = td_id.childNodes[1].value;
  let menuitem_id = td_id.id.slice(0,-4);
  let td_price_id = menuitem_id+"_PRICE"
  if (isNaN(val) || val < valMin) {
    td_id.childNodes[1].setAttribute("value",val);
  }
  if (val >= valMax) val=parseInt(valMax);
  if(sessionStorage.getItem("order")!=null) orderARRAY = jsonSTR_to_array(sessionStorage.getItem("order"));
  else {
    console.log("No stored orders");
    return
  }
  if (j==1) {
    let i = parseInt(td_id.id.split("_")[1])
    // for (i = 0; i < orderARRAY.length; i++) {
    //   let order_id = orderARRAY[i]["foodtype"]+"_"+(orderARRAY[i]["foodnameID"].toString());
      //if(menuitem_id==order_id) {
        if (parseInt(val) < valMax) val = parseInt(val)+1;
        orderARRAY[i]["qty"] = parseInt(val);
        td_id.childNodes[1].setAttribute("value",val);
        update_item_price(td_price_id,orderARRAY[i]);
      //}
    //}
    sessionStorage.setItem("order",JSON.stringify(orderARRAY));
  }
  if (j==-1) {
    for (i = 0; i < orderARRAY.length; i++) {
      let order_id = orderARRAY[i]["foodtype"]+"_"+(orderARRAY[i]["foodnameID"].toString());
      if(menuitem_id==order_id) {
        val = parseInt(val)-1;
        orderARRAY[i]["qty"] = parseInt(val);
        if (parseInt(val)<1) {
          delete_item(i+1)  //updated 2/19/2020
        }
        td_id.childNodes[1].setAttribute("value",val);
        update_item_price(td_price_id,orderARRAY[i]);
      }
    }
    sessionStorage.setItem("order",JSON.stringify(orderARRAY));
  }
  document.location.reload()
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
  // See if we can make changes here and eliminate function qty_plus_minus_review(td_id,j) {
  td_id = "order_"+i;
  // td_id = orderARRAY[i].foodtype + "_" +orderARRAY[i].foodnameID;
  qty_plus_minus_buttons(td_id,orderARRAY[i].qty,i,tr); //tried replacing with line below 2/24/20
  //qty_plus_minus_buttons(i,orderARRAY[i].qty,i,tr);
  // Column 3: Delete Button
  let td2 = document.createElement("td");
  td2.appendChild(document.createTextNode("Delete"));
  tr.appendChild(td2);
  //Column 4: Line Item Price
  let td3 = document.createElement("td");
  let price = orderARRAY[i].foodprice*orderARRAY[i].qty
  order_price = order_price + price;
  td3.appendChild(document.createTextNode(" $ " + price.toFixed(2)));
  tdprice.setAttribute("class","item_price Total");
  tr.appendChild(td3);
  orderlist.appendChild(tr);
  di = "delete_item("+(i+1)+")";
  td_id_price = td_id + "_PRICE";
  orderlist.childNodes[i+1].childNodes[3].setAttribute("class","btn btn-primary delete_button");
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
get_orderJS()

function add_more_to_order(){
    //check for first item
  if((sessionStorage.getItem("order")!=null)&&(sessionStorage.getItem("order").length>2)) {
    update_orderARRAY();
  }
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
