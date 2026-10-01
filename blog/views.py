from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q

from .models import Blog, Comment


# Home Page
def home(request):
    query = request.GET.get('q', '')
    category = request.GET.get('category', '')

    blogs = Blog.objects.all()

    if query:
        blogs = blogs.filter(
            Q(title__icontains=query) |
            Q(content__icontains=query)
        )

    if category:
        blogs = blogs.filter(category=category)

    categories = Blog.CATEGORY_CHOICES

    context = {
        'blogs': blogs,
        'query': query,
        'category': category,
        'categories': categories,
    }

    return render(request, 'blog/home.html', context)


# Register
def register_view(request):

    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':

        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if not username or not password:
            messages.error(
                request,
                'Username and password are required.'
            )
            return redirect('register')

        if password != confirm_password:
            messages.error(
                request,
                'Passwords do not match.'
            )
            return redirect('register')

        if User.objects.filter(username=username).exists():
            messages.error(
                request,
                'Username already exists.'
            )
            return redirect('register')

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        login(request, user)

        messages.success(
            request,
            'Account created successfully!'
        )

        return redirect('home')

    return render(request, 'blog/register.html')


# Login
def login_view(request):

    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:

            login(request, user)

            messages.success(
                request,
                f'Welcome {user.username}!'
            )

            return redirect('home')

        messages.error(
            request,
            'Invalid username or password.'
        )

    return render(request, 'blog/login.html')


# Logout
@login_required
def logout_view(request):

    logout(request)

    messages.success(
        request,
        'You have been logged out.'
    )

    return redirect('home')


# Blog Details
def blog_detail(request, blog_id):

    blog = get_object_or_404(
        Blog,
        id=blog_id
    )

    comments = blog.comments.all()

    return render(
        request,
        'blog/blog_detail.html',
        {
            'blog': blog,
            'comments': comments,
        }
    )


# Create Blog
@login_required
def create_blog(request):

    if request.method == 'POST':

        title = request.POST.get('title')
        content = request.POST.get('content')
        category = request.POST.get('category')
        image = request.POST.get('image')

        if not title or not content:
            messages.error(
                request,
                'Title and content are required.'
            )

            return redirect('create_blog')

        Blog.objects.create(
            title=title,
            content=content,
            category=category,
            image=image,
            author=request.user
        )

        messages.success(
            request,
            'Blog published successfully!'
        )

        return redirect('home')

    return render(
        request,
        'blog/create_blog.html'
    )


# Edit Blog
@login_required
def edit_blog(request, blog_id):

    blog = get_object_or_404(
        Blog,
        id=blog_id
    )

    if blog.author != request.user:

        messages.error(
            request,
            'You cannot edit this blog.'
        )

        return redirect('home')

    if request.method == 'POST':

        blog.title = request.POST.get('title')
        blog.content = request.POST.get('content')
        blog.category = request.POST.get('category')
        blog.image = request.POST.get('image')

        blog.save()

        messages.success(
            request,
            'Blog updated successfully!'
        )

        return redirect(
            'blog_detail',
            blog_id=blog.id
        )

    return render(
        request,
        'blog/edit_blog.html',
        {
            'blog': blog
        }
    )


# Delete Blog
@login_required
def delete_blog(request, blog_id):

    blog = get_object_or_404(
        Blog,
        id=blog_id
    )

    if blog.author != request.user:

        messages.error(
            request,
            'You cannot delete this blog.'
        )

        return redirect('home')

    if request.method == 'POST':

        blog.delete()

        messages.success(
            request,
            'Blog deleted successfully!'
        )

    return redirect('home')


# My Blogs
@login_required
def my_blogs(request):

    blogs = Blog.objects.filter(
        author=request.user
    )

    return render(
        request,
        'blog/my_blogs.html',
        {
            'blogs': blogs
        }
    )


# Add Comment
@login_required
def add_comment(request, blog_id):

    blog = get_object_or_404(
        Blog,
        id=blog_id
    )

    if request.method == 'POST':

        text = request.POST.get('text')

        if text:

            Comment.objects.create(
                blog=blog,
                author=request.user,
                text=text
            )

            messages.success(
                request,
                'Comment added!'
            )

    return redirect(
        'blog_detail',
        blog_id=blog.id
    )