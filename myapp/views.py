from django.contrib.auth import authenticate, login, logout
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


from myapp.forms import *
from myapp import models
from myapp.cart import Cart


# Create your views here.


class AdminControl:

    def login_admin(request):
        form_login = UserLoginForm(request.POST or None)
        if form_login.is_valid():
            username = form_login.cleaned_data.get('user_name')
            password = form_login.cleaned_data.get('password_login')
            user = authenticate(username=username, password=password)
            if user.is_superuser == 1:
                login(request, user)
                return redirect('views_admin')
        context = {'form_login': form_login}
        return render(request, 'my_admin/login.html', context)

    def register_user(request):
        form = UserRegisterForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            user = form.save(commit=False)
            password = form.cleaned_data.get('password')
            user.set_password(password)
            user.save()
            return redirect('login_admin')
        return render(request, 'my_admin/register.html', {'form': form})

    @login_required(login_url='/login/')
    def view_admin(request):
        obj_info = None
        if request.user.is_superuser == 1:
            if models.Information_User.objects.filter(user_id=request.user.id).exists():
                obj_info = request.user.information
            obj_pro = models.Product.objects.all()
            obj_user = models.User.objects.filter(is_superuser=0)
            obj_order = models.Order.objects.filter(status=1)
            total_order = len(obj_order)
            total_cus = len(obj_user)
            total_pro = len(obj_pro)
            total_money = 0
            for i in obj_order:
                total_money += i.total
            context = {
                'obj_info': obj_info,
                'total_cus': total_cus,
                'total_order': total_order,
                'total_money': total_money,
                'total_pro': total_pro
            }
            return render(request, 'my_admin/index.html', context)
        else:
            return redirect('login_admin')

    def log_out(request):
        logout(request)
        return redirect('login_admin')

    def profile(request):
        obj_info = None
        form_user = UserInforFormHome(request.POST or None, request.FILES or None, instance=request.user)
        form_change_pass = UserChangePasswordFormHome(request.POST or None)
        if models.Information_User.objects.filter(user_id=request.user.id).exists():
            obj_info = request.user.information

        if form_user.is_valid():
            if models.Information_User.objects.filter(user_id=request.user.id).exists():
                obj_info.phone = request.POST['phone']
                obj_info.address = request.POST['address']
                obj_info.content = request.POST['content']
                obj_info.image = request.FILES['image']
                obj_info.save()
            else:
                model = models.Information_User(phone=request.POST['phone'], address=request.POST['address'],
                                                content=request.POST['content'], image=request.FILES['image'],
                                                user=request.user)
                model.save()
            form_user.save()
            return redirect('profile_admin')

        if form_change_pass.is_valid():
            new_pass = form_change_pass.cleaned_data.get('password')
            pass_confirm = form_change_pass.cleaned_data.get('config_password')
            if new_pass == pass_confirm:
                request.user.set_password(pass_confirm)
                request.user.save()
                return redirect('logout_admin')

        context = {
            'form_change_pass': form_change_pass,
            'form_user': form_user,
            'obj_info': obj_info
        }

        return render(request, 'my_admin/pages/user/profile.html', context)

    def view_website(request):
        logout(request)
        return redirect('home')


