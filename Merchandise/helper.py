from . import models

class QS:
    def __init__(self, id, po, color, size):
        self.id = id
        self.po = po
        self.color = color
        self.size = size

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
        count = 0
        for i in models.PO_Details.objects.filter(po_job_no=model.id):
            count += 1
            total += float(i.avg_price)
        total /= count
        total = round(total, 2)
    
    return total

def color_size(model):
    temp = []
    for i in models.PO_Details.objects.filter(po_job_no=model.id):
        for j in models.ColorSizeItems.objects.filter(po_color_size=i.id):
            temp.append(QS(j.id, i.po_no, j.color, j.size))
    return temp

def name_starct(string):
    loc = 0
    for i in range(0, len(string)):
        if string[i] == '-':
            loc = i
            break
    return int(string[loc+1:])