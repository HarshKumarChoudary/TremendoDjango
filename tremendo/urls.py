from django.urls import path
from django.conf import settings

from django.conf.urls.static import static

from tremendo import views
from tremendo.forms import passwordresetform,passwordchangeform
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static

urlpatterns = [
    path('',views.home,name='home'),
    path('register',views.register_attempt,name='register_attempt'),
    path('login',views.login_attempt,name='login_attempt'),
    path('token',views.token_send,name='token_send'),
    path('success',views.success,name='success'),
    path('verify/<auth_token>',views.verify,name='verify'),
    path('error',views.error_page,name='error'),
    path('student_dashboard/',views.student_dashboard.as_view(),name='student_dashboard'),
    path('teacher_dashboard/',views.teacher_dashboard.as_view(),name='teacher_dashboard'),
    path('password_reset/',auth_views.PasswordResetView.as_view(),name='password_reset'),
    path('password_reset/done/',auth_views.PasswordResetDoneView.as_view(),name='password_reset_done'),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
    path('reset/done/',auth_views.PasswordResetCompleteView.as_view(),name='password_reset_complete'),
    path('logout/',auth_views.LogoutView.as_view(next_page='/login'),name='logout'),
    path('simg',views.simg,name="simg"),
    path('timg',views.timg,name="timg"),
    path('account/login',views.login_attempt,name="login"),
]
