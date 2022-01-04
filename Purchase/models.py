from django.db import models
from django.db.models.deletion import CASCADE
from django.utils.timezone import now
from accounts.models import Account
from Merchandise.models import *

# Create your models here.

class Bank(models.Model):
    bank_name = models.CharField(max_length=200)
    insert_date = models.DateField(default=now, blank=True, null=True)

    def __str__(self):
        return self.bank_name
    
class BankBranch(models.Model):
    bank = models.ForeignKey(Bank, on_delete=models.CASCADE)
    branch_name = models.CharField(max_length=200)
    def __str__(self):
        return self.branch_name
    
class BankAddress(models.Model):
    branch = models.ForeignKey(BankBranch, on_delete=models.CASCADE)
    address_name = models.TextField()

    def __str__(self):
        return self.address_name

class PurchaseBank(models.Model):
    STATUS = (
        ('SC No', 'SC No'),
        ('LC No', 'LC No'), 
    )
    PAYMENT_STATUS = (
        ('Completed', 'Completed'),
        ('Pending', 'Pending'), 
    )
    TENOR_STATUS = (
        ('At Sight', 'At Sight'),
        ('30 days sight', '30 days sight'), 
        ('60 days sight', '60 days sight'), 
        ('90 days sight', '90 days sight'), 
        ('120 days sight', '120 days sight'), 
    )
    job_no = models.CharField(max_length=200, blank=True, null=True)
    order_no = models.CharField(max_length=200, blank=True, null=True)
    purchase_no = models.CharField(max_length=200, blank=True, null=True)
    l_ref_no = models.CharField(max_length=200)
    p_date = models.DateField(default=now)
    buyer_name = models.CharField(max_length=200, blank=True, null=True)
    factory_name = models.ForeignKey(LibraryCompany, related_name='fact_comp', on_delete=models.CASCADE, blank=True,null=True)
    inv_no = models.CharField(max_length=200)
    bank_name = models.ForeignKey(Bank, on_delete=models.CASCADE, related_name='bank', blank=True, null=True)
    bank_branch = models.ForeignKey(BankBranch, on_delete=models.CASCADE, related_name='bank_branch_name', blank=True, null=True)
    bank_address = models.ForeignKey(BankAddress, on_delete=models.CASCADE, related_name='bank_add_name', blank=True, null=True)
    bill_value = models.FloatField(default=0)
    bill_no = models.CharField(max_length=120)
    bill_date = models.DateField(blank=True, null=True)
    choose_sc_or_lc = models.CharField(max_length=50, choices=STATUS)
    sc_or_lc_no = models.CharField(max_length=120)
    sc_or_lc_date = models.DateField(blank=True, null=True)
    sc_or_lc_amount = models.FloatField(default=0)
    total_btb_amount = models.FloatField(default=0)
    tenor = models.CharField(max_length=120, choices=TENOR_STATUS)
    export_bill = models.FloatField(default=0, blank=True, null=True)
    export_bill_amount = models.CharField(max_length=120, blank=True, null=True)
    export_bill_pct =  models.FloatField(default=100, blank=True, null=True)
    export_bill_amt =  models.FloatField(default=0, blank=True, null=True)
    btb_lc = models.CharField(max_length=120, blank=True, null=True)
    btb_lc_pct = models.FloatField(default=0, blank=True, null=True)
    btb_lc_amt = models.FloatField(default=0, blank=True, null=True)
    pc_amount = models.CharField(max_length=120, blank=True, null=True)
    pc_amount_pct = models.FloatField(default=0, blank=True, null=True)
    pc_amount_amt = models.FloatField(default=0, blank=True, null=True)
    snd_amount = models.CharField(max_length=120, blank=True, null=True)
    snd_amount_pct = models.FloatField(default=0, blank=True, null=True)
    snd_amount_amt = models.FloatField(default=0, blank=True, null=True)
    term_loan = models.CharField(max_length=120, blank=True, null=True)
    term_loan_pct = models.FloatField(default=0, blank=True, null=True)
    term_loan_amt = models.FloatField(default=0, blank=True, null=True)
    time_loan = models.CharField(max_length=120, blank=True, null=True)
    time_loan_pct = models.FloatField(default=0, blank=True, null=True)
    time_loan_amt = models.FloatField(default=0, blank=True, null=True)
    od_loan = models.CharField(max_length=120, blank=True, null=True)
    od_loan_pct = models.FloatField(default=0, blank=True, null=True)
    od_loan_amt = models.FloatField(default=0, blank=True, null=True)
    edf_interest = models.CharField(max_length=120, blank=True, null=True)
    edf_interest_pct = models.FloatField(default=0, blank=True, null=True)
    edf_interest_amt = models.FloatField(default=0, blank=True, null=True)
    buying_com = models.CharField(max_length=120, blank=True, null=True)
    buying_com_pct = models.FloatField(default=0, blank=True, null=True)
    buying_com_amt = models.FloatField(default=0, blank=True, null=True)
    tax_other = models.CharField(max_length=120, blank=True, null=True)
    tax_other_pct = models.FloatField(default=0, blank=True, null=True)
    tax_other_amt = models.FloatField(default=0, blank=True, null=True)
    additional_one = models.CharField(max_length=120, blank=True, null=True)
    additional_one_pct = models.FloatField(default=0, blank=True, null=True)
    additional_one_amt = models.FloatField(default=0, blank=True, null=True)
    additional_two = models.CharField(max_length=120, blank=True, null=True)
    additional_two_pct = models.FloatField(default=0, blank=True, null=True)
    additional_two_amt = models.FloatField(default=0, blank=True, null=True)
    total_percentage = models.FloatField(default=0)
    total_amount = models.FloatField(default=0)
    net_amount = models.FloatField(default=0)
    liability_adj = models.CharField(max_length=200, blank=True, null=True)
    liability_adj_value = models.FloatField(default=0, blank=True, null=True)
    total_purchase = models.FloatField(default=0)
    approve_net_amt = models.FloatField(default=0, blank=True, null=True)
    due_amt = models.FloatField(default=0, blank=True, null=True)
    payment_status = models.CharField(max_length=50, choices=PAYMENT_STATUS, blank=True, null=True)
    approval_date = models.DateField(blank=True, null=True)
    inserted_by = models.ForeignKey(Account, on_delete=models.CASCADE, related_name="purchase_insert_by", null=True, blank=True)
    insert_date = models.DateField(default=now, blank=True, null=True)
    

