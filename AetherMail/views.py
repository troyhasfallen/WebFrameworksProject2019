from django.shortcuts import render
from .models import Message
from .forms import MsgForm
from django.shortcuts import redirect, get_object_or_404
from django.utils import timezone
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic

# Create your views here.




def inbox_list(request):
    usn = request.user.username
    messages = Message.objects.filter(to_user=usn, received_trash_status='N').order_by('-timestamp')
    return render(request, 'AetherMail/inbox.html', {'messages':messages})


def sent_list(request):
    usn = request.user.username
    messages = Message.objects.filter(from_user=usn, sent_trash_status='N').order_by('-timestamp')
    return render(request, 'AetherMail/sent.html', {'messages':messages})



def read_sent_msg(request, pk):
    message = get_object_or_404(Message, pk=pk)
    
    return render(request, 'AetherMail/read_sent_msg.html', {'msg': message})

def delete_from_sent(request, pk):
    message = get_object_or_404(Message, pk=pk)
    message.sent_trash_status = "Y"
    message.save()
    return redirect('sent')

def read_inbox_msg(request, pk):
    message = get_object_or_404(Message, pk=pk)
    message.read_status = 'R'
    message.save()
    return render(request, 'AetherMail/read_inbox_msg.html', {'msg': message})

def delete_from_inbox(request, pk):
    message = get_object_or_404(Message, pk=pk)
    message.received_trash_status = "Y"
    message.save()
    return redirect('inbox')


def trash(request):
    usn = request.user.username
    messages1 = Message.objects.filter(from_user=usn, sent_trash_status='Y')
    messages2 = Message.objects.filter(to_user=usn, received_trash_status='Y')
    messages = messages1.union(messages2).order_by('-timestamp')
    return render(request, 'AetherMail/trash.html', {'messages':messages})
    
def read_trash_msg(request, pk):
    message = get_object_or_404(Message, pk=pk)
    usn = request.user.username
    if message.to_user == usn:
        message.read_status = 'R'
    message.save()
    return render(request, 'AetherMail/read_trash_msg.html', {'msg': message})




def compose(request):
    if request.method == 'POST':
        form = MsgForm(request.POST)
        if form.is_valid():
            msg = form.save(commit=False)
            #post.author = request.user
            msg.from_user = request.user.username
            msg.timestamp = timezone.now()
            msg.received_trash_status = "N"
            msg.sent_trash_status = "N"
            msg.read_status = "U"
            msg.save()
            return redirect('inbox')    
    else:
        form = MsgForm()
    
    return render(request, 'AetherMail/compose.html', {'form':form})

class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'