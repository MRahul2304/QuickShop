from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home', views.home, name = "home"),
    path('cart', views.cart_page, name = "cart"),
    path('login', views.login_page, name = "login"),
    path('addcart', views.add_cart, name = "addcart"),
    path('logout', views.logout_page, name = "logout"),
    path('register', views.register, name = "register"),
    path('favourite', views.favourite, name = "favourite"),
    path('collections', views.collections, name = "collections"),
    path('favourite_view', views.favourite_view, name = "favourite_view"),
    path('collections/<str:name>', views.collectionsview, name = "collections"),
    path('collections/<str:cname>/<str:pname>', views.product_details, name = "product_details"),
    path('remove_cart_product/<str:cid>', views.remove_cart_product, name = "remove_cart_product"),
    path('remove_favourite_product/<str:fid>', views.remove_favourite_product, name = "remove_favourite_product"),
]
