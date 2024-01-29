from typing import Any
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic.base import TemplateView, RedirectView
from django.views import View


from .models import Task

# Create your views here.
# adding data to database
class AddTask(TemplateView):
    def post(self,request):
        task = request.POST['task'] #return the desc of all the form value {'task':['buy tv']}
        Task.objects.create(task=task)
        return redirect('home')


class Mark_as_done(View):
    def get(self, request, pk):
        task = get_object_or_404(Task, pk=pk) #return all the fields of perticular pk
        task.is_completed = True
        task.save()
        return redirect('home')


class Mark_as_undone(View):
    def get(self, request, pk):
        task = get_object_or_404(Task, pk=pk) #return all the fields of perticular pk
        task.is_completed = False
        task.save()
        return redirect('home')


class Edit_task(View):
    def get(self, request, pk):
        get_task = Task.objects.get(pk=pk)
        context = {
            'get_task': get_task,
        }
        return render(request, 'edit_task.html', context)
    
    def post(self,request,pk):
        get_task = Task.objects.get(pk=pk)
        new_task = request.POST['task']
        get_task.task = new_task 
        get_task.save()
        return redirect('home')


class Delete_task(RedirectView):
    url = '/'
    def get_redirect_url(self, *args, **kwargs):
        del_id = kwargs['pk']
        Task.objects.get(pk=del_id).delete()
        return super().get_redirect_url(*args, **kwargs)