class ManageProduct:
    @login_required(login_url='/login/')
    def list(request):
        obj_info = None
        if models.Information_User.objects.filter(user_id=request.user.id).exists():
            obj_info = request.user.information
        obj = models.Product.objects.all()
        return render(request, 'my_admin/pages/product/tables.html', {'obj': obj, 'obj_info': obj_info})

    @login_required(login_url='/login/')
    def create(request):
        obj_info = None
        if models.Information_User.objects.filter(user_id=request.user.id).exists():
            obj_info = request.user.information
        form = ProductForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            form.save()
            return redirect('table_product')
        return render(request, 'my_admin/pages/product/forms.html', {'form': form, 'obj_info': obj_info})

    @login_required(login_url='/login/')
    def show(request, id):
        obj = models.Product.objects.get(id=id)
        return render(request, 'my_admin/pages/product/show.html', {'obj': obj})

    @login_required(login_url='/login/')
    def edit(request, id):
        obj_info = None
        if models.Information_User.objects.filter(user_id=request.user.id).exists():
            obj_info = request.user.information
        obj = models.Product.objects.get(id=id)
        form = ProductForm(request.POST or None, request.FILES or None, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('table_product')
        return render(request, 'my_admin/pages/product/forms.html', {'form': form, 'obj_info': obj_info})

    @login_required(login_url='/login/')
    def delete(request, id):
        obj_del = models.Product.objects.get(id=id)
        obj_del.delete()
        return redirect('table_product')


class ManageCategory:
    @login_required(login_url='/login/')
    def list(request):
        obj_info = None
        if models.Information_User.objects.filter(user_id=request.user.id).exists():
            obj_info = request.user.information
        obj = models.Category.objects.all()
        return render(request, 'my_admin/pages/category/tables.html', {'obj': obj, 'obj_info': obj_info})

    @login_required(login_url='/login/')
    def create(request):
        obj_info = None
        if models.Information_User.objects.filter(user_id=request.user.id).exists():
            obj_info = request.user.information
        form = CategoryForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            form.save()
            return redirect('table_category')
        return render(request, 'my_admin/pages/category/forms.html', {'form': form, 'obj_info': obj_info})

    @login_required(login_url='/login/')
    def show(request, id):
        obj = models.Category.objects.get(id=id)
        return render(request, 'my_admin/pages/category/show.html', {'obj': obj})

    @login_required(login_url='/login/')
    def edit(request, id):
        obj_info = None
        if models.Information_User.objects.filter(user_id=request.user.id).exists():
            obj_info = request.user.information
        obj = models.Category.objects.get(id=id)
        form = CategoryForm(request.POST or None, request.FILES or None, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('table_category')
        return render(request, 'my_admin/pages/category/forms.html', {'form': form, 'obj_info': obj_info})

    @login_required(login_url='/login/')
    def delete(request, id):
        obj_del = models.Category.objects.get(id=id)
        obj_del.delete()
        return redirect('table_category')


class ManageCustomer:
    @login_required(login_url='/login/')
    def list(request):
        obj_info = None
        if models.Information_User.objects.filter(user_id=request.user.id).exists():
            obj_info = request.user.information
        obj = models.User.objects.filter(is_superuser=0)
        return render(request, 'my_admin/pages/customer/tables.html', {'obj': obj, 'obj_info': obj_info})

    @login_required(login_url='/login/')
    def show(request, id):
        obj = models.User.objects.get(id=id)
        obj_info = None
        if models.Information_User.objects.filter(user_id=id).exists():
            obj_info = obj.information
        return render(request, 'my_admin/pages/customer/show.html', {'obj': obj, 'obj_info': obj_info})

    @login_required(login_url='/login/')
    def delete(request, id):
        obj_del = models.User.objects.get(id=id)
        obj_del.delete()
        return redirect('table_customer')

    @login_required(login_url='/login/')
    def lock(request, id):
        obj = models.User.objects.get(id=id)
        if obj.is_active == 1:
            obj.is_active = 0
        else:
            obj.is_active = 1
        obj.save()
        return redirect('table_customer')


class ManageOrder:
    @login_required(login_url='/login/')
    def list(request):
        obj_info = None
        if models.Information_User.objects.filter(user_id=request.user.id).exists():
            obj_info = request.user.information
        obj = models.Order.objects.all()

        return render(request, 'my_admin/pages/order/tables.html', {'obj': obj, 'obj_info': obj_info})

    @login_required(login_url='/login/')
    def show(request, id):
        obj = models.Order.objects.get(id=id)
        order_detail = models.Order_item.objects.filter(order_id=id)
        return render(request, 'my_admin/pages/order/show.html', {'obj': obj, 'order_detail': order_detail})

    @login_required(login_url='/login/')
    def cancel(request, id):
        obj = models.Order.objects.get(id=id)
        if obj.status == 1:
            obj.status = 0
        else:
            obj.status = 1
        obj.save()
        return redirect('table_order')


class HomeControl:

    def index(request):
        categories = models.Category.objects.all()
        products = models.Product.objects.filter(status=1, active_home=1)
        context = {'categories': categories, 'products': products}
        return render(request, 'web/pages/index.html', context)

    def product(request):
        products = models.Product.objects.all()
        categories = models.Category.objects.all()
        paginator = Paginator(products, 8)
        page = request.GET.get('page', 1)
        try:
            page_obj = paginator.page(page)
        except PageNotAnInteger:
            page_obj = paginator.page(1)
        except EmptyPage:
            page_obj = paginator.page(paginator.num_pages)

        context = {'categories': categories,
                   'products': page_obj,
                   }
        return render(request, 'web/pages/category.html', context)

    def category(request):
        categories = models.Category.objects.all()
        products = models.Product.objects.all()
        paginator = Paginator(products, 6)
        page = request.GET.get('page', 1)
        try:
            page_obj = paginator.page(page)
        except PageNotAnInteger:
            page_obj = paginator.page(1)
        except EmptyPage:
            page_obj = paginator.page(paginator.num_pages)

        context = {'categories': categories,
                   'products': page_obj,
                   }
        return render(request, 'web/pages/category.html', context)

    def search(request):
        search = request.POST.get('search_pro')
        categories = models.Category.objects.all()
        products = models.Product.objects.filter(name__contains=str(search))
        context = {'categories': categories,
                   'products': products,
                   }
        return render(request, 'web/pages/category.html', context)

    def view_category(request, id):
        categories = models.Category.objects.all()
        cat_id = models.Category.objects.get(id=id)
        products = models.Product.objects.filter(cat=id)
        paginator = Paginator(products, 6)
        page = request.GET.get('page', 1)
        try:
            page_obj = paginator.page(page)
        except PageNotAnInteger:
            page_obj = paginator.page(1)
        except EmptyPage:
            page_obj = paginator.page(paginator.num_pages)

        context = {'categories': categories,
                   'products': page_obj,
                   'cat_id': cat_id
                   }
        return render(request, 'web/pages/category.html', context)

    def detail_product(request, id):
        categories = models.Category.objects.all()
        products = models.Product.objects.get(id=id)
        similar_products = models.Product.objects.filter(cat=products.cat)[:4]
        context = {'categories': categories,
                   'products': products,
                   'similar_products': similar_products
                   }
        return render(request, 'web/pages/detail.html', context)

    def login_register(request):
        form_register = UserRegisterFormHome(request.POST or None)
        form_login = UserLoginForm(request.POST or None)
        if form_register.is_valid():
            user = form_register.save(commit=False)
            password = form_register.cleaned_data.get('password')
            user.set_password(password)
            user.save()
            return redirect('register_login')
        if form_login.is_valid():
            username = form_login.cleaned_data.get('user_name')
            password = form_login.cleaned_data.get('password_login')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')
        context = {'form_register': form_register, 'form_login': form_login}
        return render(request, 'web/pages/register.html', context)

    def logout_view_home(request):
        logout(request)
        return redirect('home')

    def contact(request):
        categories = models.Category.objects.all()
        context = {'categories': categories}
        return render(request, 'web/pages/contact.html', context)


class ShoppingCart:
    def view_basket(request):
        cart = Cart(request)
        carts = cart.list()
        categories = models.Category.objects.all()
        products = models.Product.objects.all()
        total = 0
        for i in carts:
            total += i['price']
        context = {'categories': categories,
                   'products': products,
                   'carts': carts,
                   'total': total,
                   'cart': cart,
                   }
        return render(request, 'web/pages/basket.html', context)

    def add_to_cart(request, id):
        if request.method == 'POST':
            product = models.Product.objects.get(id=id)
            quantity = int(request.POST['quantity'])
            cart = Cart(request)
            cart.add(product, quantity)
            return HomeControl.detail_product(request, id)

    def add_cart(request, id):
        if request.method == 'POST':
            product = models.Product.objects.get(id=id)
            quantity = 1
            if not quantity:
                quantity = 1
            cart = Cart(request)
            cart.add(product, quantity)
            return redirect('categories')

    def update_cart(request, id):
        if request.method == 'POST':
            data = request.POST
            quantity = int(data['quantity'])
            cart = Cart(request)
            cart.update(quantity, id)
        return redirect('basket')

    def del_item_cart(request, id):
        cart = Cart(request)
        cart.delete(id)
        return redirect('basket')

    def del_cart(request):
        del request.session['cart']
        return redirect('basket')


class CheckOut:
    @login_required(login_url='/register-Login/')
    def checkout(request):
        cart = Cart(request)
        carts = cart.list()
        categories = models.Category.objects.all()
        obj_user = None
        total = 0
        for i in carts:
            total += i['price']
        if request.user:
            obj_user = models.User.objects.get(id=request.user.id)
        context = {'categories': categories,
                   'cart': cart,
                   'carts': carts,
                   'obj_user': obj_user,
                   'total': total,
                   }
        return render(request, 'web/pages/checkout.html', context)

    def order(request):
        obj_info = None
        cart = Cart(request)
        carts = cart.list()
        categories = models.Category.objects.all()
        obj_user = models.User.objects.get(id=request.user.id)
        total = 0
        for i in carts:
            total += i['price']

        if models.Information_User.objects.filter(user_id=request.user.id).exists():
            obj_info = models.Information_User.objects.filter(user_id=request.user.id)

        if request.user:
            order_info = models.Order(
                phone=request.POST['phone'],
                address=request.POST['address'],
                user=request.user,
                pays=request.POST['payment'],
                total=total,
            )
            order_info.save()
            order = models.Order.objects.get(id=order_info.id)
            for item in carts:
                pro = models.Product.objects.get(id=item['id'])
                model_order_detail = models.Order_item(
                    pro=pro,
                    order=order,
                    price=item['price'],
                    quantity=item['quantity'],
                )
                model_order_detail.save()
            order_item = models.Order_item.objects.filter(order_id=order_info.id)

        del request.session['cart']

        context = {'categories': categories,
                   'order_info': order_info,
                   'obj_user': obj_user,
                   'order_item': order_item,
                   'total': total,
                   'obj_info': obj_info,
                   }
        return render(request, 'web/pages/checkout_ok.html', context)


class Customer:
    @login_required(login_url='/register-Login/')
    def customer_account(request):
        obj_info = None
        categories = models.Category.objects.all()
        form_user = UserInforFormHome(request.POST or None, instance=request.user)
        form_change_pass = UserChangePasswordFormHome(request.POST or None)
        if models.Information_User.objects.filter(user_id=request.user.id).exists():
            obj_info = request.user.information

        if form_user.is_valid():
            if models.Information_User.objects.filter(user_id=request.user.id).exists():
                obj_info.phone = request.POST['phone']
                obj_info.address = request.POST['address']
                obj_info.save()
            else:
                model = models.Information_User(phone=request.POST['phone'], address=request.POST['address'],
                                                user=request.user)
                model.save()
            form_user.save()
            return redirect('account')
        if form_change_pass.is_valid():
            new_pass = form_change_pass.cleaned_data.get('password')
            pass_confirm = form_change_pass.cleaned_data.get('config_password')
            if new_pass == pass_confirm:
                request.user.set_password(pass_confirm)
                request.user.save()
                return redirect('logout_home')

        context = {
            'categories': categories,
            'form_change_pass': form_change_pass,
            'form_user': form_user,
            'obj_info': obj_info
        }

        return render(request, 'web/customers/customer-account.html', context)

    def order_account(request):
        categories = models.Category.objects.all()
        order = models.Order.objects.filter(user=request.user)
        context = {
            'categories': categories,
            'order': order,
        }
        return render(request, 'web/customers/customer-orders.html', context)

    def view_order(request, id):
        obj = models.Order.objects.get(id=id)
        order_detail = models.Order_item.objects.filter(order_id=id)
        return render(request, 'web/customers/show.html', {'obj': obj, 'order_detail': order_detail})

    def cancel_order(request, id):
        obj = models.Order.objects.get(id=id)
        if obj.status == 1:
            obj.status = 0
        else:
            obj.status = 1
        obj.save()
        return redirect('acc_orders')

    @login_required(login_url='/register-Login/')
    def add_wish_list(request, id):
        obj_wish = models.Wish_list.objects.values_list('pro_id', flat=True).filter(user_id=request.user.id)
        list_pro_id = list(obj_wish)
        if id in list_pro_id:
            obj = models.Wish_list.objects.get(user_id=request.user.id, pro_id=id)
            obj.delete()
        else:
            obj = models.Wish_list(
                user=request.user,
                pro=models.Product.objects.get(id=id)
            )
            obj.save()
        return HomeControl.detail_product(request, id)

    def view_wish_list(request):
        categories = models.Category.objects.all()
        obj = models.Wish_list.objects.filter(user_id=request.user.id)
        context = {
            'obj': obj,
            'categories': categories
        }
        return render(request, 'web/customers/customer-wish.html', context)

    def remove_wish(request, id):
        obj = models.Wish_list.objects.filter(user_id=request.user.id, pro_id=id)
        obj.delete()
        return redirect('wish_list')



