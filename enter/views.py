from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import exit

class exitListView(ListView):
    model = exit

class exitCreateView(CreateView):
    model = exit
    fields = ['title','deadline']
    success_url = reverse_lazy('exit_list')

class exitUpdateView(UpdateView):
    model = exit
    fields = ['title', 'deadline']
    success_url = reverse_lazy('exit_list')

class exitDeleteView(DeleteView):
    model = exit
    success_url = reverse_lazy('exit_list') 

