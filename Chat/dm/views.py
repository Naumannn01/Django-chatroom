from django.shortcuts import render,redirect
from dm.models import Room,Message
from django.http import HttpResponse,JsonResponse
# from django.core.mail import send_mail
# from.utils import send_email_to_client
def home(request):
    # send_mail(
    #     'Testing mail',
    #     'Hello this is my first django mail',
    #     'nomishaikh2002@gmail.com',
    #     ['shaikhnomu2002@gmail.com'],
    #     fail_silently=False
    # )
    return render(request,'home.html')

def send_email(request):
    send_email_to_client()
    return redirect('/')

def room(request,room):
    username=request.GET.get('username')
    room_details=Room.objects.get(name=room)
    context={'username':username,'room':room,'room_details':room_details}
    return render(request,'room.html',context)

def checkview(request):
    room=request.POST['room_name']
    username=request.POST['username']
        
    if Room.objects.filter(name=room).exists():
        return redirect('/'+room+'/?username='+username)
    else:
        new_room=Room.objects.create(name=room)
        new_room.save()
        return redirect('/'+room+'/?username='+username)

def send(request):
    message=request.POST['message']
    username=request.POST['username']
    room_id=request.POST['room_id']

    new_message=Message.objects.create(value=message,user=username,room=room_id)
    new_message.save()

    return HttpResponse('Message Send Successfully') 

def getMessages(request,room):
    room_details=Room.objects.get(name=room)
    messages=Message.objects.filter(room=room_details.id)
    return JsonResponse({"messages":list(messages.values())})

