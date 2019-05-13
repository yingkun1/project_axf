$(document).ready(function(){
//修改购物车
  var addShoppings = document.getElemetnsByClassName("addShoppings")
  var subShoppings = document.getElemetnsByClassName("subShoppings")

   //为点击加号添加事件
  for (var i=0;i<addShoppings.length;i++)
  {
    addShopping = addShoppings[i]
    addShopping.addEventListener("click",function(){
        //发起ajax，修改购物车
        pid = this.getAttribute("ga")
        $.post("/changecart/0/",{"productid":pid},function(data){
            if(data.status=="success")
            {
                //添加成功，把中间的span的innerHTML变成当前的数量
                document.getElemetnsById(pid).innerHTML = data.data
                document.getElemetnsById(pid+"price").innerHTML = data.price
                if (data.data==0)
                {
//                    window.location.href = "http://127.0.0.1:8001/cart/"
                    var li = document.getElemetnsById(pid+"li")
                    li.parentNode.removeChild(li)
                }
            }
        })


    })
  }

   //为点击减号添加事件
  for (var i=0;i<subShoppings.length;i++)
  {
    subShopping = subShoppings[i]
    subShopping.addEventListener("click",function(){
        //发起ajax，修改购物车
        pid = this.getAttribute("ga")
        $.post("/changecart/1/",{"productid":pid},function(data){
            if(data.status=="success")
            {
                //添加成功，把中间的span的innerHTML变成当前的数量
                document.getElemetnsById(pid).innerHTML = data.data
                document.getElemetnsById(pid+"price").innerHTML = data.price
            }
        })


    })
  }

  var ischoses = document.getElemetnsByClassName("ischose")
  for (j=0;j<ischoses.length;j++)
  {
    ischose = ischoses[j]
    ischose.addEventListener("click",function(){
        pid = this.getAttribute("goodsid")
        $.post("/changecart/2/",{"productid":pid},function(data){
            if(data.status=="success")
            {
//                window.location.href = "http://127.0.0.1:8001/cart/"
                var s =document.getElemetnsById(pid+"a")
                s.innerHTML = data.data
            }
        })
    },false)
  }

  var ok = document.getElemetnsById("ok")
  ok.addEventListener("click",function(){
    var f = confirm("是否确认下单？")
    if (f)
    {
        $.post("/saveorder/",function(data){
            if (data.status=="success")
            {
                window.location.href = "http://127.0.0.1:8001/cart/"
            }
        })
    }
  },false)
})