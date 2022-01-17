from django.urls import path
from . import views

app_name = 'myaccount'

urlpatterns = [
    path('myprofile/', views.MyProfile.as_view(), name='profile'),
    path('register-before-using-service/', views.registerBefore, name='register_before'),
    path('mycart/', views.cart_view, name='my-cart'),
    path('add-to-cart/<int:pk>', views.add_to_cart_view,name='add-to-cart'),
    path('remove/<int:pk>', views.remove_from_cart, name='removecart'),
    path('neworder/<str:name>/<str:address>/<str:city>/', views.newOrder, name='neworder'),
    path('payment/', views.cart_payment, name='payment'),
    path('changepw/', views.change_password.as_view(),name='changepw'),
    path('savePW/', views.save_password,name='savePW'),
    path('changepf/', views.change_profile,name='changepf'),
    path('save/',views.save_profile,name='save'),
    path('myborrowed_books/', views.MyBorrowedBooks.as_view(), name='borrowBooks'),
    path('returnBook/<int:orderID>/<int:bookID>', views.returnBook, name='returnBook'),
    path('saveReturnBook/<int:orderID>/<int:bookID>',views.saveReturnBook,name='saveReturnBook'),
    path('myplan/', views.MyPlan.as_view(), name='my_plan'),
    path('updatePlan/<int:number>/', views.formUpdate, name='updatePlan'),
    path('savePlan/<int:number>/', views.updatePlan, name='savePlan'),
    path('invoice/<int:orderID>/<int:bookID>', views.download_invoice_view, name='invoice'),
    path('registerPlan/',views.enationallibrary,name='registerPlan'),
    path('registerPlanform',views.enationallibrary1,name='registerPlanform1'),
    path('getACard3',views.enationallibrary2,name='registerPlanform2'),
    path('viewmyCard',views.viewmycard,name='viewMyCard'),
    path('save_profile_plan',views.save_profile_plan,name='save_profile_plan'),
]


