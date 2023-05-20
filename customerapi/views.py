from django.shortcuts import render
import json
from django.http import JsonResponse, HttpResponseNotAllowed
from django.views.decorators.csrf import csrf_exempt
from .utils import create_customer, read_customer, update_customer, delete_customer


@csrf_exempt
def customer_create(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        return JsonResponse({'message': 'Customer created'})
    else:
        return HttpResponseNotAllowed(['POST'])


@csrf_exempt
def customer_read(request):
    if request.method == 'GET':
        customer_id = request.GET.get('customer_id')
        customer = read_customer(customer_id)
        return JsonResponse(customer, safe=False)


@csrf_exempt
def customer_update(request):
    if request.method == 'PUT':
        data = json.loads(request.body)
        update_customer(data)
        return JsonResponse({'message': 'Customer updated'})
    else:
        return HttpResponseNotAllowed(['POST'])


@csrf_exempt
def customer_delete(request):
    if request.method == 'DELETE':
        data = json.loads(request.body)
        delete_customer(data['customer_id'])
        return JsonResponse({'message': 'Customer deleted'}, safe=False)
