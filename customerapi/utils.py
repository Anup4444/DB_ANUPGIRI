import json
from django.db import connection, transaction


def call_stored_procedure(proc_name, params):
    cursor = connection.cursor()
    try:
        # Convert dictionary to JSON string
        json_params = json.dumps(params)

        # Call stored procedure with execute
        cursor.execute(f"EXEC {proc_name} @json = %s", [json_params])
    except Exception as e:
        transaction.rollback()
        raise e
    else:
        transaction.commit()
        cursor.close()


customer = {
    'Name': 'arjun',
    'Email': 'arjun@gmail.com',
    'Phone': '98482179842'
}


def create_customer(customer):
    proc_name = 'sp_CreateCustomer'
    call_stored_procedure(proc_name, customer)


create_customer(customer)


def read_customer(customer_id):
    proc_name = 'sp_ReadCustomer'
    return call_stored_procedure(proc_name, {'CustomerID': customer_id})


# read_customer(2)


def update_customer(customer):
    proc_name = 'sp_UpdateCustomer'
    call_stored_procedure(proc_name, customer)


customer = {
    'CustomerID': 20,
    'Name': 'punam',
    'Email': 'puman@gmail.com',
    'Phone': '9882379842'
}

# update_customer(customer)


def delete_customer(customer_id):
    proc_name = 'sp_DeleteCustomer'
    call_stored_procedure(proc_name, {'CustomerID': customer_id})


# delete_customer(18)
