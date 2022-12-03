from django.urls import path
from Base import views

urlpatterns = [
    path('',views.home,name='home'),
    path('delete/<str:pk>/',views.delete,name='delete'),
    path('add/',views.addActivity,name='addActivity'),
    path('view/<str:pk>/',views.viewActivity,name='viewActivity'),
    path('edit/<str:pk>/',views.editActivity,name='editActivity'),
    path('register/',views.register,name='register'),
    path('login/',views.loginUser,name='login'),
    path('logout/', views.logoutUser, name="logout"),
    path('search/',views.search,name='search'),
    path('welcome/',views.welcome,name='welcome'), 
]