/*for the interactive menu*/

var stHome = "Home";
var stHomeDesc = "Overview of the web application, log in page";
var stInput = "Input";
var stInputDesc = "Submit your expense entries here";
var stView = "View";
var stViewDesc = "View the current list of expense here";
var stAbout = "About";
var stAboutDesc = "some information about the author";


function changeBGColor(inId,inColor="rgb(219,245,193)") {
	document.getElementById(inId).style.backgroundColor =  inColor;
}

function changeText(inId,inText){
	document.getElementById(inId).innerHTML = inText;
}

function onMenuHover(inText1,inText2,inColor="rgb(219,245,193)"){
	changeBGColor('banner',inColor);
	changeText('bannerTitle',inText1);
	changeText('bannerDesc',inText2);
}

function submitFunction(){
	var a = document.querySelector('input[name=price]').value;
	var b = document.querySelector('input[name=description]').value;
	var c = document.querySelector('select[name=currency]').value;
	var d = new Date();

	
	if(checkPrice(a) && checkDesc(b)){
		document.getElementById('outputLog1').style.color = "black";
		document.getElementById('outputLog1').innerHTML = "The following will be entered to the database once server side scripting is up";
		document.getElementById('outputLog2').innerHTML = c+" "+a+","+b+", at time "+getDate(d)+","+getTime(d);
	}
	else{
		document.getElementById('outputLog1').style.color = "red";
		document.getElementById('outputLog1').innerHTML = "Invalid input!!";
	}
}


//need to implement a string check for the price
//1.must contain only numbers
//2.must contain only 2 decimal places
function checkPrice(a){
	var result;
	if(isNaN(a) || (a.length==0)){
		return false;
	}
	
	if(a.indexOf('.') > 0){ //there is a valid decimal place
		return( (a.length-a.indexOf('.')) < 4);
	}
	
	return true;
}

function checkDesc(b){
	return(b.length > 0);
}


//obtained from stack overflow, get time and Date in MySQL format
Number.prototype.padLeft = function(base,chr){
    var  len = (String(base || 10).length - String(this).length)+1;
    return len > 0? new Array(len).join(chr || '0')+this : this;
}


function getDate(d){
	var dformat = [d.getFullYear(),(d.getMonth()+1).padLeft(),
               d.getDate().padLeft(), ].join('-');
              
	return dformat;
}

function getTime(d){
	var dformat = [d.getHours().padLeft(),
               d.getMinutes().padLeft(),
               d.getSeconds().padLeft()].join(':');
	return dformat;
}
