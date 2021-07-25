from django.urls import path 

from . import views

urlpatterns = [
    path('',views.alaaform, name='alaaform'),
    path('login',views.login, name='login'),
    path('logout',views.logout, name='logout'),
    path('register',views.register, name='register'),
    path('print_pg',views.print_pg, name='print_pg'),
    path('fac_user',views.fac_user, name='fac_user'),
    path('ffff',views.final_submition, name='final_submition'),
    path('error_404',views.error_404, name='error_404'),
    path('user_confirm',views.user_confirm, name='user_confirm')
]