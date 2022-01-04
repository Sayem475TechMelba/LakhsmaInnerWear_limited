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