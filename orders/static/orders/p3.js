document.addEventListener('DOMContentLoaded', () => {
  menu_nav_init();
  p3_restore_menu();
  menu_nav_toggle();

  //Uncaught (in promise) undefine seems to be limited to Chrome, doesn't show in Firefox or Opera
});

function p3_restore_menu() {
  //This function restores the menu quantities to the values in the order object.
  let menuitems=document.getElementsByClassName("menuitem");
  if((sessionStorage.getItem("order")==null)||(sessionStorage.getItem("order").length<3)){
    return;
  }
  var orderARRAY = jsonSTR_to_array(sessionStorage.getItem("order"));
  let i1 = 0;
  for (i1 = 0; i1 < orderARRAY.length; i1++) {
    // Check if like a pizzatype
    if ((orderARRAY[i1]["foodtype"] == "regularpizza")||
      (orderARRAY[i1]["foodtype"] == "sicilianpizza")||
      (orderARRAY[i1]["foodtype"] == "special")||
      (orderARRAY[i1]["foodtype"] == "sub")||
      (orderARRAY[i1]["foodtype"] == "dinnerplatter")) {
      //Is like a pizza
      if (orderARRAY[i1]["toppings"]==null) {
        if ((orderARRAY[i1]["foodtype"] != "sub")&&
          (orderARRAY[i1]["foodtype"] != "dinnerplatter")) {
          // Pizza with no toppings
          itemID = orderARRAY[i1]["foodtype"] + "_" + "0";
        }
        //else sub or dinner platter
        else {
          itemID = orderARRAY[i1]["foodtype"] + "_" + orderARRAY[i1]["foodnameID"];
        }
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
      if(menuitem!=null){
        if ((menuitem.childNodes[1]==undefined)||(menuitem.childNodes[1]==null)) {
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
    }

    //Is not like a pizza
    else {
      itemID = orderARRAY[i1]["foodtype"] + "_" + orderARRAY[i1]["foodnameID"];
      menuitem = document.getElementById(itemID);
      if (menuitem!=null) {
        if ((menuitem.childNodes[1].value=="Add to Order")||
        (menuitem.childNodes[1].innerText=="Add to Order"))
        {
          let tr = menuitem.parentElement;
          menuitem.removeChild(menuitem.childNodes[1])
          qty_plus_minus_buttons(itemID,orderARRAY[i1]["qty"],-1,tr)
        }
      }
    }
    }
  }

function menu_nav_init() {
  if (sessionStorage.getItem("menu_nav")==null) {
    let menu_navSTR = document.getElementById("menu_nav_DICT").innerHTML;
    var menu_navJSON = JSON.parse(document.getElementById("menu_nav_DICT").innerHTML);
    sessionStorage.setItem("menu_nav",JSON.stringify(menu_navJSON));
  }
}

function menu_nav(button) {
  if (sessionStorage.getItem("menu_nav")==null) menu_nav_init();
  var menu_navJSON = JSON.parse(sessionStorage.getItem("menu_nav"));
  if (button=="All") {
    if(!menu_navJSON.All) {
      for (let [key, value] of Object.entries(menu_navJSON)) {
        menu_navJSON[key] = false;
      }
      menu_navJSON.All=true;
    }
    else {
      for (let [key, value] of Object.entries(menu_navJSON)) {
        menu_navJSON[key] = true;
      }
      menu_navJSON.All=false;
    }
  }
  else {
    if (menu_navJSON[button]) {
      menu_navJSON.All=false;
      menu_navJSON[button]=false;
    }
    else {
      menu_navJSON[button]=true;
      menu_navJSON.All=false;
    }
  }
  var no_items_on = true;
  for (let [key, value] of Object.entries(menu_navJSON)) {
    if (menu_navJSON[key] == true) no_items_on = false;
  }
  if (no_items_on) {
    alert("Please Select at least on menu");
    return
  }
  sessionStorage.setItem("menu_nav",JSON.stringify(menu_navJSON));
  menu_nav_toggle();
}

function menu_nav_toggle() {
  var menu_navJSON = JSON.parse(sessionStorage.getItem("menu_nav"));
  // change button colors
  for (let [key, value] of Object.entries(menu_navJSON)) {
    var buttonLIST = document.getElementsByClassName(key);
    for (i = 0; i < buttonLIST.length; i++) {
      if(menu_navJSON[key]) {
        buttonLIST[i].classList.remove('btn-default');
        buttonLIST[i].classList.add('btn-primary');
      }
      else {
        buttonLIST[i].classList.remove('btn-primary');
        buttonLIST[i].classList.add('btn-default');
      }
    }
  }
  // update display hidden settings
  if (menu_navJSON["All"]) {
    for (let [key, value] of Object.entries(menu_navJSON)) {
      if (key!="All") document.getElementById(key).style.display="inline";
    }
    return
  }
  else {
    for (let [key, value] of Object.entries(menu_navJSON)) {
      if (key!="All") {
        if (value) document.getElementById(key).style.display="inline";
        else document.getElementById(key).style.display="none";
      }
    }
  }
}

function initializeOrders(a,b,d,c) {
  var itemID = a + '_' + b;
  var qty = 1;
  var orderARRAY = [];
  var itemDICT = {foodtype:a,foodnameID:b,foodname:d,foodprice:c,qty:1};
  orderARRAY = [itemDICT];
  var orderSTR = JSON.stringify(orderARRAY);
  sessionStorage.setItem("order",orderSTR);
  p3_restore_menu();
}

function add_next_item_to_order(a,b,d,c) {
  //(foodtype,foodnameID,foodname,foodprice)
  var itemID = a + '_' + b;
  if(sessionStorage.getItem("order")!=null) orderARRAY = jsonSTR_to_array(sessionStorage.getItem("order"));
  else var orderARRAY = [];
  if (document.getElementById(itemID).childNodes[1].value=="Add to Order") {
    var qty =1;
    itemDICT = {foodtype:a,foodnameID:b,foodname:d,foodprice:c,qty:qty};
    console.log(itemDICT);
    orderARRAY.push(itemDICT);
    //console.log(orderARRAY);
    sessionStorage.setItem("order",JSON.stringify(orderARRAY));
    if ((a == "regularpizza")||(a == "sicilianpizza")|| (a == "special"))
    {
      //Is a pizza
    }
    else {
      p3_restore_menu();
      return;
    }
  }
  else {
    qty = parseInt(document.getElementById(itemID).childNodes[1].value) + 1
    var i;
    for (i = 0; i < orderARRAY.length; i++) {
      if ((orderARRAY[i]["foodtype"]==a)&&(orderARRAY[i]["foodnameID"]==b)) {
        orderARRAY[i]["qty"] = qty;
      }
    }
  }
  sessionStorage.setItem("order",JSON.stringify(orderARRAY));
  p3_restore_menu();
}

function reset_item(a,b,d,c) {
  var orderARRAY = jsonSTR_to_array(sessionStorage.getItem("order"));
  var i;
  for (i = 0; i < orderARRAY.length; i++) {
    if ((orderARRAY[i]["foodtype"]==a)&&(orderARRAY[i]["foodnameID"]==String(b))) {
      orderARRAY.splice(i,1);
    }
  }
  var itemID = a + '_' + b;
  document.getElementById(itemID+"_placeholder").style.display="none";
  document.getElementById(itemID+"_resetspan").style.display="none";
  document.getElementById(itemID).childNodes[1].classList.remove("btn-success");
  document.getElementById(itemID).childNodes[1].classList.add("btn-primary");
  document.getElementById(itemID).childNodes[1].value="Add to Order";
  sessionStorage.setItem("order",JSON.stringify(orderARRAY));
}
