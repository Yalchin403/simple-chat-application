from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from .models import Message
from django.http import JsonResponse
from django.http import HttpResponse



def index(request):
    return render(request, 'chat/index.html')
    
def room(request, room_name):
    if request.user.is_authenticated:
        return render(request, 'chat/room.html', {
            'room_name': room_name

        })
    return HttpResponse("You are not logged in")

def fetch_messages(request):
    if request.user.is_authenticated:
        room_name = request.GET.get('room_name', None)
        messages = Message.objects.filter(room=room_name)
        str_messages = ''
        for message in messages:
            str_messages = str_messages + message.msg_content +"\n"
        data = {
            'fetched_messages': str_messages
        }
        return JsonResponse(data)
    return HttpResponse("You are not logged in")