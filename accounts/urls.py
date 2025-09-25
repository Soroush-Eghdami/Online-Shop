from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'accounts'

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html', next_page='shop:product_list'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='shop:product_list'), name='logout'),
    path('profile/', views.profile, name='profile'),
]

