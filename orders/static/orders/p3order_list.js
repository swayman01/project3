document.getElementById("pagetitle").innerHTML = "Order Placed"
console.log('In p3order_list.js')
function order_historyJS() {
  show_order_history = true;
  console.log("order_historyJS/show_order_history:",show_order_history);
  document.location.reload();

}
function filter_by_dateJS() {
  console.log("filter_by_dateJS")
}
function export_csvJS() {
  console.log("export_csvJS")
}
sessionStorage.clear();
