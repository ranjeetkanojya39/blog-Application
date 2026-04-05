from django.urls import path
from . import views


urlpatterns = [

    path('', views.signup, name='signup-page'),
    path('loginn/', views.loginn, name='login-page'),
    path('home/',views.home, name='home-page'),
    path('newpost/', views.newPost, name='new-post'),
    path('mypost/', views.myPosts, name='my-post'),   
    path('signout/', views.signout, name='logout'),
     path('delete/<int:id>/', views.delete_post, name='delete-post'),
]

