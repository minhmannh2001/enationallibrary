from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from .models import Customer

gender_choice = [
    ('Nam', 'Nam'),
    ('Nữ', 'Nữ'),
    ('Không xác định', 'Không xác định'),
]
city_choice = [
    ('Hà Nội', 'Hà Nội'),
    ('Bắc Ninh', 'Bắc Ninh'),
    ('Thanh Hóa', 'Thanh Hóa'),
    ('Nghệ An', 'Nghệ An'),
    ('TP Hồ Chí Minh', 'TP Hồ Chí Minh'),
    ('Đà Nẵng', 'Đà Nẵng'),
    ('Hải Phòng', 'Hải Phòng'),
    ('Cần Thơ', 'Cần Thơ'),
    ('Không Xác Định', 'Không Xác Định')
]


class UpdateProfileForm(forms.ModelForm):
    lastName = forms.CharField(max_length=30, required=True,
                               widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'lastName'}))
    firstName = forms.CharField(max_length=30, required=True,
                                widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'firstName'}))
    dateOfBirth = forms.DateField(
        widget=forms.DateInput(attrs={'class': 'datepicker', 'placeholder': 'Select a date', 'type': 'date'}))
    gender = forms.TypedChoiceField(choices=gender_choice)
    address = forms.CharField(max_length=30, required=True,
                              widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Address'}))
    city = forms.TypedChoiceField(choices=city_choice)
    identificationCard = forms.CharField(max_length=30, required=True, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'identificationCard'}))
    email = forms.CharField(max_length=30, required=True,
                            widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'email'}))
    phoneNumber = forms.CharField(max_length=30, required=True,
                                  widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'phoneNumber'}))

    class Meta:
        model = Customer
        fields = ['lastName', 'firstName', 'dateOfBirth', 'gender', 'address', 'city', 'identificationCard', 'email',
                  'phoneNumber']


class formOrder(forms.ModelForm):
    name = forms.CharField(label='Your name', max_length=30, required=True, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Tên khách hàng', 'width': '196%'}))
    address = forms.CharField(label='Address', max_length=30, required=True, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Địa chỉ', 'width': '196%'}))
    city = forms.TypedChoiceField(label='City', choices=city_choice, widget=forms.Select(
        attrs={'class': 'form-control', 'id': 'mySelect', 'onchange': 'myFunction()', 'width': '196%'}))
    postalCode = forms.CharField(label='Postal Code', max_length=3, required=True, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Mã bưu chính', 'width': '196%'}))
    phoneNumber = forms.CharField(label='Phone Number', max_length=30, required=True, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Số điện thoại', 'width': '196%'}))
    giftCartOrDiscount = forms.CharField(label='gift Cart Or Discount', max_length=10, required=False,
                                         widget=forms.TextInput(
                                             attrs={'class': 'form-control', 'placeholder': 'Mã giảm giá',
                                                    'width': '196%'}))

    class Meta:
        model = Customer
        fields = ['name', 'address',
                  'city',
                  'postalCode', 'phoneNumber', 'giftCartOrDiscount']


class formReturn(forms.ModelForm):
    lastName = forms.CharField(max_length=30, required=True, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'lastName', 'width': '196%'}))
    firstName = forms.CharField(max_length=30, required=True, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'firstName', 'width': '196%'}))
    bookName = forms.CharField(max_length=200, required=True, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'book name', 'width': '196%'}))
    numberOfbook = forms.IntegerField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'book id', 'width': '510px', 'width': '196%'}))
    img = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control-file'}))

    class Meta:
        model = Customer
        fields = ['lastName', 'firstName', 'bookName', 'numberOfbook', 'img']


class updatePlanform(forms.ModelForm):
    # num = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'num'}))
    cardNumber = forms.IntegerField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Card Number', 'width': '510px'}))
    country = forms.CharField(max_length=30, required=True, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Country', 'width': '510px'}))
    expirationDate = forms.DateField(
        widget=forms.DateInput(attrs={'class': 'datepicker', 'placeholder': 'Select a date', 'type': 'date'}))
    securityCode = forms.IntegerField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Security Code'}))
    postalCode = forms.IntegerField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Postal Code'}))

    class Meta:
        model = Customer
        fields = ['cardNumber', 'country', 'expirationDate', 'securityCode', 'postalCode']


class registerPlanform(forms.ModelForm):
    lastName = forms.CharField(max_length=30, required=True, label='lastName',
                               widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'lastName'}))
    firstName = forms.CharField(max_length=30, required=True,
                                widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'firstName'}))
    dateOfBirth = forms.DateField(widget=forms.DateInput(
        attrs={'class': 'datepicker', 'placeholder': 'Select a date', 'type': 'date', 'width': '196%'}))
    email = forms.CharField(max_length=30, required=True, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'email', 'width': '196%'}))
    address = forms.CharField(label='Address', max_length=30, required=True, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Address', 'width': '196%'}))
    city = forms.TypedChoiceField(label='City', choices=city_choice, widget=forms.Select(
        attrs={'class': 'form-control', 'placeholder': 'City', 'width': '196%'}))
    postalCode = forms.CharField(label='Postal Code', max_length=3, required=True, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Postal Code', 'width': '196%'}))
    identificationCard = forms.CharField(max_length=30, required=True, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'identificationCard', 'width': '196%'}))
    gender = forms.TypedChoiceField(choices=gender_choice)
    phoneNumber = forms.CharField(label='Phone Number', max_length=30, required=True, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Phone Number', 'width': '196%'}))

    class Meta:
        model = Customer
        fields = ['lastName', 'firstName', 'dateOfBirth', 'email', 'address', 'city', 'postalCode',
                  'identificationCard', 'gender', 'phoneNumber']