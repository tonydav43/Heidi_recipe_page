from django.urls import path, include
from . import views

app_name = "account"

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register_view, name='register'),
    path('profile/', views.user_profile_page_view, name='profile'),
    path('profile/edit/', views.user_edit_profile_page_view, name='profile_edit'),
    path('change_password/', views.user_change_password_view, name='change_password'), 
    path('delete_user/<int:pk>/', views.UserDeleteView.as_view(), name='delete_user'),  
]

