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


product = {
    'ProductName': 'fruits',
    'Description': 'This is a test fruits.',
    'Price': 200.99,
    'RemainingQuantity': 5
}


def create_product(product):
    proc_name = 'sp_CreateProduct'
    call_stored_procedure(proc_name, product)


# create_product(product)


def read_product(product_id):
    proc_name = 'sp_ReadProduct'
    call_stored_procedure(proc_name, {'ProductID': product_id})


# read id 1 suppose
# read_product(2)


def update_product(product):
    proc_name = 'sp_UpdateProduct'
    call_stored_procedure(proc_name, product)


# Update the product with ID 1
product_update = {
    'ProductID': 2,
    'ProductName': 'Fruits',
    'Description': 'This is an updated fruits.',
    'Price': 15.99,
    'RemainingQuantity': 44
}

# update_product(product_update)


def delete_product(product_id):
    proc_name = 'sp_DeleteProduct'
    call_stored_procedure(proc_name, {'ProductID': product_id})


# Delete the product with ID 20
# delete_product(2)
