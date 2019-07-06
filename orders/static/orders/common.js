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
  for (i=0;i<jsonLIST.length-1;i++){
    jsonLIST[i] = jsonLIST[i].concat("}");
  }
  for (i=0;i<jsonLIST.length;i++){
    jsonLIST[i] = JSON.parse(jsonLIST[i]);
  }
  return jsonLIST;
}
