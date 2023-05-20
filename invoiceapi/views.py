from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
import json
from django.http import JsonResponse, HttpResponseNotAllowed
from django.views.decorators.csrf import csrf_exempt
from .utils import create_invoice, read_invoice, update_invoice, delete_invoice


@csrf_exempt
def invoice_create(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        return JsonResponse({'message': 'invoice created'})
    else:
        return HttpResponseNotAllowed(['POST'])


@csrf_exempt
def invoice_read(request):
    if request.method == 'GET':
        invoice_id = request.GET.get('invoice_id')
        invoice = read_invoice(invoice_id)
        return JsonResponse(invoice, safe=False)


@csrf_exempt
def invoice_update(request):
    if request.method == 'PUT':
        data = json.loads(request.body)
        update_invoice(data)
        return JsonResponse({'message': 'Invoice updated'})
    else:
        return HttpResponseNotAllowed(['POST'])


@csrf_exempt
def invoice_delete(request):
    if request.method == 'DELETE':
        data = json.loads(request.body)
        delete_invoice(data['invoice_id'])
        return JsonResponse({'message': 'invoice deleted'}, safe=False)
