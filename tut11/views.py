from django.shortcuts import render,redirect
from django.http import HttpResponse
from tut11.models import Physic, PhysicComment, Chemistry, ChemistryComment, Math, MathComment
from django.contrib import messages
from tut11.templatetags import extras


# Create your views here.
def tut11Home(request):
    user = request.user
    user2 = str(user)
    if user2 == 'AnonymousUser':
        return render(request,'error.html')
    elif user.last_name == "11":
        return render(request,'tut11/tut11Home.html')
    else:
        return render(request,'error.html')
        

# physic tutorials and comments
def physic(request,slug):
    cur_vid = Physic.objects.get(slug=slug)
    all_series = Physic.objects.all()
    comment = PhysicComment.objects.filter(tut=cur_vid, parent=None)
    replies = PhysicComment.objects.filter(tut=cur_vid).exclude(parent=None)

    repDict = {}
    for reply in replies:
        if reply.parent.sr not in repDict:
            repDict[reply.parent.sr] = [reply]
        else:
            repDict[reply.parent.sr].append(reply)

    param = {'cur_vid':cur_vid, 'all_series':all_series, 'comments':comment, 'replies':repDict}
    user = request.user
    user2 = str(user)
    if user2 == 'AnonymousUser':
        return render(request,'error.html')
    elif user.last_name == "11":
        return render(request,'tut11/physic.html', param)
    else:
        return render(request,'error.html')
    
def physicComment(request):
    if request.method == 'POST':
        comment = request.POST['content']
        user = request.user
        cur_vid_num = request.POST['cur_vid_num']
        cur_vid = Physic.objects.get(sr=cur_vid_num)
        parentSno = request.POST['parentSno']

        if parentSno == "":
            physiccomment = PhysicComment(comment=comment, user=user, tut=cur_vid) 
            physiccomment.save()
            messages.success(request, 'your comment has been posted successfully.....')
            return redirect(f'/tut11/physic-{cur_vid.slug}')
        
        else:
            parent = PhysicComment.objects.get(sr=parentSno)
            physiccomment = PhysicComment(comment=comment, user=user, tut=cur_vid, parent=parent) 
            physiccomment.save()
            messages.success(request, 'your reply has been posted successfully.....')
            return redirect(f'/tut11/physic-{cur_vid.slug}')
    return render(request,'error.html')


# Chemistry tutorials and comments
def chemistry(request, slug):
    cur_vid = Chemistry.objects.get(slug=slug)
    all_series = Chemistry.objects.all()
    comment = ChemistryComment.objects.filter(tut=cur_vid, parent=None)
    replies = ChemistryComment.objects.filter(tut=cur_vid).exclude(parent=None)
    repDict = {}
    for reply in replies:
        if reply.parent.sr not in repDict:
            repDict[reply.parent.sr] = [reply]
        else:
            repDict[reply.parent.sr].append(reply)

    param = {'cur_vid':cur_vid, 'all_series':all_series, 'comments':comment, 'replies':repDict}
    user = request.user
    user2 = str(user)
    if user2 == 'AnonymousUser':
        return render(request,'error.html')
    elif user.last_name == "11":
        return render(request,'tut11/chemistry.html', param)
    else:
        return render(request,'error.html')
    
def chemistryComment(request):
    if request.method == 'POST':
        comment = request.POST['content']
        user = request.user
        cur_vid_num = request.POST['cur_vid_num']
        cur_vid = Chemistry.objects.get(sr=cur_vid_num)
        parentSno = request.POST['parentSno']

        if parentSno == "":
            chemistrycomment = ChemistryComment(comment=comment, user=user, tut=cur_vid) 
            chemistrycomment.save()
            messages.success(request, 'your comment has been posted successfully.....')
            return redirect(f'/tut11/chemistry-{cur_vid.slug}')
        
        else:
            parent = ChemistryComment.objects.get(sr=parentSno)
            chemistrycomment = ChemistryComment(comment=comment, user=user, tut=cur_vid, parent=parent) 
            chemistrycomment.save()
            messages.success(request, 'your reply has been posted successfully.....')
            return redirect(f'/tut11/chemistry-{cur_vid.slug}')    
    return render(request,'error.html')


# Maths tutorials and comments
def math(request,slug):
    cur_vid = Math.objects.get(slug=slug)
    all_series = Math.objects.all()
    comment = MathComment.objects.filter(tut=cur_vid, parent=None)
    replies = MathComment.objects.filter(tut=cur_vid).exclude(parent=None)
    repDict = {}
    for reply in replies:
        if reply.parent.sr not in repDict:
            repDict[reply.parent.sr] = [reply]
        else:
            repDict[reply.parent.sr].append(reply)


    param = {'cur_vid':cur_vid, 'all_series':all_series, 'comments':comment, 'replies':repDict}
    user = request.user
    user2 = str(user)
    if user2 == 'AnonymousUser':
        return render(request,'error.html')
    elif user.last_name == "11":
        return render(request, 'tut11/math.html', param)
    else:
        return render(request,'error.html')

def mathComment(request):
    if request.method == 'POST':
        comment = request.POST['content']
        user = request.user
        cur_vid_num = request.POST['cur_vid_num']
        cur_vid = Math.objects.get(sr=cur_vid_num)
        parentSno = request.POST['parentSno']

        if parentSno == "":
            mathcomment = MathComment(comment=comment, user=user, tut=cur_vid) 
            mathcomment.save()
            messages.success(request, 'your comment has been posted successfully.....')
            return redirect(f'/tut11/math-{cur_vid.slug}')
        
        else:
            parent = MathComment.objects.get(sr=parentSno)
            mathcomment = MathComment(comment=comment, user=user, tut=cur_vid, parent=parent) 
            mathcomment.save()
            messages.success(request, 'your reply has been posted successfully.....')
            return redirect(f'/tut11/math-{cur_vid.slug}')    
    return render(request,'error.html')

# error page
def errorfunc(request,slug):
    return render(request, 'error.html')    