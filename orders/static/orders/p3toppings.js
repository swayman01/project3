document.addEventListener('DOMContentLoaded', () => {
  set_labels(pizzatype,foodname)
});

var qtysmallpizza=0;
var qtylargepizza=0;
var add_to_order_flag=false
document.getElementById("extra_cheese_frame").style.display="none"
document.getElementById("extra_cheese_table").style.display="none"

function toggleselecttopping(toppingID,numtoppings){
  if (document.getElementById(toppingID).childNodes[1].value=="Select") {
    if (document.getElementById(toppingID).childNodes[1].classList.contains("disabled")==false) {
      document.getElementById(toppingID).childNodes[1].value="Deselect"
      document.getElementById(toppingID).childNodes[1].classList.add('btn-info')
      document.getElementById(toppingID).childNodes[1].classList.remove('btn-default')
    }
  }
  else {
    document.getElementById(toppingID).childNodes[1].value="Select"
    document.getElementById(toppingID).childNodes[1].classList.add('btn-default')
    document.getElementById(toppingID).childNodes[1].classList.remove('btn-info')
    document.getElementById(toppingID).childNodes[1].classList.remove('disabled')
  }
  // Count selected toppings and compare
  selectedtoppingcount = countselectedtoppings();
  if (selectedtoppingcount==numtoppings) {
    document.getElementById("add_to_order").classList.remove('disabled')
    document.getElementById("add_to_order").classList.remove('btn-default')
    document.getElementById("add_to_order").classList.add('btn-primary')
    add_to_order_flag=true
  }
  //when limit is reached don't allow more
  var toppingLIST = document.getElementsByClassName("selectbutton");
  if (selectedtoppingcount>numtoppings) {
    alert("You have exceeded your topping limit. Either deselect a topping or proceed with the order");
    var i;
    for (i = 0; i < toppingLIST.length; i++) {
      if (toppingLIST[i].value=="Select") {
        toppingLIST[i].classList.add("disabled");
      }
    }
    document.getElementById("add_to_order").classList.add('disabled')
    document.getElementById("add_to_order").classList.remove('btn-primary')
    document.getElementById("add_to_order").classList.add('btn-default')
    return
  }
  if ((selectedtoppingcount<numtoppings)&&(add_to_order_flag)
  &&(!(document.getElementById("add_to_order").classList.contains('disabled')))){
    //when if deselect reduces the number of toppings deselect
    document.getElementById("add_to_order").classList.add('disabled')
    document.getElementById("add_to_order").classList.remove('btn-primary')
    document.getElementById("add_to_order").classList.add('btn-default')
    for (i = 0; i < toppingLIST.length; i++) {
      toppingLIST[i].classList.remove("disabled");
    }
    add_to_order_flag=false;
    return
  }
}

function countselectedtoppings() {
  //select top node
  let selectedtoppingcount = 0;
  let toppingLIST = document.getElementsByClassName("selectbutton");
  //loop through childNodes and count
  var i;
  for (i = 0; i < toppingLIST.length; i++) {
    if (toppingLIST[i].value=="Deselect") {
      selectedtoppingcount++;
    }
  }
  return selectedtoppingcount;
}

function set_labels(pizzatype, foodname) {
  if(pizzatype==6) {
    pizzatypeSTR = foodname + " Sub";
    document.getElementsByClassName('smallitem')[0].innerText="Small " + pizzatypeSTR + "s";
    document.getElementsByClassName('largeitem')[0].innerText="Large " + pizzatypeSTR + "s";
    if (foodname.includes("Extra Cheese")) {
      extra_cheese();
    }
  }
  if(pizzatype==4) {
    pizzatypeSTR = foodname + " Platter";
    document.getElementsByClassName('smallitem')[0].innerText="Small " + pizzatypeSTR + "s";
    document.getElementsByClassName('largeitem')[0].innerText="Large " + pizzatypeSTR + "s";
  }
}

