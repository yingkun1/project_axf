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
            }
            else
            {
                if(data.data==-1)
                {
//                    console.log("**************")
//                    $.get('/login/')
                    window.location.href="http://127.0.0.1:8001/login/"
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
            }
            else
            {
                if(data.data==-1)
                {
//                    console.log("**************")
//                    $.get('/login/')
                    window.location.href="http://127.0.0.1:8001/login/"
                }
            }
        })


    })
  }

