window.onload = paperLinks;
function paperLinks(){
    var links = document.getElementsByTagName("a");
        for (var i=0;i<links.length;i++){
           if(links[i].getAttribute("class")=="popUp"){
                links[i].onclick = function(){
                 popUp(this.getAttribute("href"));
                return false;
            }
     }
    } 
}
<!==把调用popUp函数的onclick事件添加到有关的链接中==>

function popUp(winURL){
    window.open(winURL,"popup","width=320,height=480");
}