function add_pizza(pizzaID,pizzatype,numtoppings,smallprice,largeprice) {
  var pizzaARRAY = ["regularpizza", "sicilianpizza", "special","special","dinnerplatter","5","sub"];
  pizzaID = arguments[0];
  pizzatype = arguments[1];
  numtoppings = arguments[2];
  smallprice = arguments[3];
  largeprice = arguments[4];
  foodtype =  pizzaARRAY[pizzatype];
  //check for qtylargepizza or qtysmallpizza >0
  qtysmallpizza = parseInt(document.getElementById("qtysmallpizza").value);
  qtylargepizza = parseInt(document.getElementById("qtylargepizza").value);
  if((qtysmallpizza>0)||(qtylargepizza>0)) {}
  else {
    alert("Select the number of small and/or large pizzas with these toppings");
    return
  }

  var toppingLIST = document.getElementsByClassName("selectbutton");
  var pizzatypeSTR = null;
  //gather info here
  if(parseInt(pizzatype)==0) {
    pizzatypeSTR = "Regular Pizza";
  }
  if(pizzatype==1) {
    pizzatypeSTR = "Sicilian Pizza";
  }
  if(pizzatype==2) {
    pizzatypeSTR = "Special Regular Pizza";
  }
  if(pizzatype==3) {
    pizzatypeSTR = "Special Sicilian Pizza";
  }
  if(pizzatype==4) {
    pizzatypeSTR = foodname + " Dinner Platter";
  }
  if(pizzatype==6) {
    pizzatypeSTR = foodname + " Sub";
  }
  //extract toppings
  var toppings = []
  var toppingLIST = document.getElementsByClassName("selectbutton");
  var i;
  for (i = 0; i < toppingLIST.length; i++) {
    if (toppingLIST[i].value=="Deselect") {
      toppings.push(toppingLIST[i].parentElement.parentElement.parentElement.childNodes[3].innerText);
    }
  }

  if (qtysmallpizza>0){
    if(pizzatype<=1) {
      itemDICT = {"foodtype":foodtype,"foodprice":smallprice,"qty":qtysmallpizza,
      "toppings":toppings,"foodnameID":pizzaID,"foodname":"Small "+pizzatypeSTR+" with "+toppings};
    }
    if((pizzatype==2)||(pizzatype==3)) {
      itemDICT = {"foodtype":foodtype,"foodprice":smallprice,"qty":qtysmallpizza,
      "toppings":toppings,"foodnameID":pizzaID,"foodname":"Small "+pizzatypeSTR + ": " + foodname};
    }
    if(pizzatype>=4) {
      itemDICT = {"foodtype":foodtype,"foodnameID":pizzaID,"foodprice":smallprice,"qty":qtysmallpizza,
      "foodname":"Small "+pizzatypeSTR,"display_order":display_order};
    }
    add_pizza_to_order(itemDICT);
  }

  if (qtylargepizza>0){
    if(pizzatype<=1) {
      itemDICT = {"foodtype":foodtype,"foodprice":largeprice,"qty":qtylargepizza,
      "toppings":toppings,"foodnameID":pizzaID,"foodname":"Large "+pizzatypeSTR+" with "+toppings};
    }
    if((pizzatype==2)||(pizzatype==3)) {
      itemDICT = {"foodtype":foodtype,"foodprice":largeprice,"qty":qtylargepizza,
      "toppings":toppings,"foodnameID":pizzaID,"foodname":"Large "+pizzatypeSTR + ": " + foodname};
    }
    if(pizzatype>=4) {
      itemDICT = {"foodtype":foodtype,"foodnameID":pizzaID,"foodprice":largeprice,"qty":qtylargepizza,
      "foodname":"Large "+pizzatypeSTR,"display_order":display_order};
    }
    add_pizza_to_order(itemDICT);
  }
}

function initializeOrderWithPizza(pizzaID){
  sessionStorage.clear();
  var orderARRAY = [];
  console.log("SOMEDAY: Complete this section as below or Delete")
}

function add_pizza_to_order(itemDICT) {
  if((sessionStorage.getItem("order")==null)||(sessionStorage.getItem("order").length<3)) {
    var orderARRAY = [];
    orderARRAY = [itemDICT];
    let orderSTR = JSON.stringify(orderARRAY);
    sessionStorage.setItem("order",orderSTR);
    gohome();
  }
  else {
    orderARRAY = jsonSTR_to_array(sessionStorage.getItem("order"));
    orderARRAY.push(itemDICT);
    sessionStorage.setItem("order",JSON.stringify(orderARRAY));
    gohome();
  }
}

$('.qty').click(function() {
  var $t = $(this),
  $in = $('input[name="' + $t.data('field') + '"]'),
  val = parseInt($in.val()),
  valMax = 9,
  valMin = 0;

  // Check if a number is in the field first
  if (isNaN(val) || val < valMin) {
    // If field value is NOT a number, or
    // if field value is less than minimum,
    // ...set value to 0 and exit function
    $in.val(valMin);
    return false;
  }
  else if (val > valMax) {
    // If field value exceeds maximum,
    // ...set value to max
    $in.val(valMax);
    return false;
  }
  // Perform increment or decrement logic
  if ($t.data('func') == 'plus') {
    if (val < valMax) $in.val(val + 1);
  }
  else {
    if (val > valMin) $in.val(val - 1);
  }
  if ($t.data("field")=="field1") {
    qtysmallpizza = parseInt($in.val());
    if (qtysmallpizza > 0) {
      document.getElementById("qtysmallpizza").classList.add('btn-info')
      document.getElementById("qtysmallpizza").classList.remove('btn-default')
    }
    else {
      document.getElementById("qtysmallpizza").classList.add('btn-default')
      document.getElementById("qtysmallpizza").classList.remove('btn-info')
    }
  }
  if ($t.data("field")=="field2") {
    qtylargepizza = parseInt($in.val());
    if (qtylargepizza > 0) {
      document.getElementById("qtylargepizza").classList.add('btn-info')
      document.getElementById("qtylargepizza").classList.remove('btn-default')
    }
    else {
      document.getElementById("qtylargepizza").classList.add('btn-default')
      document.getElementById("qtylargepizza").classList.remove('btn-info')
    }
  }
});

