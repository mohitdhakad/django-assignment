from django.shortcuts import render,redirect
from django.template import Template
from django.shortcuts import get_object_or_404
from tasklist.models import addtask
from tasklist.forms import TasksForm,GeeksForm
from tasklist.filters import datefilter
# Create your views here.



def form(request):
    if request.method == "POST":
        context = {}
        context['form'] = GeeksForm()
        form = TasksForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/',context)
        else:
            return render(request,"form.html",{'form':form})
    else:
        form = TasksForm()

        return render(request, "form.html",{'form':form})


def tasklist(request):
    filter = datefilter(request.GET, queryset=addtask.objects.all())
    return render(request, "home.html",{'task_posted': addtask.objects.all(),'filter': filter})



# def tasklist(request):
#     return render(request, "home.html", {'task_posted': addtask.objects.all()})


# def tasklistView(request, id):
#     if request.method == "POST":

#         new_task = addtask(task_name=request.POST['Input'],
#                       time=request.POST['Input1'], details=request.POST['Input2'],status=request.POST['Input3'])
#         new_task.save()
#         return redirect('')
#     else:
#         return render(request, "form.html", {'task_posted': addtask.objects.all()})




# def taskView(request, id):
#     jobs = job.objects.get(pk=id)
#     if request.method == "POST":
#         form = TmsForm(request.POST, request.FILES, instance=jobs)
#         if form.is_valid():
#             form.save()
#             return redirect('/home.html')
#         else:
#             print(form.errors)
#             return redirect('/home.html/'+str(id))
#     else:
#         return render(request, "form.html", {'jobs': jobs})