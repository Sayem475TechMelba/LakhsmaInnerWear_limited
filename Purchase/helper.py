from django.http import request


def temp_dict(i):
    branch_dict = {} 
    branch_dict[i.branch.branch_name] = i.address_name
    return branch_dict

def conv2b(request, item):
    if request.POST.get(item) == 'on':
        return 1
    else:
        return 0

def update(request, item):
    if request.POST.get(item) == '1':
        return 1
    else:
        return 0

class Company:
    def __init__(self, name):
        self.name = name
        self.id = []
        self.order_value = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    
    def pointer_add(self, id):
        self.id.append(id)
    
    def add_ov(self, amount, index):
        self.order_value[index] += float(amount)
        

def graphAPI(order, po, year):
    companys = []
    name = []
    decode = {
        1 :'jan',
        2 :'feb',
        3 :'mar',
        4 :'apr',
        5 :'may',
        6 :'jun',
        7 :'jul',
        8 :'aug',
        9 :'sep',
        10 :'oct',
        11 :'nov',
        12 :'dec'
    }
    temp_dict_final = {}
    temp_dict = {
        'jan' : 0,
        'feb' : 0,
        'mar' : 0,
        'apr' : 0,
        'may' : 0,
        'jun' : 0,
        'jul' : 0,
        'aug' : 0,
        'sep' : 0,
        'oct' : 0,
        'nov' : 0,
        'dec' : 0,
    }
    for i in order.all():
        if i.company_name.company_name not in name:
            companys.append(Company(i.company_name.company_name))
            name.append(i.company_name.company_name)
    
    for i in order.all():
        for j in companys:
            if i.company_name.company_name == j.name:
                j.pointer_add(i.id)

    for i in companys:
        for j in i.id:
            for k in po.filter(po_job_no=j):
                if k.pub_shipment_date.year == year:
                    i.add_ov(k.amount, k.pub_shipment_date.month-1)
    
    for i in companys:
        count = 1
        temp_dict_month = temp_dict.copy()
        for j in i.order_value:
            temp_dict_month[decode[count]] = j
            count += 1
        temp_dict_final[i.name] = temp_dict_month

    return temp_dict_final
