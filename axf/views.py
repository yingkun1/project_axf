from django.shortcuts import render, redirect

from .models import Wheel,Nav,Mustbuy,Shop,FoodTypes,Goods,User,Cart,Order
# Create your views here.

def home(request):
    wheelList = Wheel.objects.all()
    navList = Nav.object.all()
    mustbuyList = Mustbuy.object.all()
    shopList = Shop.objects.all()
    shop1 = shopList[0]
    shop2 = shopList[1:3]
    shop3 = shopList[3:7]
    shop4 = shopList[7:11]
    return render(request,'axf/home.html',{"title":"主页","wheelList":wheelList,"navList":navList,"mustbuyList":mustbuyList,"shop1":shop1,"shop2":shop2,"shop3":shop3,"shop4":shop4})

def market(request,categoryid):
    leftList = FoodTypes.objects.all()
    productList = Goods.objects.filter(categoryid=categoryid)
    childNameList = []
    childnames = group.childtypenames
    arr1 = childnames.split("#")
    if sortid ==1:
        pass
    elif sortid ==2:
        pass
    elif sortid ==3:
        pass

    cartList = []
    token = request.session.get("token")
    if token:
        user = User.objects.get(userToken = token)
        cartlist = Cart.objects.filter(userAccount = user.userAccount)
    cartlistnum = len(cartlistnum)
    print("*******************cartlistnum=",cartlistnum)
    for p in productList:
        for c in cartlist:
            if c.productid == p.productid:
                p.num = c.productnum

    return render(request,'axf/market.html',{"title":"闪送超市","leftList":leftList,"productList":productList})


def cart(request):
    cartlist = []
    # 判断用户是否登录
    token = request.session.get("token")
    if token != None:
        user = User.objects.get(userToken=token)
        cartlist = Cart.objects.filter(userAccount=user.userAccount) #拿出当前用户的所有购物数据
    return render(request,'axf/cart.html',{"title":"购物车","cartlist":cartlist})

