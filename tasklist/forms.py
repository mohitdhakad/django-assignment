from django import forms
from tasklist.models import addtask


class TasksForm(forms.ModelForm):
    class Meta:
        model = addtask
        fields = ['name', 'time', 'details','status', ]



class GeeksForm(forms.Form):
    name = forms.CharField(label='Task name')    
    time = forms.DateTimeField()
    details = forms.CharField(label='Details') 
    status = forms.BooleanField()

