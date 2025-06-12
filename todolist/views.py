import uuid
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.decorators import login_required
from todolist.models import TODOO 
from django.contrib.auth import logout

def signup(req):
    if req.method == 'POST':
        name = req.POST.get('fnm')  # This is just their name
        email = req.POST.get('inp')
        pwd = req.POST.get('pwd')

        if User.objects.filter(email=email).exists():
            return render(req, 'todolist/sign.html', {
                'error': 'Email already exists'
            })

        # ✅ Generate unique username (you can also use uuid or email prefix)
        unique_username = email.split('@')[0] + str(uuid.uuid4())[:5]

        # ✅ Create user (email will be unique, username won't matter to user)
        user = User.objects.create_user(username=unique_username, email=email, password=pwd)
        user.first_name = name  # optional
        user.save()

        # return redirect('/admin')

    return render(req, 'todolist/sign.html')

def login(req):
    if req.method=='POST':
        email=req.POST.get('email')
        psw=req.POST.get('password')
        try:
            user_obj=User.objects.get(email=email)
            # print(user_obj)
            username = user_obj.username 
            user = authenticate(username=username, password=psw)
            print(user)
            if user is not None:
                auth_login(req, user)
                return redirect('/todo/todos/')
             
           
        except User.DoesNotExist:
            print("user nahi exist karta hai ")
               
        
    return render(req , 'todolist/login.html')


@login_required(login_url='/todo/login/')
def todos(req):
    if req.method=='POST':
        task = req.POST.get('task')
        if task:
            TODOO.objects.create(title=task, user=req.user)
            return redirect('/todo/todos/')
        
        elif 'todo_id' in req.POST:
            todo_id=req.POST.get('todo_id')
            if todo_id:
                try:
                 todo = TODOO.objects.get(id=todo_id, user=req.user)
                 todo.delete()
                except TODOO.DoesNotExist:
                 pass
            return redirect('/todo/todos/')    
            


        
    todos=TODOO.objects.filter(user=req.user).order_by('-date')

    return render(req,'todolist/todo.html',{'todos':todos})

def user_logout(req):
    logout(req)
    return redirect('/todo/login/') 