#修改购物车
def checkcart(request,flag):
    #判断用户是否登录
    token = request.session.get("token")
    print("token=",token)
    if token == None:
        #没登录
        # print("*************dasdasd")
        # return redirect('/login/')
        return JsonResponse({"data":-1,"status":"error"}) #js会接收这个json

    productid = request.POST.get("productid")
    product = Goods.objects.get(productid=productid)
    user = User.objects.get(userToken = token)

    if flag == '0':
        #判断该商品是否还有库存
        if product.storenums == 0:
            return JsonResponse({"data":-2,"status":"error"})
        #尝试从模型中取出数据，可能有，也可能没有
        carts = Cart.objects.filter(userAccount = user.userAccount)
        c = None
        if catrs.count()==0:
            #直接增加一条订单
            c = Cart.createcart(user.userAccount,productid,1,product.price,True,product.productimg,product.productlongname,False)
            c.save()

        else:
            try:
                c = carts.get(productid == productid)
                c.productnum += 1
                c.productprice = "%.2f" % (float(product.price)*c.productnum)
                c.save()
            except: Cart.DoesNotExist as e:
                #直接增加一条订单
            c = Cart.createcart(user.userAccount, productid, 1, product.price, True, product.productimg,product.productlongname, False)
            c.save()
    #库存减一：
    product.storenums-=1
    product.save()
    return JsonResponse({"data":c.productnum,"price":c.productprice""status":"success"})

    # elif flag=='1':
    #     return JsonResponse({"data": -2, "status": "error"})
    #     # 尝试从模型中取出数据，可能有，也可能没有
    #     carts = Cart.objects.filter(userAccount=user.userAccount)
        c = None
        if catrs.count() == 0:
            # 直接返回，无需多余的操作
            return JsonResponse({"data":-2,"status":"error"})

        else:
            try:
                c = carts.get(productid == productid)
                c.productnum -= 1
                c.productprice = "%.2f" % (float(product.price) * c.productnum)
                if c.productnum == 0:
                    c.delete()
                else:
                    c.save()
            except:
                Cart.DoesNotExist as e:
                # 直接返回，无需多余操作
                return JsonResponse({"data": -2, "status": "error"})


        # 库存加一：
        product.storenums += 1
        product.save()
        return JsonResponse({"data": c.productnum,"price":c.productprice "status": "success"})

    elif flag==2:
        carts = Cart.objects.filter(userAccount=user.userAccount)
        c = carts.get(productid == productid)
        c.isChose = not c.isChose
        str = ""
        if c.isChose:
            str="√"
        c.save()
        # return JsonResponse({"data":str,"status":"success"})

def saveorder(request):
    # 判断用户是否登录
    token = request.session.get("token")
    if token == None:
        return JsonResponse({"data": -1, "status": "error"})  # js会接收这个json
    user = User.objects.get(userToken=token)
    carts = Cart.objects.filter(isChose = True)
    if carts.count() == 0:
        return JsonResponse({"data":-1,"status":"error"})

    oid = time.time() + random.randrange(1,10000)
    oid = "%d" % oid
    o = Order.createorder(oid,user.userAccount,0)
    o.save()
    for item in carts:
        item.isDelete = True
        item.orderid = oid
        item.save()
    return JsonResponse({"status":"success"})



def mine(request):
    username = request.session.get("username","未登陆")

    return render(request,'axf/mine.html',{"title":"我的","username":username})

#登陆
from .forms.login import LoginForm
from django.http import HttpResponse
def login(request):
    if request.method == "POST":
        f = LoginForm(request.POST)
        if f.is_valid():
            #信息格式没有问题的话，验证账号和密码的正确性
            print("*************")
            name =f.cleaned_data["username"]
            pswd = f.cleaned_data["passwd"]
            try:
                user = User.objects.get("")
                if user.userPasswd != pwsd:
                    return redirect('/login/')
            except:User.DoesNotExist as e:
                return redirect('/login/')

            #登陆成功
            token = time.time() + random.randrange(1, 100000)
            user.userToken = str(token)
            user.save()
            request.session['username'] = user.userName
            request.session['token'] = user.userToken

            # print("name=",name)
            # print("password=",pswd)

            return redirect('/mine/')
        else:
            return render(request, 'axf/login.html', {"title": "登陆", "form": f,"errors":f.errors})
    else:
        f = LoginForm()
        return render(request,'axf/login.html',{"title":"登陆","form":f})


#注册界面
import time
import random
import os
from django.conf import settings
def register(request):
    if request.method = "POST":
        userAccount = request.POST.get("userAccount")
        userPasswd = request.POST.get("userPasswd")
        userName = request.POST.get("userName")
        userPhone = request.POST.get("userPhone")
        userAddress = request.POST.get("userAddress")
        userRank = 0
        token = time.time()+random.randrange(1,100000)
        userToken = str(token)

        f = request.FILES["userImg"]
        userImg = os.path.join(settings.MEDIA_ROOT,userAccount+".png")
        with open(userImg,'wb') as fp:
            for data in f.chunks():
                fp.write(data)

        user = User.createuser(userAccount,userPasswd,userName,userPhone,userAddress,userImg,userRank,userToken)
        user.save()
        request.session['username'] = userName
        request.session['token'] = userToken

        return redirect('/mine/')

    else:
        return render(request,'axf/register.html',{"title":"注册"})

from django.http import JsonResponse
#验证账号是否被注册过
def checkuserid(request):
    userid = request.POST.get("userid")
    return render(request,'axf/checkuserid.html')
    # try:
    #     user = User.objects.get(userAccount = userid)
    #     return JsonResponse({data:"该用户已经被注册"，status:"error"})
    # except User.DoesNotExist as e:
    #     return JsonResponse({data:"可以注册",status:"success"})

#退出登陆
from django.contrib.auth import logout
def quit(request):
    logout(request)
    return redirect('/mine')


