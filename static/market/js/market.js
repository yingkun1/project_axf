$(document).ready(function(){
    var alltypebtn = docunment.getElementById("alltypebtn")
    var showsortbtn = docunment.getElementById("showsortbtn")

    var typediv = document.getElementById("typediv")
    var sortdiv = document.getElementById("sortdiv")

    typediv.style.display = "none"
    sortdiv.style.display = "none"

    alltypebtn.addEventListener("click",function(){
        typediv.style.display = "block"
        sortdiv.style.display = "none"
    },false)

    showsortbtn.addEventListener("click",function(){
        typediv.style.display = "none"
        sortdiv.style.display = "block"
    },false)

    alltypebtn.addEventListener("click",function(){
        typediv.style.display = "none"
    },false)

    showsortbtn.addEventListener("click",function(){
        sortdiv.style.display = "none"
    },false)

})
