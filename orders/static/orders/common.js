// File of common functions for project3
function timestamp(){
  //TODO: Do we use this?
  d = new Date()
  yr = d.getFullYear();
  yrstr = yr.toString();
  mnth = d.getMonth()+1;
  mnthstr = mnth.toString();
  if (mnth < 10) {
    mnthstr = "0" + mnthstr;
  }
  day = d.getDate();
  daystr = day.toString();
  if (day < 10) {
    day = "0" + daystr;
  }
  hr = d.getHours();
  min = d.getMinutes();
  hrstr = hr.toString();
  minstr = min.toString();
  if (hr < 10) {
    hrstr = "0" + hrstr;
  }
  if (min < 10) {
    minstr = "0" + minstr;
  }
  ts = yrstr + "-" + mnthstr + "-" + daystr + " " + hrstr + ":" + minstr;
  return ts;
}

function restore_menu() {
  //This function restores the menu quantities to the values in the order object.
  let menuitems=document.getElementsByClassName("menuitem");
  if(sessionStorage.getItem("order")==null) return;
  var orderARRAY = jsonSTR_to_array(sessionStorage.getItem("order"));
  let i1 = 0;
  for (i1 = 0; i1 < orderARRAY.length; i1++) {
    if ((orderARRAY[i1]["foodtype"] == "regularpizza")||(orderARRAY[i1]["foodtype"] == "sicilianpizza")||
    (orderARRAY[i1]["foodtype"] == "special"))
    {
      //Is a pizza
      if (orderARRAY[i1]["toppings"]==null) {
        // Pizza with no toppings
        itemID = orderARRAY[i1]["foodtype"] + "_" + "0";
      }
      else {
        // Pizza with toppings
        //check for first time this item has shown up in order object
        itemID = orderARRAY[i1]["foodtype"] + "_" + orderARRAY[i1]["toppings"].length;
      }
      menuitem = document.getElementById(itemID);
      if(menuitem==null)
      {
        itemID = itemID + "_BTN";
        menuitem = document.getElementById(itemID);
      }
      //First time this pizza was ordered
      if (menuitem.childNodes[1]==undefined) {
        console.log(menuitem);
      }
      else {
        if ((menuitem.childNodes[1].value=="Add to Order")
        ||(menuitem.childNodes[1].innerText=="Add to Order"))
        {
          menuitem.childNodes[1].innerText = "Add More";
          menuitem.classList.remove("btn-primary");
          menuitem.classList.add("btn-success");
        }
      }
    }

    //Is not a pizza
    else {
      console.log("not a pizza")
      itemID = orderARRAY[i1]["foodtype"] + "_" + orderARRAY[i1]["foodnameID"];
      menuitem = document.getElementById(itemID);
      if ((menuitem.childNodes[1].value=="Add to Order")||
      (menuitem.childNodes[1].innerText=="Add to Order"))
      {
        let tr = menuitem.parentElement;
        menuitem.removeChild(menuitem.childNodes[1])
        qty_plus_minus_buttons(itemID,orderARRAY[i1]["qty"],-1,tr)
        //RESUME: Figure out i , i is td_index
        //qty_plus_minus_buttons(itemID,orderARRAY[i]["qty"],-1,document.getElementById(itemID).parentNode)
        //qty_plus_minus_buttons(itemID);
        //RESUME HERE
        //document.getElementById(itemID).childNodes[1].childNodes[1].value=orderARRAY[i]["qty"];
      }
      else {
      }
    }
  }
  //console.log("loop finished - pause");
}

function jsonSTR_to_array(jsonSTR){
  //This function takes a string that looks like an array of json objects and
  //converts it to a list
  //Strip leading and closing brackets ([])
  jsonSTR = jsonSTR.slice(1,-1);
  jsonLIST = jsonSTR.split("},");
  //console.log("jsonLIST.length: ",jsonLIST.length,jsonLIST)
  for (i=0;i<jsonLIST.length-1;i++){
    jsonLIST[i] = jsonLIST[i].concat("}");
    //console.log(jsonLIST[i])
  }
  for (i=0;i<jsonLIST.length;i++){
    jsonLIST[i] = JSON.parse(jsonLIST[i]);
    //console.log(i,jsonLIST[i],"\n");
  }
  return jsonLIST;
}

