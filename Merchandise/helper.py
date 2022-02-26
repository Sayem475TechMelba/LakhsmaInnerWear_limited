from . import models

class QS:
    def __init__(self, id, po, country, color, size, order_qty, gmt_items):
        self.id = id
        self.po = po
        self.color = color
        self.size = size
        self.order_qty = order_qty
        self.gmt_items = gmt_items
        self.country = country

def coustom_inline(color, fabric, count):
    color_lis = []
    fabric_lis = []
    counter = 0
    for i in color:
        color_lis.append(i)
    for j in fabric:
        fabric_lis.append(j)

    for i in range(1, count+1):
        color_lis[counter].fabric_cost = fabric_lis[counter]
        color_lis[counter].save()
        counter += 1
        
def embl_inline(color, embl, count):
    color_lis = []
    embl_lis = []
    counter = 0
    for i in color:
        color_lis.append(i)
    for j in embl:
        embl_lis.append(j)

    for i in range(1, count+1):
        color_lis[counter].embl_cost = embl_lis[counter]
        color_lis[counter].save()
        counter += 1

def wash_inline(color, wash, count):
    color_lis = []
    wash_lis = []
    counter = 0
    for i in color:
        color_lis.append(i)
    for j in wash:
        wash_lis.append(j)

    for i in range(1, count+1):
        color_lis[counter].wash_cost = wash_lis[counter]
        color_lis[counter].save()
        counter += 1
        
def job_no(model):
    if len(model) > 0:
        temp = []
        for i in model:
            temp.append(i)
        return temp[-1]

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
            temp.append(QS(j.id, i.po_no, i.country, j.color, j.size, j.order_qty, j.gmt_items))
    return temp

def name_starct(string):
    loc = 0
    for i in range(0, len(string)):
        if string[i] == '_':
            loc = i
            break
    return int(string[loc+1:])

def gmts_item(model, type):
    if type == 'color':
        pro = []
        final = []
        for i in models.PO_Details.objects.filter(po_job_no=model.id):
            for j in models.ColorSizeItems.objects.filter(po_color_size=i.id):
                if str(j.color).lower() not in pro:
                    pro.append(str(j.color).lower())

        for i in pro:
            final.append(i.capitalize())
        return final
    elif type == "gmt":
        pro = []
        final = []
        for i in models.PO_Details.objects.filter(po_job_no=model.id):
            for j in models.ColorSizeItems.objects.filter(po_color_size=i.id):
                if str(j.gmt_items).lower() not in pro:
                    pro.append(str(j.gmt_items).lower())

        for i in pro:
            final.append(i.capitalize())
        return final