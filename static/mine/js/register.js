//通过这个js来检测该账号是否已经被注册过了
$(document).ready(function(){
    var account = document.getElementById("account")
    var accounter = document.getElementById("accounter")
    var checkerr = document.getElementById("checkerr")
    var pass = document.getElementById("pass")
    var passerr = document.getElementById("passerr")
    var passwd = document.getElementById("passwd")
    var passwderr = document.getElementById("passwderr")

    //为账号添加聚焦事件
    account.addEventListener("focus",function(){
        accounter.style.display = "none"
        checkerr.style.display = "none"
    },false)

    accoun.addEventListener("blur",function(){
        instr = this.value
        if (instr.length<6||instr.length>12)
        {
            accounter.style.display="block"
            return
        }

        $.post("/checkuserid/",{"userid":instr},function(data){
            if (data.status=="error"){
                checkerr.style.display="block"
            }
        })
    },false)

    //为密码添加聚焦事件
    pass.addEventListener("focus",function(){
        passerr.style.display = "none"
    },false)

    pass.addEventListener("blur",function(){
        instr = this.value
        if (instr.length<6||instr.length>12)
        {
            passerr.style.display="block"
            return
        }
    },false)

    //为验证密码添加聚焦
    passwd.addEventListener("focus",function(){
        passwderr.style.display = "none"
    },false)

    passwd.addEventListener("blur",function(){
        instr = this.value
        if(instr != pass.value){
            passwderr.style.display="block"
        }
    },false)
})