from . import models

def job_no(model):
    if len(model) > 0:
        temp = []
        for i in model:
            temp.append(i.id)
        return int(temp[-1]) + 1
    else:
        return 1

def po_no(model):
    if len(model) > 0:
        temp = []
        for i in model:
            temp.append(i.id)
        return int(temp[-1])
    else:
        return 1
    
def bc_job_no(model):
    if len(model) > 0:
        temp = []
        for i in model:
            temp.append(i.id)
        return int(temp[-1])
    else:
        return 1

def total(model, type):
    total = 0
    if type == 'po_quantity':
        for i in models.PO_Details.objects.filter(po_job_no=model.id):
            total += int(i.po_quantity)
    if type == 'avg_price':
        for i in models.PO_Details.objects.filter(po_job_no=model.id):
            total += float(i.avg_price)
    
    return total