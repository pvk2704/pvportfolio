from django.shortcuts import render,redirect
from django.contrib import messages,auth
from pvpf.models import Contact,Hire
from django.contrib.auth.models import User

def index(r):                       
    return render(r,'index.html')

def contact(req):
    if req.method=='POST':
        if req.POST['name']and req.POST['email']and req.POST['message']:
            user=Contact()          
            name=req.POST['name']
            email=req.POST['email']
            message=req.POST['message']          
            user.name=name
            user.email=email
            user.message=message        
            user.save()
            messages.info(req,'Your Input is Received ,Thanks !')
            return render(req,'index.html',{})
    else:
       
         return render (req,'index.html',{})

def login(r):
    if r.method=='POST':
 
        username=r.POST['username']
        pwd=r.POST['pwd']    
        
     
        
        obj=auth.authenticate(username=username,password=pwd)
        if obj is not None:
            auth.login(r,obj)        
            messages.info(r,'You Are Logged In !')
            return redirect('education')
        else:
            messages.info(r,'wrong credentials please enter the correct username & password')
            return redirect('login')  
    else: 
     return render(r,'login.html',{})



def register(r):                       
    if r.method=='POST':
    
        username=r.POST['username']
        pwd=r.POST['pwd']
        if User.objects.filter(username=username).exists():
            messages.info(r,'User Already Exists')
            return redirect('register')
        else:
            user=User.objects.create_user(username=username,password=pwd)
            user.save()
            messages.info(r,'User Created Successfully')
            return redirect('login')
    else:
        return render(r,'register.html')
    
def logout(r):                       
     return render(r,'index.html')

def education(r):                       
     return render(r,'education.html')


def hire(req):
    if req.method=='POST':
        if req.POST['jobt']and req.POST['describe']and req.POST['skills']and req.POST['exp']and req.POST['cont']and req.POST['email']:
            user=Hire()          
            jobt=req.POST['jobt']
            describe=req.POST['describe']
            skills=req.POST['skills'] 
            exp=req.POST['exp'] 
            cont=req.POST['cont']
            email=req.POST['email']

            user.jobt=jobt
            user.describe=describe
            user.skills=skills     
            user.exp=exp 
            user.cont=cont 
            user.email=email  
            user.save()
            messages.info(req,'Your Input is Received ,Thanks !')
            return render(req,'hire.html',{})
    else:
       
         return render (req,'hire.html',{})








