from django.shortcuts import render

# Create your views here.
# products/views.py
from django.http import JsonResponse, HttpResponseNotAllowed
from .utils import create_product, read_product, update_product, delete_product
import json
from django.views.decorators.csrf import csrf_exempt

# product api view


@csrf_exempt
def product_create(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        create_product(data)
        return JsonResponse({'message': 'Product created'})
    else:
        return HttpResponseNotAllowed(['POST'])


def product_detail(request, product_id):
    if request.method == 'GET':
        product = read_product(product_id)
        return JsonResponse(product, safe=False)
    elif request.method == 'PUT':
        data = json.loads(request.body)
        update_product(data)
        return JsonResponse({'message': 'Product updated'})
    elif request.method == 'DELETE':
        delete_product(product_id)
        return JsonResponse({'message': 'Product deleted'})
