from Merchandise import models
import datetime

class MailTableData():
    def __init__(self, name, job, b_name, po, oty, avg_p, t_value, ship_d, lead_t, eb, date):
        self.name = name
        self.job = job
        self.b_name = b_name
        self.po = po
        self.oty = oty
        self.avg_p = avg_p
        self.t_value = t_value
        self.ship_d = ship_d
        self.lead_t = lead_t
        self.eb = eb
        self.date = date

def test_data():
    lis = []
    data = []
    for i in models.OrderEntryInfo.objects.all():
        if str(i.insert_date) == '2022-01-04': #datetime.datetime.now().strftime('%y-%m-%d'):
            lis.append(i)

    for i in lis:
        data.append(MailTableData(i.company_name.company_name, i.job_no, i.buyer_name.buyer_name, None, None, None, None, None, None, None, i.insert_date))

    return data