from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Posts
from django.shortcuts import get_object_or_404


# ✅ SIGNUP
def signup(request):
    if request.method == 'POST':
        name = request.POST.get('uname')
        email = request.POST.get('uemail')
        password = request.POST.get('upassword')

        # 🔒 Check if user already exists
        if User.objects.filter(username=name).exists():
            messages.error(request, "Username already exists")
            return redirect('signup-page')

        # 🔒 Create user
        User.objects.create_user(
            username=name,
            email=email,
            password=password
        )

        messages.success(request, "Account created successfully")
        return redirect('login-page')

    return render(request, 'blog/signup.html')


# ✅ LOGIN
def loginn(request):
    if request.method == 'POST':
        name = request.POST.get('uname')
        password = request.POST.get('upassword')

        user = authenticate(request, username=name, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "Login successful")
            return redirect('home-page')
        else:
            messages.error(request, "Invalid username or password")
            return redirect('login-page')

    return render(request, 'blog/login.html')


# ✅ HOME
@login_required(login_url='login-page')
def home(request):
    posts = Posts.objects.all().order_by('-id')  # latest first
    return render(request, "blog/home.html", {'posts': posts})


# ✅ MY POSTS
@login_required(login_url='login-page')
def myPosts(request):
    posts = Posts.objects.filter(author=request.user).order_by('-id')
    return render(request, "blog/mypost.html", {'posts': posts})


# ✅ NEW POST
@login_required(login_url='login-page')
def newPost(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')

        Posts.objects.create(
            title=title,
            content=content,
            author=request.user
        )

        messages.success(request, "Post created successfully")
        return redirect('home-page')

    return render(request, 'blog/newpost.html')


# ✅ LOGOUT
def signout(request):
    logout(request)
    messages.success(request, "Logged out successfully")
    return redirect('login-page')



@login_required(login_url='login-page')
def delete_post(request, id):
    post = get_object_or_404(Posts, id=id)

    if post.author != request.user:
        messages.error(request, "Not allowed")
        return redirect('home-page')

    if request.method == 'POST':
        post.delete()
        messages.success(request, "Deleted successfully")
        return redirect('home-page')