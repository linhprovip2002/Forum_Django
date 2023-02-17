from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.template import loader

# Create your views here.
def HomePage(request):
    return render(request, 'home.html')
def SignupPage(request):
    if request.method == 'POST':
        print(request.POST)
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        # chưa xử lý trường hợp password1 != password2
        # chưa xử lý trường hợp username đã tồn tại
        print(username,email,password1,password2)
        my_user = User.objects.create_user(username,email,password1)
        my_user.save()
        return redirect('login')
    return render(request, 'auth/register.html') 
def LoginPage(request):
    if request.method == 'POST':
        print(request.POST)
        username = request.POST.get('username')
        password = request.POST.get('pass')
        user = authenticate(request,username=username,password=password)
        print(user)

        if user:
            login(request,user)
            print('Đăng nhập thành công')
            template = loader.get_template('home.html')
            Array = User.objects.all()
            print(Array.values)
            context = {
                'user': user,
                'Array': Array,
            }
            return HttpResponse(template.render(context, request))
      
        else:
            print('Đăng nhập thất bại')
            return HttpResponse('Đăng nhập thất bại')
    else:
        return render(request, 'auth/login.html')
def LogoutPage(request):
    logout(request)
    return redirect('login')    