import json
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from api.models import TaskList
from api.serializers import TaskListSerializer, TaskListSerializer2, TaskSerializer
from django.views import View

@csrf_exempt
def all_task_list(request):
    print(request.method)
    if request.method == 'GET':
        tasklist = TaskList.objects.all()
        serializer = TaskListSerializer2(tasklist, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        body = json.loads(request.body)
        serializer = TaskListSerializer2(data=body)
        if serializer.is_valid():
            #create function from serializer
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors)
    return JsonResponse({'error': 'bad request'})

@csrf_exempt
def task_detail(request, pk):
    try:
            task_detail = TaskList.objects.get(id=pk)
    except TaskList.DoesNotExist as e:
        return JsonResponse({'error': str(e)})
    if request.method == 'GET':
        serializer = TaskListSerializer(task_detail)
        return JsonResponse(serializer.data)
    elif request.method == 'PUT':
        body = json.loads(request.body)
        serializer = TaskListSerializer(instance=task_detail, data=body)
        if serializer.is_valid():
            #update function from serializer
            serializer.save()
        return JsonResponse(task_detail.to_json())
    elif request.method == 'DELETE':
        task_detail.delete()
        return JsonResponse({})
    return JsonResponse({'error': 'bad request'})

def id_task_list(request, pk):
    try:
        task_detail = TaskList.objects.get(id=pk)
    except TaskList.DoesNotExist as e:
        error = {
            'error': str(e)
        }
        return JsonResponse(error, safe=False)

    products = task_detail.task_set.all()
    serializer = TaskSerializer(products, many=True)
    return JsonResponse(serializer.data, safe=False)


# Create your views here.
