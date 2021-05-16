from django.shortcuts import render,redirect
from django.template import Template
from django.shortcuts import get_object_or_404
from tasklist.models import addtask
from tasklist.forms import TasksForm,InputForm
from tasklist.filters import datefilter
# Create your views here.

def tasklist(request):
    filter = datefilter(request.GET, queryset=addtask.objects.all())
    return render(request, "home.html",{'task_posted': addtask.objects.all(),'filter': filter})



def form(request):
    if request.method == "POST":
        context = {}
        context['form'] = InputForm()
        form = TasksForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/',context)
        else:
            return render(request,"form.html",{'form':form})
    else:
        form = TasksForm()

        return render(request, "form.html",{'form':form})




