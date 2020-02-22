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

function json2xml() {
  //get order history
  // from https://tqdev.com/2017-converting-json-to-xml-in-javascript-and-php
    var json = document.getElementById("order_data").innerHTML
    console.log(json);
    json = json.replace(/[\n\r]+/g, '');
    //console.log(json);
    var a = JSON.parse(json)
    var c = document.createElement("root");
    var t = function (v) {
        return {}.toString.call(v).split(' ')[1].slice(0, -1).toLowerCase();
    };
    var f = function (f, c, a, s) {
        c.setAttribute("type", t(a));
        if (t(a) != "array" && t(a) != "object") {
            if (t(a) != "null") {
                c.appendChild(document.createTextNode(a));
            }
        } else {
            for (var k in a) {
                var v = a[k];
                if (k == "__type" && t(a) == "object") {
                    c.setAttribute("__type", v);
                } else {
                    if (t(v) == "object") {
                        var ch = c.appendChild(document.createElementNS(null, s ? "item" : k));
                        f(f, ch, v);
                    } else if (t(v) == "array") {
                        var ch = c.appendChild(document.createElementNS(null, s ? "item" : k));
                        f(f, ch, v, true);
                    } else {
                        var va = document.createElementNS(null, s ? "item" : k);
                        if (t(v) != "null") {
                            va.appendChild(document.createTextNode(v));
                        }
                        var ch = c.appendChild(va);
                        ch.setAttribute("type", t(v));
                    }
                }
            }
        }
    };
    f(f, c, a, t(a) == "array");
    console.log(c.outerHTML);
    return c.outerHTML;
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
