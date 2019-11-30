from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.
from .models import *

def login(request):

    data={"username": 'admin', "password": "123.asd"}
    username = request.POST.get("username")
    password = request.POST.get('password')
    print(username, password)
    user = User.objects.filter(username=username).first()
    if user:
        if username != user.username:
            return JsonResponse({"msg": "用户名不存在", "flag": 1})
        if password != user.password:
            return JsonResponse({"msg": "密码错误", "flag": 2})


        request.session["loginflag"]={"username": user.username, "userid":user.id}

        return JsonResponse({"msg": "登陆成功", "flag": 3})