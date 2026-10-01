from django.contrib import admin
from django.urls import path
from blog import views


urlpatterns = [
    # Admin
    path('admin/', admin.site.urls),

    # Home
    path('', views.home, name='home'),

    # Authentication
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),

    # Blog
    path(
        'blog/<int:blog_id>/',
        views.blog_detail,
        name='blog_detail'
    ),

    path(
        'create/',
        views.create_blog,
        name='create_blog'
    ),

    path(
        'edit/<int:blog_id>/',
        views.edit_blog,
        name='edit_blog'
    ),

    path(
        'delete/<int:blog_id>/',
        views.delete_blog,
        name='delete_blog'
    ),

    path(
        'my-blogs/',
        views.my_blogs,
        name='my_blogs'
    ),

    # Comments
    path(
        'comment/<int:blog_id>/',
        views.add_comment,
        name='add_comment'
    ),
]