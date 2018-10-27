from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from Iphone.models import User


def index(request):
    username = request.COOKIES.get('username')
    return render(request,'index.html',context={'username':username})


def test(request):
    return HttpResponse('测试数据，反向解析操作')

# 注册
def register(request):
    if request.method == 'GET':
        return render(request,'register.html')
    elif request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        tel = request.POST.get('tel')
        print(username,password,tel)

        user = User()
        user.username = username
        user.password = password
        user.tel = tel
        user.save()

        response = redirect('Iphone:index')

        response.set_cookie('username',username)

        return response

# 登录
def login(request):
    if request.method == 'GET':
        return render(request,'login.html')
    elif request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username,password)

        users = User.objects.filter(username=username,password=password)
        if users.count():
            user = users.first()

            response = redirect('Iphone:index')

            response.set_cookie('username',user.username)

            return response
        else:
            return HttpResponse('账号或密码错误！！')


def logout(request):

    response = redirect('Iphone:index')

    response.delete_cookie('username')

    return response


def cart(request):
    username = request.COOKIES.get('username')
    return render(request, 'cart.html', context={'username': username})
