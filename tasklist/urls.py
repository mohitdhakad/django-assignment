from django.urls import include, path
from . import views
urlpatterns = [
        path("", views.tasklist, name='tasklist'),
        path("form/", views.form, name='form'),
        # path("home/<int:id>", views.tasklistView, name="tasklistview"),
        # path("basic-form-elements/", views.form, name='form'),

]