function qty_plus_minus(td_id,j) {
  //This function increments quantities when clicking on the plus or minus keys
  // j of 1 signifies +, j of -1 signifies -
  //SOMEDAY: Learn $(this)
  let valMax = 9, valMin = 0;
  let val = td_id.childNodes[1].value;
  let menuitem_id = td_id.id.slice(0,-4);
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
    let i=0;
    for (i = 0; i < orderARRAY.length; i++) {
      let order_id = orderARRAY[i]["foodtype"]+"_"+(orderARRAY[i]["foodnameID"].toString());
      if(menuitem_id==order_id) {
        if (val < valMax) val = parseInt(val)+1;
        orderARRAY[i]["qty"] = parseInt(val);
        td_id.childNodes[1].setAttribute("value",val);
      }
    }
    sessionStorage.setItem("order",JSON.stringify(orderARRAY));
  }
  if (j==-1) {
    for (i = 0; i < orderARRAY.length; i++) {
      let order_id = orderARRAY[i]["foodtype"]+"_"+(orderARRAY[i]["foodnameID"].toString());
      if(menuitem_id==order_id) {
        val = parseInt(val)-1;
        orderARRAY[i]["qty"] = parseInt(val);
        td_id.childNodes[1].setAttribute("value",val);
        // console.log(orderARRAY[i],val);
      }
    }
    sessionStorage.setItem("order",JSON.stringify(orderARRAY));
  }
}

function update_orderARRAY(){
  // reads values on screen and updates orderARRAY file
  // TODO: If qty = 0 Delete item
  // TODO: Move to p3review_orders
  let orderitems=document.getElementsByClassName("orderitem");
  if(sessionStorage.getItem("order")!=null) orderARRAY = jsonSTR_to_array(sessionStorage.getItem("order"));
  else {
    console.log("No stored orders");
    return
  }
  let input = document.getElementById("order");
  console.log("TODO: Add check for no input")
  for (i = 0; i < orderARRAY.length; i++) {
    let item_id = orderARRAY[i]["foodtype"]+"_"+(orderARRAY[i]["foodnameID"].toString());
    for (j=0; j<orderitems.length; j++){
      order_id = orderitems[j].childNodes[2].id.slice(0,-4)
      if(item_id==order_id) {
        orderARRAY[j]["qty"] = parseInt(orderitems[j].childNodes[2].childNodes[1].value);
        //console.log(orderARRAY[i]);
      }
    }
  }
  console.log("set sessionStorage");
  sessionStorage.setItem("order",JSON.stringify(orderARRAY));
}

function qty_plus_minus_buttons(td_id,qty,i,tr)
//TODO eliminate i from argument list
{
  console.log("td_id: ",td_id)
  let td1 = document.createElement("td");
  td_id = td_id + "_BTN";
  td1.setAttribute("id",td_id);
  let ts1 = document.createElement("button");
  ts1.appendChild(document.createTextNode("+"));
  ts1.setAttribute("class","qty blabel");
  ts1.setAttribute("type","button");
  ts1.setAttribute("data-func","plus");
  ts1.setAttribute("data-field","field1");
  ocplus = "qty_plus_minus("+td_id+",1)";
  ts1.setAttribute("onclick",ocplus);
  td1.appendChild(ts1);
  tr.appendChild(td1);

  let ts2 = document.createElement("input");
  ts2.setAttribute("class","btn btn-success");
  ts2.setAttribute("type","button");
  ts2.setAttribute("name","field1");
  ts2.setAttribute("value",qty);
  ts2.setAttribute("id",td_id+"_qty");
  td1.appendChild(ts2);

  let ts3 = ts1.cloneNode(true);
  ts3.innerHTML="-";
  ts3.setAttribute("data-func","minus");
  ocminus = "qty_plus_minus("+td_id+",-1)";
  ts3.setAttribute("onclick",ocminus);
  td1.appendChild(ts3);
  tr.appendChild(td1);
}
