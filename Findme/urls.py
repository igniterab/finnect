from django.contrib import admin
from django.urls import path  , include
from accounts import views as user_views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/',user_views.register,name='register'),
    path('profile/',user_views.profile,name='profile'),
    path('profileupdate/',user_views.profileupdate,name='profile_update'),
    path('logout/',auth_views.LogoutView.as_view(template_name = 'accounts/logout.html'),name='logout'),
    path('login/',auth_views.LoginView.as_view(template_name = 'accounts/login.html'),name='login'),
    path('password-reset/',auth_views.PasswordResetView.as_view(template_name = 'accounts/password_reset.html'),
    name='password-reset'),
    path('password-reset/done',auth_views.PasswordResetDoneView.as_view(template_name = 'accounts/password_reset_done.html'),
    name='password-reset-done'),
    path('password-reset-confirm/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name = 'accounts/password_reset_confirm.html'),
    name='password-reset-confirm'),
    path('',include('home.urls')),

] + static(settings.MEDIA_URL , document_root = settings.MEDIA_ROOT)
