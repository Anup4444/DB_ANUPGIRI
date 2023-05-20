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


invoice = {
    'CustomerID': 20,
    'InvoiceDate': '2025-01-01'
}


def create_invoice(invoice):
    proc_name = 'sp_CreateInvoice'
    call_stored_procedure(proc_name, invoice)


# create_invoice(invoice)


def read_invoice(invoice_id):
    proc_name = 'sp_ReadInvoice'
    return call_stored_procedure(proc_name, {'InvoiceID': invoice_id})


# read_invoice(2)


def update_invoice(invoice):
    proc_name = 'sp_UpdateInvoice'
    call_stored_procedure(proc_name, invoice)


invoice = {
    'InvoiceID': 3,
    'InvoiceDate': '2023-01-01',

}
# update_invoice(invoice)


def delete_invoice(invoice_id):
    proc_name = 'sp_DeleteInvoice'
    call_stored_procedure(proc_name, {'InvoiceID': invoice_id})


# delete_invoice(18)
