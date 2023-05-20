from django.http import JsonResponse
from django.db import connection
import json
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def get_customer_info(request):
    # Extract parameters from request
    start_date = request.GET.get('StartDate')
    end_date = request.GET.get('EndDate')
    customer_id = request.GET.get('CustomerId')

    # Create JSON string for stored procedure
    json_input = json.dumps({
        "StartDate": start_date,
        "EndDate": end_date,
        "CustomerId": customer_id
    })

    # Call stored procedure
    try:
        with connection.cursor() as cursor:
            cursor.execute("EXEC sp_GetCustomerInfo %s", [json_input])
            result = cursor.fetchall()
	        
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)

    # Convert result to JSON and return
    if result:
        return JsonResponse(result, safe=False)
    else:
        return JsonResponse({"error": "No result found"}, status=404)


# run line in powershell
# Invoke-WebRequest -Uri http://localhost:8000/get_customer_info/ -Method POST -Body '{"StartDate": "2022-01-01", "EndDate": "2022-12-31", "CustomerId": 1}' -ContentType "application/json"
