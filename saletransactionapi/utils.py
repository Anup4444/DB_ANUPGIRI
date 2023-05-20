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


saletransaction = {
    'TransactionDate': '2024-02-01',
    'ProductID': 7,
    'CustomerID': 1,
    'Quantity': 80

}


def create_saletransaction(customer):
    proc_name = 'sp_CreateSalesTransaction'
    call_stored_procedure(proc_name, saletransaction)


# create_saletransaction(saletransaction)


def read_saletransaction(transaction_id):
    proc_name = 'sp_ReadSalesTransaction'
    return call_stored_procedure(proc_name, {'TransactionID': transaction_id})

# read_saletransaction(4)


def update_saletransaction(saletransaction):
    proc_name = 'sp_UpdateSalesTransaction'
    call_stored_procedure(proc_name, saletransaction)


saletransaction = {
    'TransactionID': 1,
    'TransactionDate': '2023-01-01',
    'ProductID': 6,
    'CustomerID': 2,
    'Quantity': 40
}

# update_saletransaction(saletransaction)


def delete_saletransaction(transaction_id):
    proc_name = 'sp_DeleteSalesTransaction'
    call_stored_procedure(proc_name, {'TransactionID': transaction_id})


# delete_saletransaction(3)
