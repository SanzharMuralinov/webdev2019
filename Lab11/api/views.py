from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from api.models import TaskList

@csrf_exempt
def all_task_list(request):
    print(request.method)
    tasklist = TaskList.objects.all()
    json_categories = [c.to_json() for c in tasklist]
    return JsonResponse(json_categories, safe=False)

def task_detail(request, pk):
    try:
            task_detail = TaskList.objects.get(id=pk)
    except TaskList.DoesNotExist as e:
        error = {
            'error': str(e)
        }
        return JsonResponse(error, safe=False)
    return JsonResponse(task_detail.to_json())

def id_task_list(request, pk):
    try:
        task_detail = TaskList.objects.get(id=pk)
    except TaskList.DoesNotExist as e:
        error = {
            'error': str(e)
        }
        return JsonResponse(error, safe=False)

    products = task_detail.task_set.all()
    json_products = [p.to_json() for p in products]
    return JsonResponse(json_products, safe=False)


# Create your views here.
