from email.policy import default
from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.models import User

from myapp import models


class CategoryForm(forms.ModelForm):
    name = forms.CharField(label='Tên danh mục', widget=forms.TextInput(attrs={'class': "form-control"}))
    description = forms.CharField(label='Keyword', widget=forms.Textarea(attrs={'class': "form-control"}))
    keyword = forms.CharField(label='Mô tả', widget=forms.TextInput(attrs={'class': "form-control"}))
    status = forms.BooleanField(label='Trạng thái', required=False)

    class Meta:
        model = models.Category
        fields = ['name', 'description', 'keyword', 'status']


class ProductForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': "form-control"}))
    cat = forms.ModelChoiceField(empty_label='Chọn loại danh mục', required=True,
                                 widget=forms.Select(attrs={'class': "form-control"}),
                                 queryset=models.Category.objects.filter(status=1))
    price = forms.CharField(widget=forms.TextInput(attrs={'class': "form-control"}))
    size = forms.CharField(widget=forms.TextInput(attrs={'class': "form-control"}))
    status = forms.BooleanField(label='Hide product', required=False)
    active_home = forms.BooleanField(label='Hiển thị trang chủ', required=False)
    description = forms.CharField(label='Mô tả', widget=forms.Textarea(attrs={'class': "form-control"}))
    keyword = forms.CharField(label='Keyword', widget=forms.TextInput(attrs={'class': "form-control"}))

    class Meta:
        model = models.Product
        fields = ['name', 'cat', 'price', 'size', 'active_home', 'image', 'keyword', 'description', 'status']


class UserRegisterForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(
        attrs={'id': "register-username", 'type': "text", 'name': "registerUsername",
               'required data-msg': "Please enter your username",
               'class': "input-material"}))
    email = forms.CharField(widget=forms.TextInput(attrs={'id': "register-email",
                                                          'type': "email", 'name': "registerEmail",
                                                          'required data-msg': "Please enter your password",
                                                          'class': "input-material"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'id': "register-password",
                                                                 'type': "password", 'name': "registerPassword",
                                                                 'required data-msg': "Please enter your password",
                                                                 'class': "input-material"}))


#  customer


class UserRegisterFormHome(forms.ModelForm):
    first_name = forms.CharField(label='Họ', widget=forms.TextInput(attrs={'class': "form-control"}))
    last_name = forms.CharField(label='Tên', widget=forms.TextInput(attrs={'class': "form-control"}))
    username = forms.CharField(label='Tên người dùng', widget=forms.TextInput(attrs={'class': "form-control"}))
    email = forms.EmailField(label='Email', widget=forms.TextInput(attrs={'class': "form-control"}))
    password = forms.CharField(label='Mật khẩu', widget=forms.PasswordInput(attrs={'class': "form-control"}))
    config_password = forms.CharField(label='Nhập lại mật khẩu',
                                      widget=forms.PasswordInput(attrs={'class': "form-control"}))

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password']

        def config_password(self):
            password = self.cleaned_data.get('config_password')
            config = self.cleaned_data.get('config_password')
            if password != config:
                raise forms.ValidationError('Mật khẩu config không hợp lệ')
            return password

        def clean_email(self):
            email = self.cleaned_data.get('email')
            email_qs = User.objects.filter(email=email)
            if email_qs.exists():
                raise forms.ValidationError('Email này đã được sử dụng')
            return email


class UserLoginForm(forms.Form):
    user_name = forms.CharField(label='Tên người dùng', widget=forms.TextInput(attrs={'class': "form-control"}))
    password_login = forms.CharField(label='Mật khẩu', widget=forms.PasswordInput(attrs={'class': "form-control"}))

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get('user_name')
        password = self.cleaned_data.get('password_login')
        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError('Người dùng này không tồn tại')
            if not user.check_password(password):
                raise forms.ValidationError('Mật khẩu không chính xác')
            if not user.is_active:
                raise forms.ValidationError('Tài khoản này hiện không hoạt động')
        return super(UserLoginForm, self).clean(*args, **kwargs)


class InformationUserForm(forms.ModelForm):
    phone = forms.CharField(widget=forms.TextInput(attrs={'class': "form-control"}))
    address = forms.CharField(widget=forms.Textarea(attrs={'class': "form-control"}))
    content = forms.CharField(widget=forms.Textarea(attrs={'class': "form-control"}))
    image = forms.CharField(widget=forms.FileInput(attrs={'class': "form-control"}))

    class Meta:
        model = models.Information_User
        fields = [
            'phone', 'address', 'content', 'image'
        ]


class UserChangePasswordFormHome(forms.Form):
    password = forms.CharField(label='Mật khẩu', widget=forms.PasswordInput(attrs={'class': "form-control"}))
    config_password = forms.CharField(label='Nhập lại mật khẩu',
                                       widget=forms.PasswordInput(attrs={'class': "form-control"}))


class UserInforFormHome(forms.ModelForm):
    first_name = forms.CharField(label='Họ', widget=forms.TextInput(attrs={'class': "form-control"}))
    last_name = forms.CharField(label='Tên', widget=forms.TextInput(attrs={'class': "form-control"}))
    email = forms.EmailField(label='Địa chỉ email', widget=forms.TextInput(attrs={'class': "form-control"}))

    class Meta:
        model = User
        fields = [
            'first_name', 'last_name', 'email'
        ]

    # def clean_email(self):
    #     email = self.cleaned_data.get('email')
    #     email_qs = User.objects.filter(email=email)
    #     if email_qs.exists():
    #         raise forms.ValidationError('Email này đã được sử dụng')
    #     return email


class UserRegisterForm(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': "form-control"}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': "form-control"}))
    username = forms.CharField(widget=forms.TextInput(attrs={'class': "form-control"}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'class': "form-control"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': "form-control"}))
    is_superuser = forms.BooleanField(required=False)
    is_staff = forms.BooleanField(required=False)
    is_active = forms.BooleanField(required=False)

    class Meta:
        model = User
        fields = [
            'first_name', 'last_name', 'username', 'email', 'password', 'is_superuser', 'is_staff', 'is_active'
        ]

    def clean_email(self):
        email = self.cleaned_data.get('email')
        email_qs = User.objects.filter(email=email)
        if email_qs.exists():
            raise forms.ValidationError('Email này đã được sử dụng')
        return email