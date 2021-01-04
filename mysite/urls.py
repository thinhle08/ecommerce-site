"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from myapp.views import *

urlpatterns = [
    #   path('admin/', admin.site.urls),
    path('admin/', AdminControl.view_admin, name='views_admin'),
    path('admin/login/', AdminControl.login_admin, name='login_admin'),
    #  path('admin/register', AdminControl.register_user, name='register_user'),
    path('admin/logout', AdminControl.log_out, name='logout_admin'),
    path('admin/profile', AdminControl.profile, name='profile_admin'),
    path('admin/website', AdminControl.view_website, name='view_website'),

    #  Product
    path('admin/product/', ManageProduct.list, name='table_product'),
    path('admin/product/add', ManageProduct.create, name='add_product'),
    path('admin/product/show/<int:id>', ManageProduct.show, name='show_product'),
    path('admin/product/edit/<int:id>', ManageProduct.edit, name='edit_product'),
    path('admin/product/delete/<int:id>', ManageProduct.delete, name='delete_product'),
    #  Category
    path('admin/category/', ManageCategory.list, name='table_category'),
    path('admin/category/add', ManageCategory.create, name='add_category'),
    path('admin/category/show/<int:id>', ManageCategory.show, name='show_category'),
    path('admin/category/edit/<int:id>', ManageCategory.edit, name='edit_category'),
    path('admin/category/delete/<int:id>', ManageCategory.delete, name='delete_category'),

    #  Customer
    path('admin/customer/', ManageCustomer.list, name='table_customer'),
    path('admin/customer/show/<int:id>', ManageCustomer.show, name='show_customer'),
    path('admin/customer/lock/<int:id>', ManageCustomer.lock, name='lock_customer'),
    path('admin/customer/delete/<int:id>', ManageCustomer.delete, name='delete_customer'),
    #
    path('admin/order/', ManageOrder.list, name='table_order'),
    path('admin/order/show/<int:id>', ManageOrder.show, name='show_order'),
    path('admin/order/cancel/<int:id>', ManageOrder.cancel, name='cancel_order'),
    path('', include('myapp.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
