from django.urls import path, include
from . import views


urlpatterns = [
    path('login/', views.login_user, name="login"),
    path('logout/', views.logout_user, name="logout"),
    
    path('', views.dashboard, name="dashboard"),
    path('incoming/', views.incoming, name="incoming"),
    path('incoming_form/', views.incoming_form, name="incoming_form"),
    path('update_incoming/<str:pk>/', views.incoming_form_update, name="incoming_form_update"),
    path('delete_incoming/<str:pk>/', views.incoming_form_delete, name="incoming_form_delete"),

    path('outgoing/', views.outgoing, name="outgoing"),
    path('outgoing_form/', views.outgoing_form, name="outgoing_form"),
    path('update_outgoing/<str:pk>/', views.outgoing_form_update, name="outgoing_form_update"),
    path('delete_outgoing.html/<str:pk>/', views.outgoing_form_delete, name="outgoing_form_delete")

]