function extra_cheese() {
  //This function brings up the extra cheese menu
  if((sessionStorage.getItem("order")==null)||(sessionStorage.getItem("order").length<3)) {
    alert("No Subs to add Extra Cheese");
    gohome();
  }
  else {
    orderARRAY = jsonSTR_to_array(sessionStorage.getItem("order"));
  }
  subct=0;
  extra_cheese_candidates=[];
  for (i = 0; i < orderARRAY.length; i++) {
    if (orderARRAY[i].foodtype=="sub") {
      subct = subct+1;
      extra_cheese_candidates.push(orderARRAY[i])
    }
  }
  if (subct==0) {
    alert("No Subs to add Extra Cheese");
    gohome();
  }
  console.log(extra_cheese_candidates);
  document.getElementById("pizzabuttons").style.display="none";
  document.getElementById("menu_control").style.display="none";
  document.getElementById("pagetitle").innerText="Extra Cheese?";
  let extra_cheese_start = document.getElementById("extra_cheese_menu");
  let items_with_extra_cheese = 0;
  for (i = 0; i < extra_cheese_candidates.length; i++) {
    if(extra_cheese_candidates[i].foodname.includes("with extra cheese")) {
      items_with_extra_cheese = items_with_extra_cheese + 1;
      if(items_with_extra_cheese==extra_cheese_candidates.length) {
        alert("All items eligible for extra cheese have extra cheese");
        gohome()
      }
    }
    if(!extra_cheese_candidates[i].foodname.includes("with extra cheese")) {
      let tr = document.createElement("tr");
      tr.setAttribute("class","extra_cheese");
      let item_name = document.createTextNode(extra_cheese_candidates[i].foodname);
      let tdname = document.createElement("td");
      tdname.appendChild(item_name);
      tr.appendChild(tdname);
      let tdname2 = document.createElement("td");
      tdname2.appendChild(document.createTextNode("Extra Cheese"));
      tdname2.setAttribute("onclick","add_cheese("+i+")");
      tdname2.setAttribute("class","btn btn-primary")
      tr.appendChild(tdname2);
      tr.setAttribute("id","extra_cheese_"+i);
      extra_cheese_start.appendChild(tr)
    }
  }
  document.getElementById("extra_cheese_frame").style.display="block"
  document.getElementById("extra_cheese_table").style.display="block"
  document.getElementById("extra_cheese_form").style.display="block"
}

function add_cheese(sub_index) {
  let subct=-1;
  orderARRAY = jsonSTR_to_array(sessionStorage.getItem("order"));
  for (i = 0; i < orderARRAY.length; i++) {
    //if (orderARRAY[i].foodtype=="sub") {
    if (orderARRAY[i].foodtype=="sub") {
      subct = subct+1;
      if(subct==sub_index) {
        current_sub = orderARRAY[i];
        order_INDEX = i;
      }
    }
  }
  //Toggle button
  extra_cheese_btn = document.getElementById("extra_cheese_"+String(sub_index)).childNodes[1]
  extra_cheese_btn.innerText = "Extra Cheese Added"
  extra_cheese_btn.classList.add('btn-info')
  extra_cheese_btn.classList.remove('btn-primary')
  console.log(current_sub);
  extra_cheese_smallprice = parseFloat(extra_cheese_smallprice)
  extra_cheese_largeprice = parseFloat(extra_cheese_largeprice)
  if (orderARRAY[order_INDEX].foodname.startsWith("Small")) {
    orderARRAY[order_INDEX].foodprice = orderARRAY[order_INDEX].foodprice + extra_cheese_smallprice
  }
  if (orderARRAY[order_INDEX].foodname.startsWith("Large")) {
    orderARRAY[order_INDEX].foodprice = orderARRAY[order_INDEX].foodprice + extra_cheese_largeprice
  }
  orderARRAY[order_INDEX].foodname = orderARRAY[order_INDEX].foodname + " with extra cheese";
  sessionStorage.setItem("order",JSON.stringify(orderARRAY));
}
