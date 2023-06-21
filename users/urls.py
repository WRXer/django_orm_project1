from django.contrib.auth.views import LoginView, LogoutView, PasswordResetView
from django.urls import path

from users.apps import UsersConfig
from users.views import RegisterView, ProfileView, VerifyEmailView, VerifyEmailSentView, EmailConfirmedView

app_name = UsersConfig.name





urlpatterns = [
    path('', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('verify_email/<str:uidb64>/<str:token>/', VerifyEmailView.as_view(), name='verify_email'),
    path('verify_email_sent/', VerifyEmailSentView.as_view(), name='verify_email_sent'),
    path('email_confirmed/', EmailConfirmedView.as_view(), name='email_confirmed'),
    path('password_reset/', PasswordResetView.as_view(), name='password_reset'),

]