var c = 0;

window.onload = function(){
	elemento();
}

function elemento(){
	var elem = document.getElementsByTagName('img');
	for (var i = 0; i < elem.length; i++)
		elem[i].style.display = (c % elem.length) == i ? '':'none';
	c++;
	setTimeout('elemento()',1000);

}