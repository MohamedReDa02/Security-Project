from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import CustomUserCreationForm , CustomLoginForm  

# users/views.py

from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm

def signup_view(request):
    print("here")
    if request.method == 'POST':
        print("here")
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            print("here")
            return redirect('login')  # Redirect to login page after successful signup
    else:
        form = CustomUserCreationForm()
    return render(request, 'users/signup.html', {'form': form})


import requests
from django.conf import settings
from django.urls import reverse
from django.contrib.auth import authenticate, login
from .forms import CustomLoginForm
from .models import CustomUser, Conversation
def login_view(request):
    print("here")
    if request.method == 'POST':
        print("here")
        form = CustomLoginForm(request, data=request.POST)
        recaptcha_response = request.POST.get('g-recaptcha-response')
        data = {
            'secret': settings.RECAPTCHA_SECRET_KEY,
            'response': recaptcha_response
        }
        r = requests.post('https://www.google.com/recaptcha/api/siteverify', data=data)
        result = r.json()

        if form.is_valid() and result.get('success'):
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            print(username)
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('success')  
            else:
                
                pass
        else:
            
            pass
    else:
        form = CustomLoginForm()
    return render(request, 'users/login.html', {'form': form})

# Success view
def success_view(request):
    return render(request, 'users/success.html')

from .models import CustomUser  

from django.shortcuts import render
from .models import CustomUser, Conversation , Message

def user_list(request):
    users = CustomUser.objects.all()
    conversations = {conv.participants.exclude(id=request.user.id).first().id: conv.id
                     for conv in Conversation.objects.filter(participants=request.user)}

    for user in users:
        if request.user != user:
            if user.id in conversations:
                user.conversation_url = reverse('view_conversation', args=[conversations[user.id]])
                user.conversation_label = 'View Conversation'
            else:
                user.conversation_url = reverse('start_conversation', args=[user.id])
                user.conversation_label = 'Start Conversation'
        else:
            user.conversation_url = None
            user.conversation_label = None

    return render(request, 'messages/users_list.html', {'users': users})

from django.shortcuts import redirect


from django.shortcuts import redirect, get_object_or_404
from .models import CustomUser, Conversation 
def start_conversation(request, user_id):
    if request.method == 'POST':
        other_user = get_object_or_404(CustomUser, pk=user_id)
        conversation = Conversation.objects.create()
        conversation.participants.add(request.user, other_user)
        return redirect('view_conversation', conversation_id=conversation.id)
    return redirect('user_list')  # Replace with your user list view


from django.shortcuts import render, get_object_or_404, redirect
from .models import Conversation

def view_conversation(request, conversation_id):
    conversation = get_object_or_404(Conversation, pk=conversation_id)
    messages = conversation.message_set.all()
    other_user = conversation.participants.exclude(id=request.user.id).first()
    # Decrypt each message
    decrypted_messages = [{'sender': msg.sender, 'content': msg.content, 'timestamp': msg.timestamp} for msg in messages]
    return render(request, 'messages/conversation_detail.html', {'conversation': conversation, 'messages': decrypted_messages, 'other_user': other_user})

def send_message(request, conversation_id):
    if request.method == 'POST':
        conversation = get_object_or_404(Conversation, pk=conversation_id)
        message_content = request.POST.get('message_content')
        message = Message(sender=request.user, conversation=conversation)
        message.content = message_content  # Use the property setter
        message.save()
        return redirect('view_conversation', conversation_id=conversation.id)
    return redirect('user_list')  # Replace with your user list view

