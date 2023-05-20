from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
import json
from django.http import JsonResponse, HttpResponseNotAllowed
from django.views.decorators.csrf import csrf_exempt
from .utils import create_saletransaction, read_saletransaction, update_saletransaction, delete_saletransaction


@csrf_exempt
def saletransaction_create(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        return JsonResponse({'message': 'saletransaction created'})
    else:
        return HttpResponseNotAllowed(['POST'])


@csrf_exempt
def saletransaction_read(request):
    if request.method == 'GET':
        saletransaction_id = request.GET.get('transaction_id')
        saletransaction = read_saletransaction(saletransaction_id)
        return JsonResponse(saletransaction, safe=False)


@csrf_exempt
def saletransaction_update(request):
    if request.method == 'PUT':
        data = json.loads(request.body)
        update_saletransaction(data)
        return JsonResponse({'message': 'saletransaction updated'})
    else:
        return HttpResponseNotAllowed(['POST'])


@csrf_exempt
def saletransaction_delete(request):
    if request.method == 'DELETE':
        data = json.loads(request.body)
        delete_saletransaction(data['transaction_id'])
        return JsonResponse({'message': 'sale transaction deleted'}, safe=False)
