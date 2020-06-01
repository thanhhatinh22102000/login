from django.shortcuts import render,HttpResponse
from django.views import View
from django.contrib.auth import authenticate,login
from .models import Post



class IndexClass(View):
    def get(self,request):
        return render(request,'user/loichao.html')

class LoginClass(View):
    def get(self,request):
        return render(request,'user/login.html')

    def post(self,request):
        username=request.POST.get('username')
        password=request.POST.get('matkhau')
        my_user=authenticate(username=username,password=password)
        if my_user is None:
            return HttpResponse('user không tồn tại')
        else:
            login(request,my_user)
            return render(request,'user/success.html')


def View(request):
    list_info=Post.objects.all()
    context={'list':list_info}
    return render(request,'user/detail.html',context)
