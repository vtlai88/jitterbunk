from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from django.db.models import Q

from .models import User, Bunk

# Create your views here.

def index(request):
    # displays all bunks in the order of the lastest bunks
    # -time means reverse: so lastest to oldest
    all_bunks = Bunk.objects.all().order_by('-time')

    user_list = User.objects.all()

    context = {
        "bunks": all_bunks, 
        "users": user_list
    }
  
    return render(request, 'jitterbunk/index.html', context)

def personalBunkFeed(request, user_id):
    #return HttpResponse("You are at the Personal Bunk Feed, which displays bunks for a specific user: %s" % username)
 
    user = get_object_or_404(User, pk=user_id)
    bunks_user_list = Bunk.objects.filter(Q(from_user_id = user_id) | Q(to_user_id = user_id))
    
    context = {
        'bunks': bunks_user_list,
        'user_id': user_id,
        'photo': user.photo,
        #'username': User.objects.filter(id = user_id)[0].username
        'username': user.username
    }

    return render(request, 'jitterbunk/personal.html', context)

def makeBunk(request, user_id):
    if request.method == "GET":
        context = {
            'profile_pic': (get_object_or_404(User, pk=user_id)).photo,
            'sender': (get_object_or_404(User, pk=user_id)),
            'username': (get_object_or_404(User, pk=user_id)).username,

            #this removes the sender from the list of users to bunk
            'targets': User.objects.all().filter(~Q(pk=user_id))
        }
        return render(request, 'jitterbunk/makeBunk.html', context)

    elif request.method == "POST":
        user = get_object_or_404(User,pk=user_id)
        myBunk = Bunk(from_user=user, to_user=(get_object_or_404(User,username=request.POST['target'])))
        myBunk.save()
        return HttpResponseRedirect('/')