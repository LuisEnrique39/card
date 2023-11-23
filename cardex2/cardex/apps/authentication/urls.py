
from django.urls import path,re_path,include
from .views import login_view, register_user
from django.contrib.auth.views import LogoutView
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView

urlpatterns = [
    path('login/', login_view, name="login"),
    path('register/', register_user, name="register"),
    path("logout/", LogoutView.as_view(), name="logout"),

    path('reset/password_reset', PasswordResetView.as_view(template_name='recovery/password_reset_form.html', email_template_name="recovery/password_reset_email.html"), name = 'password_reset'),

    path('reset/password_reset_done', PasswordResetDoneView.as_view(template_name='recovery/password_reset_done.html'), name = 'password_reset_done'),

    re_path(r'^reset/(?P<uidb64>[0-9A-za-z_\-]+)/(?P<token>.+)/$', PasswordResetConfirmView.as_view(template_name='recovery/password_reset_confirm.html'), name = 'password_reset_confirm'),

    path('reset/done',PasswordResetCompleteView.as_view(template_name='recovery/password_reset_complete.html') , name = 'password_reset_complete'),
]
