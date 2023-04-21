from django.shortcuts import render,redirect
from .models import *

def index(request):
    allBlogs = Blog.objects.all().order_by('-posted')
    try:
        active_user = Blogger.objects.get(email = request.session['email'])
        return render(request,'index.html',{'active':active_user,'all_blogs':allBlogs})
    except:
        return render(request,'index.html',{'all_blogs':allBlogs})

def signup(request):
    if request.method == 'GET':
        return render(request,"signup.html")
    else:
        try:
            Blogger.objects.get(email = request.POST['email'])
            return render(request,'signup.html',{"msg":'email already in use'})
        except:
            if request.POST['password'] == request.POST['cpassword']:
                Blogger.objects.create(
                    name = request.POST['name'],
                    email = request.POST['email'],
                    password = request.POST['password']
                )
                return render(request,'login.html') 
            else:
                return render(request,'signup.html',{"msg":'please enter same password'})
                

def login(request):
    if request.method == 'GET':
        return render(request,"login.html")
    else:
        try:
            user = Blogger.objects.get(email = request.POST['email'])
            if request.POST['password'] == user.password:
                request.session['email'] = user.email
                return redirect('index')
            else:
                return render(request,'login.html',{'msg':'incorrect password'})
        except:
            return render(request,'login.html',{'msg':'Invalid Credential'})
    
def logout(request):
    del request.session['email']
    return redirect('index')

def addpost(request):
    active_user = Blogger.objects.get(email = request.session['email'])
    if request.method == "GET":
        return render(request,'addpost.html',{'active':active_user})
    else:
        try:
            Blog.objects.create(
                title = request.POST['title'],
                desc = request.POST['desc'],
                pic = request.FILES['pic'],
                auther = active_user
            )
            return render(request,'addpost.html',{'msg':"POSTED",'active':active_user})
        except:
            return redirect('addpost')
        
def mypost(request):
    active_user = Blogger.objects.get(email = request.session['email'])
    myblogs = Blog.objects.filter(auther = active_user)
    return render(request,'mypost.html',{'active':active_user,'myblogs':myblogs})

def currentpost(request,pk):
    post = Blog.objects.get(id = pk)
    return render(request,'post.html',{'post':post})

    