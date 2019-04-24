from django.urls import path
from . import views
from django.views.generic.base import TemplateView

urlpatterns = [
    #path('', views.message_list, name='message_list'),
    path('', TemplateView.as_view(template_name = 'AetherMail/home.html'), name='home'),

    path('inbox/', views.inbox_list, name='inbox'),
    path('sent/', views.sent_list, name='sent'),
    path('compose/', views.compose, name='compose'),
    path('signup/', views.SignUp.as_view(), name='signup'),
    #path('mail/<int:pk>/', views.read_msg, name='read_msg'),
    path('sent/mail/<int:pk>/', views.read_sent_msg, name='read_sent_msg'),
    path('sent/delete/<int:pk>/', views.delete_from_sent, name='delete_from_sent'),

    path('inbox/mail/<int:pk>/', views.read_inbox_msg, name='read_inbox_msg'),
    path('inbox/delete/<int:pk>/', views.delete_from_inbox, name='delete_from_inbox'),

    path('trash/', views.trash, name='trash'),
    path('trash/mail/<int:pk>/', views.read_trash_msg, name='read_trash_msg'),

]