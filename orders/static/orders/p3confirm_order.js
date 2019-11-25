document.getElementById("pagetitle").innerHTML = "Confirm Order"
console.log("in p3confirm_order");
if (sessionStorage.length<1) {
  alert("Nothing Ordered");
  window.history.go(-1);
}

function confirm_orderjs(OrderSTR){
  console.log("function confirm_orderjs");
  var orderARRAY = jsonSTR_to_array(sessionStorage.getItem("order"));
  // console.log (orderARRAY);
  orderJSON = JSON.stringify(orderARRAY);
  console.log(orderJSON);
  // confirm_order(orderJSON); //This doesn't work - try context or template variable
  // perhaps create string that contains this string and use as pick?
  // or put orderJSON in URL via POST
}

function checkoutjs(test){
  console.log("confirm_orderjs",test);
  var orderARRAY = jsonSTR_to_array(sessionStorage.getItem("order"));
  // console.log (orderARRAY);
  orderJSON = JSON.stringify(orderARRAY);
  console.log(orderJSON);
  // confirm_order(orderJSON); //This doesn't work - try context or template variable
  // perhaps create string that contains this string and use as pick?
  // or put orderJSON in URL via POST
}
//orderJSON = "test URL"

//orderJSON_test/order/checkout.html
var orderARRAY = jsonSTR_to_array(sessionStorage.getItem("order"));
var orderJSON = JSON.stringify(orderARRAY);
var actionVar="/"+orderJSON+"/orders/checkout.html" ;
//console.log(actionVar)

// from https://stackoverflow.com/questions/32217741/post-request-using-ajax-in-django
// $("retrieveOrder").submit(function() {
//       console.log("in ajax");
//    $.ajax({

//        data: orderJSON,
//         dataType: "json",
//         type: "POST",
//     });
// });
//from https://realpython.com/django-and-ajax-form-submissions this worked as far as it went
$('#post-form').on('submit', function(event){
    console.log("form submitted!")  // sanity check
    event.preventDefault();
    create_post();
});

//update from https://realpython.com/django-and-ajax-form-submissions/
function create_post() {
    console.log("create post is working!") // sanity check
    console.log($('#post-text').val())
    $.ajax({
        url : "create_post.html", // the endpoint
        type : "POST", // http method
        data : { the_post : $('#post-text').val() }, // data sent with the post request

        // handle a successful response
        success : function(json) {
            $('#post-text').val(''); // remove the value from the input
            console.log(json); // log the returned json to the console
            console.log("success"); // another sanity check
        },

        // handle a non-successful response
        error : function(xhr,errmsg,err) {
            $('#results').html("<div class='alert-box alert radius' data-alert>Oops! We have encountered an error: "+errmsg+
                " <a href='#' class='close'>&times;</a></div>"); // add the error to the dom
            //console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
            console.log(xhr.status );
        }
    });
};

// This results in p3confirm_order.js:37 GET http://127.0.0.1:8000/orders/checkout.html 500 (Internal Server Error)
// var xhttp = new XMLHttpRequest();
// var url = "/order/checkout.html";
// url = "/xhttp_test/checkout.html";
// url = "checkout.html"
// xhttp.open('GET', url, true);
// var data = "xhttp_test";
// console.log(url,data)
// xhttp.send(data);
// xhttp.onreadystatechange = (e) => {
//   //console.log(xhttp.responseText)
// }





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
