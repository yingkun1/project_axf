from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^home/$',views.home,name="home"),
    url(r'^market/(\d+)/$',views.market,name="market"),
    url(r'^cart/$',views.cart,name="cart"),
    url(r'^mine/$',views.mine,name="mine"),
    url(r'^login/$',views.login,name="login"),
    url(r'^register/$',views.register,name = "register"),
    url(r'^checkuserid/$',views.checkuserid,name="checkuserid"),
    url(r'^quit/$',views.quit,name="quit"),
    url(r'^checkcart/(\d+)/$',views.checkcart,name="checkcart"),
    url(r'^saveorder\$',views.saveorder,name="saveorder"),

]