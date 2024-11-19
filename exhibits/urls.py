from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('floor/<int:floor>/', views.floor, name='floor'),
    path('exhibit/<int:id>/', views.exhibit_detail, name='exhibit_detail'),
    path('add_exhibit/', views.add_exhibit, name='add_exhibit'),
    path('edit_exhibit/<int:id>/', views.edit_exhibit, name='edit_exhibit'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]