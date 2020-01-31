document.getElementById("pagetitle").innerHTML = "Orders Placed";
document.addEventListener('DOMContentLoaded', () => {
  my_ratingsJSONSTR = document.getElementById("my_ratingsJSONSTR").innerHTML
  if (my_ratingsJSONSTR.length>2) {
    my_ratingsARRAY = jsonSTR_to_array(my_ratingsJSONSTR);
    update_rating_buttons();
  }
});

function order_historyJS() {
  show_order_history = true;
  document.location.reload();

}
function filter_by_dateJS() {
  console.log("TODO filter_by_dateJS")
}

function export_csvJS() {
  console.log("TODO export_csvJS")
}

function update_rating_buttons() {
  var orderLIST = document.getElementsByClassName("orderitem");
  for (i = 1; i < orderLIST.length; i++) { //skip heading row
    for (j = 0; j < my_ratingsARRAY.length; j++) {
      if (orderLIST[i].children[1].innerHTML == my_ratingsARRAY[j]["foodname"]) {
        if (my_ratingsARRAY[j]["customer_rating"]==1) {
          orderLIST[i].children[4].children[0].children[0].innerHTML="<p>&#128077</p>"
          orderLIST[i].children[4].children[0].children[0].innerHTML="&#128077"
          orderLIST[i].children[4].children[0].children[0].setAttribute("class","btn btn-default btn-lg")
        }
        if (my_ratingsARRAY[j]["customer_rating"]==-1) {
          orderLIST[i].children[4].children[0].children[0].innerHTML="<p>&#128078</p>"
          orderLIST[i].children[4].children[0].children[0].innerHTML="&#128078"
          orderLIST[i].children[4].children[0].children[0].setAttribute("class","btn btn-default btn-lg")
        }
        if (my_ratingsARRAY[j]["customer_rating"]==0) {
          orderLIST[i].children[4].children[0].children[0].innerHTML="No Opinion"
          orderLIST[i].children[4].children[0].children[0].setAttribute("class","btn btn-default btn-sm")
        }
      }
    }
  }
}



sessionStorage.clear();
