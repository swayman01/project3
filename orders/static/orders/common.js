// File of common functions for project3
function timestamp(){
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
    //console.log(jsonLIST[i])
  }
  return jsonLIST;
}

function qty_plus_minus(td_index,j) {
  //This function increments quantities when clicking on the plus or minus keys
  // j of 1 signifies +, j of -1 signifies -
  let
  valMax = 9,
  valMin = 0;
  let td_prefix = "order+"; //Until I can pass multiple arguments,this is the best choice for DRY code
  let td_id = td_prefix+td_index;
  let val = document.getElementById(td_id).childNodes[1].value;

  // Check if a number is in the field first
  if (isNaN(val) || val < valMin) {
    // If field value is NOT a number, or
    // if field value is less than minimum,
    // ...set value to 0 and exit function
    document.getElementById(td_id).childNodes[1].value=parseInt(valMin)
    //return false;
  }
  else if (val > valMax) {
    // If field value exceeds maximum,
    // ...set value to max
    document.getElementById(td_id).childNodes[1].value=parseInt(valMax);
    //return false;
  }

  // Perform increment or decrement logic
  //let t = document.getElementById(td_id);
  if (document.getElementById(td_id).childNodes[0].dataset["func"] == 'plus') {
    if (j==1) {
      if (val < valMax) document.getElementById(td_id).childNodes[1].value=parseInt(val)+1;
      else document.getElementById(td_id).childNodes[1].value=parseInt(valMax);
    }



  else {
    if (val > valMin) document.getElementById(td_id).childNodes[1].value=parseInt(val)-1;
    else document.getElementById(td_id).childNodes[1].value=parseInt(valMin);
  }
}
}

$('.qty').click(function() {
  console.log("fix login for review order page");
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
    console.log("129 in anonymous plus");
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