class ShipmentChalan(models.Model):
    DELIVERY_STATUS = (
        ('On Going', 'On Going'),
        ('Delivered', 'Delivered'), 
        ('Canceled', 'Canceled'), 
    )
    
    job_no = models.CharField(max_length=120)
    lock_no = models.CharField(max_length=120,blank=True,null=True)
    chalan_no = models.CharField(max_length=200, blank=True, null=True)
    factory_name = models.ForeignKey(LibraryCompany, related_name='lib_fact_comp', on_delete=models.CASCADE, blank=True,null=True)
    port_name = models.CharField(max_length=200)
    chalan_to = models.CharField(max_length=200)
    chalan_date = models.DateField(default=now)
    m_or_s = models.CharField(max_length=120, blank=True, null=True)
    gate_pass_no = models.CharField(max_length=120)
    address = models.TextField()
    vehicle_in_time = models.TimeField(blank=True, null=True)
    vehicle_it_image = models.ImageField(upload_to='delivery_chalan/', blank=True, null=True)
    truck_no = models.CharField(max_length=120)
    through = models.CharField(max_length=120)
    driver_name = models.CharField(max_length=120)
    buyer_name = models.CharField(max_length=120)
    driver_license_no = models.CharField(max_length=120)
    invoice_no = models.CharField(max_length=120)
    mobile_no = models.CharField(max_length=120)
    driver_license = models.ImageField(upload_to='delivery_chalan/', blank=True, null=True)
    chalan_license = models.ImageField(upload_to='delivery_chalan/', blank=True, null=True)
    ex_factory_time = models.CharField(max_length=120, blank=True, null=True)
    total_good_qty = models.IntegerField(default=0)
    total_cartoon_qty = models.IntegerField(default=0)
    total_cbm = models.IntegerField(default=0 ,blank=True, null=True)
    delivery_status = models.CharField(max_length=50, choices=DELIVERY_STATUS)
    remarks = models.TextField()
    shipmode = models.ForeignKey(LibraryShipMode, related_name='lib_ship_chal', on_delete=models.CASCADE, blank=True,null=True)
    inserted_by = models.ForeignKey(Account, on_delete=models.CASCADE, related_name="challan_insert_by", null=True, blank=True)
    insert_date = models.DateField(default=now, blank=True, null=True)

    def __str__(self):
        return str(self.id)

class ShipmentChalanItems(models.Model):
    QTY_STATUS = (
        ('Piece', 'Piece'),
        ('Package', 'Package'), 
        
    )
    shipment_chalan = models.ForeignKey(ShipmentChalan, related_name='sh_inline', on_delete=models.CASCADE, null=True, blank=True)
    sl_no = models.CharField(max_length=20, null=True, blank=True)
    item_desc = models.TextField(null=True, blank=True)
    order_no = models.CharField(max_length=20, null=True, blank=True)
    style_no = models.CharField(max_length=20, null=True, blank=True)
    article_no = models.CharField(max_length=20, null=True, blank=True)
    destination = models.CharField(max_length=20, null=True, blank=True)
    goods_qty = models.IntegerField(default=0, null=True, blank=True)
    qty_status = models.CharField(max_length=50, choices=QTY_STATUS, null=True, blank=True)
    cbm = models.IntegerField(default=0, blank=True, null=True)
    cartoon_qty = models.IntegerField(default=0, null=True, blank=True)

class Chechboxes(models.Model):
    fc = models.ForeignKey(PurchaseBank, on_delete=models.CASCADE, null=True)
    btb = models.IntegerField(default=0)
    pc = models.IntegerField(default=0)
    snd = models.IntegerField(default=0)
    term = models.IntegerField(default=0)
    time = models.IntegerField(default=0)
    od = models.IntegerField(default=0)
    edf = models.IntegerField(default=0)
    buying = models.IntegerField(default=0)
    tax = models.IntegerField(default=0)
