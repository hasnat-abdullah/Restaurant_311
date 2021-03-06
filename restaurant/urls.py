from django.conf.urls import url
from restaurant import views
from django.urls import include, path
from django.contrib import admin

urlpatterns = [
    path('', views.index, name='index'),
    path('404/', views.error404, name='error404'),
    path('about/', views.about, name='about'),
    path('blog/', views.blog, name='blog'),
    path('blog/<int:id>', views.blog_single, name='blog_single'),
    path('checkout/', views.checkout, name='checkout'),
    path('coupon/', views.coupon, name='coupon'),
    path('cart/', views.cart, name='cart'),
    path('contact/', views.contact, name='contact'),
    path('gallary/', views.gallary, name='gallary'),
    path('menu/', views.menu, name='menu'),
    path('reservation/', views.reservation, name='reservation'),
    path('shop/', views.shop, name='shop'),
    path('shop/cat/<name>', views.shop_category, name='shop_category'),
    path('shop/<int:id>', views.shop_single, name='shop_single'),
    path('cart/<int:fid>', views.add_to_cart, name='add_to_cart'),
    path('cart/update_inc/<int:fid>', views.cart_Update_increase, name='cart_Update_increase'),
    path('cart/update_dec/<int:fid>', views.cart_Update_decrease, name='cart_Update_decrease'),
    path('cart/delete/<int:fid>', views.add_to_cart_Delete, name='add_to_cart_Delete'),
    path('login/', views.getlogin, name='login'),
    path('lostPassword/', views.lostpass, name='lostpass'),
    path('logout/', views.getlogout, name='logout'),
    path('signup/', views.getsignup, name='signup'),
    path('customerReg/', views.customerReg, name='customerReg'),
    path('customerReg/update', views.customerRegUpdate, name='customerRegUpdate'),
    path('place_order/', views.place_order, name='place_order'),

]