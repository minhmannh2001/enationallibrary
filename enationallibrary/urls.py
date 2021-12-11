from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from . import settings
from django.contrib.auth import views as auth_views

admin.site.index_title = "Trang quản trị"

urlpatterns = [
    path('home/', include('home.urls')),
    path('location/', include('location.urls')),
    path('login/', include('login.urls')),
    path('category/', include('category.urls')),
    path('myaccount/', include('myaccount.urls')),
    path('news/', include('news.urls')),
    path('services/', include('services.urls')),
    path('support/', include('support.urls')),
    path('admin/password_reset/', auth_views.PasswordResetView.as_view(), name='admin_password_reset'),
    path('admin/password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('admin/', admin.site.urls),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)