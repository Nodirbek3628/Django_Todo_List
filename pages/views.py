from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from uuid import uuid4
# Create your views here.

task_list = []

def add_task(request: HttpRequest) -> HttpResponse:
    if request.method == 'GET':
        return render(request=request,template_name='add.html')
    elif request.method == 'POST':
      form = request.POST

      title = form.get('title')
      deadline = form.get('deadline')
      description = form.get('description')
      priority = form.get('priority')
      status = form.get('status')

   # validition 

    if title in '':
       return HttpResponse('title uniddingz',status=400)
    elif deadline in '':
       return HttpResponse('deadline unitdingz',status=400)
    
    elif description  in '':
       return HttpResponse('description unitdngiz',status=400)
    
    elif priority not in ['low','medium','high']:
       return HttpResponse('priority belgilang',status=400)
    
    elif status not in ['todo','in-progress','done']:
       return HttpResponse('status belgilang',status=400)
    
    else:
       new_task = {
        'id':(uuid4()),
        'title':title,
        'deadline':deadline,
        'description':description,
        'priority':priority,
        'status':status
        }
       task_list.append(new_task)

       return HttpResponse(task_list)
    
       
    