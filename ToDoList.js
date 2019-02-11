var myNodeList = document.getElementsByTagName("LI");
var i;
for(i =0; i < myNodeList.length;i++){
    var span = document.createElement("SPAN");
    var text = document.createTextNode("\u00D7");
    span.className="close";
    span.appendChild(text);
    myNodeList[i].appendChild(span);
}

//hide current element after clicking on a close button
var close = document.getElementsByClassName("close");
var i;
for(i= 0;i <close.length;i++){
    close[i].onclick = function(){
        var div = this.parentElement;
        div.style.display="none";
    }
}

//add finished status to events
var list = document.querySelector('ul');
list.addEventListener('click',function(ev){
    if(ev.target.tagName==='LI'){
        ev.target.classList.toggle('finished');
    }
},false)


function addNewElement(){
    var li = document.createElement("li");
    var inputValue= document.createTextNode("list").value;
    var t = document.createTextNode(inputValue);
    li.appendChild(t);
    if(inputValue ===''){
        alert("Please write something! You can't add emty event.")
    }
    else{
        document.getElementById("myList").appendChild(li);
    }
    document.getElementById("list").value="";

    var span = document.createElement("SPAN");
    var text = document.createTextNode("\u00D7");
    span.className = "close";
    span.appendChild(text);
    li.appendChild(span);

    for(i =0 ;i < close.length;i++){
        close[i].onclick = function(){
            var div = this.parentElement;
            div.style.display="none";
        }
    }
}