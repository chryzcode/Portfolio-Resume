from django.shortcuts import render
from .models import Message
from .forms import MessageForm
from django.views.generic import  CreateView
from django.urls import reverse, reverse_lazy
# Create your views here.

class TheView(CreateView):
    model = Message
    form_class = MessageForm
    template_name = 'resume.html'
    success_url = reverse_lazy('the_view')

