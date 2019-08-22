document.getElementById("pagetitle").innerHTML = "My Order"
// Read order JSON
if (sessionStorage.length<1) {
  alert("Nothing Ordered");
  console.log("sessionStorage.length<1 - TODO: Return to main menu")
}
var orderARRAY = jsonSTR_to_array(sessionStorage.getItem("order"));
console.log(orderARRAY);
let orderlist = document.getElementById("order");
//let orderARRAYIndex = 0;
//let cl = "qty_plus_minus()";
for (i = 0; i < orderARRAY.length; i++) {
  //Column 1: Item and price
  let tr = document.createElement("tr");
  let item = document.createTextNode(orderARRAY[i].foodname + " $ " + orderARRAY[i].foodprice);
  let td = document.createElement("td");
  td.appendChild(item);
  tr.appendChild(td);
  // Column 2: Quantity pizzabuttons
  let td1 = document.createElement("td");
  //SOMEDAY - pass two arguments, id_prefix and index
  let td_id_prefix = "order+";
  td1.setAttribute("id",td_id_prefix+i);
  let ts1 = document.createElement("button");
  ts1.appendChild(document.createTextNode("+"));
  ts1.setAttribute("class","qty blabel");
  ts1.setAttribute("type","button");
  ts1.setAttribute("data-func","plus");
  ts1.setAttribute("data-field","field1");
  // tdfunc = "qty_plus_minus("+td_id_prefix+","+i+")";
  // ts1.setAttribute("onclick",tdfunc);
  // ts1.setAttribute("onclick","qty_plus_minus("+i+")");
  ts1.setAttribute("onclick","qty_plus_minus("+i+","+1+")");
  td1.appendChild(ts1);
  tr.appendChild(td1);
  let ts2 = document.createElement("input");
  //ts2.appendChild(document.createTextNode(orderARRAY[i].qty));
  ts2.setAttribute("class","btn-info");
  ts2.setAttribute("type","text");
  ts2.setAttribute("name","field1");
  ts2.setAttribute("value",orderARRAY[i].qty);
  td1.appendChild(ts2);

  // let ts3 = document.createElement("span");
  // ts3.appendChild(document.createTextNode("-"));
  let ts3 = ts1.cloneNode(true);
  // td_id_prefix = "order-";
  // td3.setAttribute("id",td_id_prefix+i);

  ts3.innerHTML="-";
  ts3.dataset["func"]="minus";
  ts3.setAttribute("onclick","qty_plus_minus("+i+","+-1+")");
  td1.appendChild(ts3);
  tr.appendChild(td1)
  // Column 3: Delete Button
  let td2 = document.createElement("td");
  td2.appendChild(document.createTextNode("Delete"));
  tr.appendChild(td2);
  orderlist.appendChild(tr);
  di = "delete_item("+(i+1)+")";
  //di = "delete_item(1)";
  orderlist.childNodes[i+1].childNodes[2].setAttribute("class","btn btn-primary");
  orderlist.childNodes[i+1].childNodes[2].setAttribute("onclick",di);
  //orderARRAYIndex++;
  // console.log(i,orderARRAY[i].foodname,orderARRAY[i].foodprice)
  // TODO Erase session storage when last item is delete
}

function delete_item(index) {
  // reset index for header
  index = index - 1;
  orderARRAY.splice(index,1);
  sessionStorage.setItem("order",JSON.stringify(orderARRAY));
  location.reload();
  }

  function add_more_to_order(){
    let input = document.getElementById("order");
    for (i = 0; i < orderARRAY.length; i++) {
      //Check for match with order orderARRAY
      // if no match search orderARRAY for match
      //Get value and update orderARRAY
      let tempx = input.childNodes[i+1].childNodes[1].childNodes[1].value;
      console.log ("tempx: ",tempx,"orderARRAY qty: ",orderARRAY[i]["qty"]);
      orderARRAY[i]["qty"] = tempx;
    }
  //Set sessionStorage
  console.log("set sessionStorage");
  sessionStorage.setItem("order",JSON.stringify(orderARRAY));


console.log(window.history.go(-1));
}

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
