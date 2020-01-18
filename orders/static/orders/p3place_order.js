document.addEventListener('DOMContentLoaded', () => {
  document.getElementById("pagetitle").innerHTML = "Place Your Order"
});

console.log("in p3place_order");
if (sessionStorage.length<1) {
  alert("Nothing Ordered");
  window.history.go(-1);
}

var orderARRAY = jsonSTR_to_array(sessionStorage.getItem("order"));
orderJSON = JSON.stringify(orderARRAY);
console.log(orderARRAY,"\n",orderJSON)
document.getElementById('orderdataJSON').innerText=orderJSON
console.log(orderJSON)

// Commented out 12/30/19
// $('.workaround').click(function(){
//     $.ajax(
//       {
//         type:"GET",
//         url: "orders/checkout/", //Not found
//         //url: "orders/confirm_order/", //Not found
//         //url: "orders/retrieve_order/",  //this works
//         data:{
//           orderdata: orderJSON,
//         },
//         success: function( data )
//         {
//           alert(data);
//           alert("line 53 in p3place_order.js")
//         }
//       })
//     });
// $('.retrieve_order').click(function(){
//       $.ajax(
//         {
//           type:"GET",
//           url: "orders/retrieve_order/",
//           //url: "orders/place_order",
//           data:{
//             //orderdata: "test_dataSTRing", //this passed value in quotes
//             orderdata: orderJSON,
//           },
//           //success: function( data )
//           success: function()
//           {
//             document.getElementById("testajax").innerHTML = "Order Placed!"
//             document.getElementById("GoToOrderList").style.display="inline"
//             document.getElementById("LoginOrGuest").style.display="none"
//             //TODO sessionStorage.clear()
//             //TODO: if guest, logout, otherwise button to review history and rate previous orders
//             $.ajax(
//               {
//                 type:"GET",
//                 //url: "/", //result is correct GET, but no action
//                 url: "orders/review_order.html/" //result is always not found
//                 // data:{
//                 //   orderdata: "success callback",
//                 // }
//               })
//             }
//           });
//         });
// //end like button copy
//
// $('#ajax_on_click').click(function(){
//     console.log("ajax on click");
//     $.ajax(
//       {
//         type:"get",
//         url: "place_order.html",
//         data:{
//           "orderSTR":orderJSON
//         },
//         //dataType: "json",  //get data instead of html
//         success: function(data){
//           console.log("GET Success");
//           console.log(data['orderSTR']);
//           alert(data.orderSTR)
//           alert(orderJSON)
//           alert(data);
//         },
//         error: function(xhr,errmsg,err) {
//           console.log("TODO: Add failure data",err);
//           alert(orderJSON)
//           alert(data)
//         }
//       })
//     });
//
//     // From https://www.w3schools.com/jquery/tryit.asp?filename=tryjquery_ajax_get
//     $(document).ready(function(){
//       $("button").click(function(){
//         $.getJSON("place_order.html", function(data, status){
//           alert("Data: " + data + "\nStatus: " + status);
//         });
//       });
//     });
