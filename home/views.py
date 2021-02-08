# home views 

from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from home.models import Contact
from tut11.models import Physic, Chemistry, Math


# generic func
def index(request):
    return render(request, 'home/index.html')

def about(request):
    return render(request, 'home/about.html')

def contact(request):
    if request.method == 'POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        Class = request.POST['class']
        section = request.POST['section']
        msg = request.POST['msg']
        contact = Contact(First_Name=fname, Last_Name=lname, Email=email, Class=Class, Section=section, Message=msg)
        contact.save()
        messages.success(request, 'Your Message has been submitted...')
        return redirect('contact')
    return render(request, 'home/contact.html')

def verify(tut,querys):
    for query in querys:
        if query in tut.title.lower():
            return True    
    else:
        return False
def search(request):
    query = request.GET['query']
    if len(query)>50:
        long_query = True
        param = {'long_query':long_query, 'query':query}
        return render(request, 'home/search.html', param)
    else:
        querys = query.split()

    user = request.user
    user2 = str(user)
    if user2 == 'AnonymousUser':
        return render(request,'error.html')
    elif user2 == 'dashadmin':
        return render(request,'error.html')

    # 11th stardard search result
    elif user.last_name == "11":
        all_phy_tut = Physic.objects.all()
        all_chem_tut = Chemistry.objects.all()
        all_math_tut = Math.objects.all()
        phy_res = [tut for tut in all_phy_tut if verify(tut,querys)]
        chem_res = [tut for tut in all_chem_tut if verify(tut,querys)]
        math_res = [tut for tut in all_math_tut if verify(tut,querys)]
        param = {'phy_res':phy_res, 'chem_res':chem_res , 'math_res':math_res}
        return render(request, 'home/search.html', param)
    

# authentication
def handleLogin(request):
    if request.method == 'POST':
        loginusername = request.POST['username']
        loginpassword = request.POST['password']
        user = authenticate(username=loginusername, password=loginpassword)

        if user is not None and user.last_name=='11':
            auth_login(request, user)
            messages.success(request, 'your are successfully loged in...')
            return redirect('home')
        else:
            messages.error(request, 'invalid Credential..')
            return redirect('home')
    return render(request,'error.html')

def handleLogout(request):
    auth_logout(request)
    messages.success(request, 'your are successfully logout...')
    return redirect('home')

