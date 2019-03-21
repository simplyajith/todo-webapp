from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import TodoItem
# from templates
# Create your views here.

'''
Login to shell using python manage.py shell command and create objects for TodoItems as below:
-----------------------------------------------------------------------------------------------
>>> from todo.models import TodoItem
>>> TodoItem
<class 'todo.models.TodoItem'>
>>> TodoItem.objects.all()
<QuerySet []>
>>> a = TodoItem()
>>> a.content = 'Permanent Todo Item-A'
>>> b = TodoItem()
>>> b.content = 'Permanent Todo Item-B'
>>> TodoItem.objects.all()
<QuerySet []>
>>> a
<TodoItem: TodoItem object (None)>
>>> a.save()
>>> a
<TodoItem: TodoItem object (1)>
>>> b.save()
>>> TodoItem.objects.all()
<QuerySet [<TodoItem: TodoItem object (1)>, <TodoItem: TodoItem object (2)>]>
>>> all_todo_items = TodoItem.objects.all()
>>> all_todo_items[0].content
'Permanent Todo Item-A'
>>> all_todo_items[0].id
1
'''
def todoView(request):
    all_todo_items = TodoItem.objects.all()
    return render(request,'todo.html',{'all_items': all_todo_items})

def addTodo(request):
    # create a new to-do all items
    # save
    # re-direct the browser to to-do
    c = request.POST['content']
    new_item = TodoItem()
    new_item.content = c
    new_item.save()
    return HttpResponseRedirect('/todo/')

def deleteTodo(request,todo_id):
    # Get the to-do id from url
    # delete the Todo item with the id given
    # re-direct the browser to to-do
    todo_items_delete = TodoItem.objects.get(id = todo_id)
    todo_items_delete.delete()
    return HttpResponseRedirect('/todo/')

