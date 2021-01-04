from django.urls import path
from .views import *

urlpatterns = [
    # Home
    path('', HomeControl.index, name='home'),
    path('register-Login/', HomeControl.login_register, name='register_login'),
    path('product/', HomeControl.product, name='product'),
    path('categories/', HomeControl.category, name='categories'),
    path('categories/<int:id>', HomeControl.view_category, name='shows_categories'),
    path('detail/<int:id>', HomeControl.detail_product, name='detail_product'),
    path('logout/home', HomeControl.logout_view_home, name='logout_home'),
    path('home/contact', HomeControl.contact, name='contact'),
    path('home/search', HomeControl.search, name='search'),
    # Shopping cart
    path('add_to_cart/<int:id>', ShoppingCart.add_to_cart, name='add_to_cart'),
    path('add_cart/<int:id>', ShoppingCart.add_cart, name='add_cart'),
    path('update_cart/<int:id>', ShoppingCart.update_cart, name='update_cart'),
    path('delete_item_cart/<int:id>', ShoppingCart.del_item_cart, name='del_item_cart'),
    path('del_cart', ShoppingCart.del_cart, name='del_cart'),
    path('basket/', ShoppingCart.view_basket, name='basket'),
    # check out
    path('checkout/', CheckOut.checkout, name='checkout'),
    path('order_successful/', CheckOut.order, name='order_successful'),

    # customer
    path('customer/account/', Customer.customer_account, name='account'),
    path('customer/account-orders/', Customer.order_account, name='acc_orders'),
    path('customer/account-order/<int:id>', Customer.view_order, name='acc_order'),
    path('customer/account-order/cancel/<int:id>', Customer.cancel_order, name='acc_cancel_order'),
    path('customer/wish/<int:id>', Customer.add_wish_list, name='wish'),
    path('customer/wish_list/', Customer.view_wish_list, name='wish_list'),
    path('customer/wish_list/remove/<int:id>', Customer.remove_wish, name='remove_wish'),

]
