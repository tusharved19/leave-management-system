from django.urls import path
from .import views

app_name ='user'

urlpatterns = [

    path('user_create/',views.register_user,name = 'register'),
    path('user_login/',views.login_view,name = 'login'),
    path('users/all',views.users_list,name='users'),
    path('logout/',views.logout_view,name='logout'),
]