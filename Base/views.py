from multiprocessing import context
from django.contrib import messages
from django.shortcuts import render,redirect
from .forms import GetForm,UserCreationForm
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.contrib.auth import login,authenticate,logout
from .models import Get
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url='welcome/')
def home(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    topics = Get.objects.filter(activity__icontains=q)[:9]
    host = Get.objects.filter(host = request.user )[:9]
    
    if  request.method == 'GET':
        submit = True
    else :
        submit = False

    context = {
        'topics':host,
        'topic':topics,
        'submit':submit,
    }
    return render(request,'Base/home.html',context)

def viewActivity(request,pk):
    view = Get.objects.get(id=pk)
    host = Get.objects.filter(host  = request.user) [:3]

    if request.method == 'POST':
        view.delete()
        return redirect('home')
        
    context = {
        'topics':host,
        'view':view,
    }
    return render(request,'Base/view_activity.html',context)

def welcome(request):
    return render(request,"Base/index.html")

def search(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    topics = Get.objects.filter(Q(activity__icontains=q) | 
    Q(description__icontains=q))[:900000000000000000]

    return render(request, 'Base/search.html',{'topics':topics})


def delete(request,pk):
    get = Get.objects.get(id=pk)

    if request.method == 'POST':
        get.delete()
        return redirect('home')

    return render(request,'Base/delete.html',{'get':get})

def addActivity(request):
    form = GetForm
    get = Get.objects.all()
    
    if request.method == 'POST':
        form = GetForm(request.POST)

        Get.objects.create(
            host = request.user,
            activity = request.POST.get('activity'),
            description = request.POST.get('description')
        )
        return redirect('home')

        
        # if form.is_valid():
        #     form.save()
        #     return HttpResponseRedirect('/')
    
    context = {
        'form':form,
        'get':get
    }

    return render(request,'Base/add_activity.html',context)

def editActivity(request,pk):
    edit = Get.objects.get(id=pk)
    form = GetForm(instance=edit)

    if request.method == 'POST':
        form = GetForm(request.POST ,instance=edit)
        if form.is_valid():
            form.save()
            return redirect('home')

    return render(request , 'Base/edit.html',{'form':form})

def register(request):
    page = 'register'
    form = UserCreationForm
    name = ['Username','Password','Re-type Password']
    #user = User

    context = {
        'form':form,
        'label':name,
        'page':page,
        #'user':user
    }

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            User = form.save(commit=False)
            User.username = User.username.lower()
            User.save()
            login(request,User)
            
            return redirect('home')
    
    return render(request,'Base/login_register.html',context)

def loginUser(request):
    form = UserCreationForm

    if request.user.is_authenticated :
        return redirect('home')

    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'User does not exist')

        user = authenticate(request,username=username,password=password)

        if user is not None:
            login(request,user)
            return redirect('home')
  

    context ={
        'form':form,
        # 'messages':messages
    }

    return render(request,'Base/login_register.html',context)

def logoutUser(request):
    logout(request)
    return redirect('home')

def hostActivity(request):
    activity = Get.objects.get(name='host')

    return render(request,'Base/index.html',{'activity':activity})