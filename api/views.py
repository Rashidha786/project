from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from api.models import Dummy
from api.serializers import RegisterS


# Create your views here.
@csrf_exempt
def register_list(request):
    if request.method == 'GET':
        registers = Dummy.objects.all()
        serializer = RegisterS(registers, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        print(data)
        serializer = RegisterS(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)






@csrf_exempt
def register_detail(request, pk):

    try:
        registers = Dummy.objects.get(pk=pk)
    except Dummy.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = RegisterS(registers)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = RegisterS(registers, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        registers.delete()
        return HttpResponse(status=204)

