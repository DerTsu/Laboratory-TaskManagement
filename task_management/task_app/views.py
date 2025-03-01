from django.shortcuts import render
from .models import Task
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django import forms

class TaskList(ListView):
    model = Task

class CreateTask(SuccessMessageMixin, CreateView): 
    model = Task 
    form = Task 
    fields = "__all__" 
    success_message = 'Task created succesfully!' 
    def get_success_url(self):        
        return reverse('read')

class TaskDetail(DetailView): 
    model = Task 

class UpdateTask(SuccessMessageMixin, UpdateView): 
    model = Task
    form = Task 
    fields = "__all__"
    success_message = 'Task updated succesfully !'
    def get_success_url(self):               
        return reverse('read') 

class DeleteTask(SuccessMessageMixin, DeleteView): 
    model = Task 
    form = Task
    fields = "__all__"     
    def get_success_url(self): 
        success_message = 'Task deleted succesfully !' 
        messages.success (self.request, (success_message))       
        return reverse('read')