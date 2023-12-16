from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('success/', views.success_view, name='success'),
    path('viewall/', views.user_list, name='user_list'),
    path('start_conversation/<int:user_id>/', views.start_conversation, name='start_conversation'),
    path('view_conversation/<int:conversation_id>/', views.view_conversation, name='view_conversation'),
    path('send_message/<int:conversation_id>/', views.send_message, name='send_message'),
    ]
