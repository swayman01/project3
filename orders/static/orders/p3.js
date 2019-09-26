document.addEventListener('DOMContentLoaded', () => {
  menu_nav_init();
  restore_menu();
  menu_nav_toggle();
});

function menu_nav_init() {
  if (sessionStorage.getItem("menu_nav")==null) {
    let menu_navSTR = document.getElementById("menu_nav_DICT").innerHTML;
    var menu_navJSON = JSON.parse(document.getElementById("menu_nav_DICT").innerHTML);
    sessionStorage.setItem("menu_nav",JSON.stringify(menu_navJSON));
  }
}

function menu_nav(button) {
  console.log(button);
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


function add_to_order(foodtype,foodnameID,foodname,foodprice){
  if (sessionStorage.length>0) {
    console.log("sessionStorage.length>0:", sessionStorage.length)
    add_next_item_to_order(foodtype,foodnameID,foodname,foodprice);
  }
  else {
    console.log("sessionStorage.length <1:", sessionStorage.length);
    console.log("What happens in reset menu that doesn't happen here?")
    var orderARRAY = [];
    //add_next_item_to_order(foodtype,foodnameID,foodname,foodprice);
    initializeOrders(foodtype,foodnameID,foodname,foodprice);
    /*
    if this works delete initializeOrders() function
    and look at deleting add_to_order() function

    */

  }

  /* Submit order
  Pass order to python
  Clear session storage
  Reset buttons and cart screen
  */

  /* Review Order button
  Allow login to save history
  */

  /*
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
  var itemID = a + '_' + b;
  var qty = 1;
  /* Commented out 9/16/19
  let tr = document.getElementById(itemID);
  let spantr = document.createElement("span");
  spantr.appendChild(tr);
  */
  var orderARRAY = [];
  var itemDICT = {foodtype:a,foodnameID:b,foodname:d,foodprice:c,qty:1};
  orderARRAY = [itemDICT];
  var orderSTR = JSON.stringify(orderARRAY);
  sessionStorage.setItem("order",orderSTR);
  restore_menu();
}

function add_next_item_to_order(a,b,d,c) {
  //(foodtype,foodnameID,foodname,foodprice)
  var itemID = a + '_' + b;
  if(sessionStorage.getItem("order")!=null) orderARRAY = jsonSTR_to_array(sessionStorage.getItem("order"));
  else var orderARRAY = [];
  if (document.getElementById(itemID).childNodes[1].value=="Add to Order") {
    var qty =1;
    itemDICT = {foodtype:a,foodnameID:b,foodname:d,foodprice:c,qty:qty};
    orderARRAY.push(itemDICT);
    console.log(orderARRAY);
    sessionStorage.setItem("order",JSON.stringify(orderARRAY));
    //Check for pizza
    if ((a == "regularpizza")||(a == "sicilianpizza")|| (a == "special"))
    {
      //Is a pizza
    }
    else {
      restore_menu();
      // let tr = document.createElement("tr");
      // //itemID=itemID+"_BTN"; RESUME HERE
      // qty_plus_minus_buttons(itemID,1,-1,tr);
      // console.log("Remove Add to Order Button")
      return;
    }
    //(td_id,qty,i,tr)
  }
  else {
    qty = parseInt(document.getElementById(itemID).childNodes[1].value) + 1
    var i;
    for (i = 0; i < orderARRAY.length; i++) {
      //console.log(orderARRAY[i])
      if ((orderARRAY[i]["foodtype"]==a)&&(orderARRAY[i]["foodnameID"]==b)) {
        orderARRAY[i]["qty"] = qty;
      }
    }
  }
  sessionStorage.setItem("order",JSON.stringify(orderARRAY));
  restore_menu();
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
  var itemID = a + '_' + b;
  document.getElementById(itemID+"_placeholder").style.display="none";
  document.getElementById(itemID+"_resetspan").style.display="none";
  document.getElementById(itemID).childNodes[1].classList.remove("btn-success");
  document.getElementById(itemID).childNodes[1].classList.add("btn-primary");
  document.getElementById(itemID).childNodes[1].value="Add to Order";
  sessionStorage.setItem("order",JSON.stringify(orderARRAY));
}

function cancel_order() {
  sessionStorage.clear();
  document.location.reload()
}

  /*TODOs
fix division for Subs in html
sepatate id for pastas and salads in html or make table display:hidden
check for sessionStorage.length and replace with if null
check html divisions for ids
in p3.js initial sessionStorage("menu_nav") if null
menu_navDICT = {"All": true,
                "everything else":false}
  */
