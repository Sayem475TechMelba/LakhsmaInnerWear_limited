from functools import total_ordering
from django.db import models
import datetime
from django.utils.timezone import now
from django.urls import reverse
from accounts.models import Account

# Create your models here.
#########################################################
############### Library Table Start #####################
##########################################################
class LibraryBuyer(models.Model):
    BUYER_SUB_TYPE = (
        ('Yes', 'Yes'),
        ('No', 'No'),
    )

    buyer_name = models.CharField(max_length=200, null=True)
    contact_person = models.CharField(max_length=200,blank=True, null=True)
    buyer_email = models.CharField(max_length=200, null=True)
    contact_no = models.CharField(max_length=20, null=True)
    website = models.CharField(max_length=200, null=True)
    address = models.TextField(null=True)
    subcontract_party = models.CharField(max_length=200, choices=BUYER_SUB_TYPE, default=0, null=True)
    remark = models.TextField(null=True)
    insert_date = models.DateTimeField(default=now)
    
    def __str__(self):
        return self.buyer_name

class LibraryCompany(models.Model):
    company_name = models.CharField(max_length=200, null=True)
    contact_person = models.CharField(max_length=200, null=True)
    company_nature = models.CharField(max_length=200, null=True)
    core_business = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    website = models.CharField(max_length=200, null=True)
    province = models.CharField(max_length=120, null=True)
    city = models.CharField(max_length=120, null=True)
    zip_code = models.CharField(max_length=120, null=True)
    trade_license_no = models.CharField(max_length=20, null=True)
    insert_date = models.DateTimeField(default=now)

    def __str__(self):
        return self.company_name

class LibraryCompAddress(models.Model):
    company = models.ForeignKey(LibraryCompany, on_delete=models.CASCADE, related_name='compnay')
    location_name = models.CharField(max_length=200, null=True)
    plot_no = models.CharField(max_length=20, null=True)
    level_no = models.CharField(max_length=20, null=True)
    road_no = models.CharField(max_length=20, null=True)
    block_no = models.CharField(max_length=20, null=True)

    def __str__(self):
        return self.location_name

class LibraryProdDept(models.Model):
    department_name = models.CharField(max_length=200, null=True)
    remark = models.TextField(null=True)
    insert_date = models.DateTimeField(default=now)
    
    def __str__(self):
        return self.department_name

class LibraryProdSubDept(models.Model):
    sub_dept_name = models.CharField(max_length=200, null=True)
    remark = models.TextField(null=True)
    insert_date = models.DateTimeField(default=now)
    
    def __str__(self):
        return self.sub_dept_name

class LibraryProductCate(models.Model):
    category_name = models.CharField(max_length=200, null=True)
    category_desc = models.TextField(null=True)
    insert_date = models.DateTimeField(default=now)

    def __str__(self):
        return self.category_name

class LibraryTeamLeader(models.Model):
    leader_name = models.CharField(max_length=200)
    leader_address = models.TextField(null=True, blank=True)
    leader_phone = models.CharField(max_length=200)
    leader_email = models.EmailField(max_length=200)
    leader_company = models.CharField(max_length=200, blank=True, null=True)
    leader_designation = models.CharField(max_length=200, blank=True, null=True)
    leader_dept = models.CharField(max_length=200, blank=True, null=True)
    insert_date = models.DateTimeField(default=now)

    def __str__(self):
        return self.leader_name

class LibraryDealingMerchant(models.Model):
    d_merchant_name = models.CharField(max_length=200)
    d_merchant_address = models.TextField(null=True, blank=True)
    d_merchant_phone = models.CharField(max_length=200)
    d_merchant_email = models.EmailField(max_length=200)
    d_merchant_company = models.CharField(max_length=200, blank=True, null=True)
    d_merchant_designation = models.CharField(max_length=200, blank=True, null=True)
    d_merchant_dept = models.CharField(max_length=200, blank=True, null=True)
    d_merchant_date = models.DateTimeField(default=now)

    def __str__(self):
        return self.d_merchant_name

class LibraryFactoryMerchant(models.Model):
    f_merchant_name = models.CharField(max_length=200)
    f_merchant_address = models.TextField(null=True, blank=True)
    f_merchant_phone = models.CharField(max_length=200)
    f_merchant_email = models.EmailField(max_length=200)
    f_merchant_company = models.CharField(max_length=200, blank=True, null=True)
    f_merchant_designation = models.CharField(max_length=200, blank=True, null=True)
    f_merchant_dept = models.CharField(max_length=200, blank=True, null=True)
    f_merchant_date = models.DateTimeField(default=now)

    def __str__(self):
        return self.f_merchant_name

class LibrarySeason(models.Model):
    season_name = models.CharField(max_length=200, null=True)
    insert_date = models.DateTimeField(default=now)

    def __str__(self):
        return self.season_name

class LibraryRegion(models.Model):
    region_name = models.CharField(max_length=200, null=True)
    insert_date = models.DateTimeField(default=now)

    def __str__(self):
        return self.region_name

class LibraryAgent(models.Model):
    agent_name = models.CharField(max_length=200, null=True)
    insert_date = models.DateTimeField(default=now)

    def __str__(self):
        return self.agent_name


class LibraryClient(models.Model):
    client_name = models.CharField(max_length=200, null=True)
    insert_date = models.DateTimeField(default=now)

    def __str__(self):
        return self.client_name


class LibraryCurrency(models.Model):
    currency_code = models.CharField(max_length=200, null=True)
    description = models.TextField(blank=True)
    insert_date = models.DateTimeField(default=now)

    def __str__(self):
        return self.currency_code
    
class LibraryPacking(models.Model):
    packing_title = models.CharField(max_length=200, null=True)
    insert_date = models.DateTimeField(default=now)

    def __str__(self):
        return self.packing_title
    
class LibraryShipMode(models.Model):
    ship_mode_name = models.CharField(max_length=200, null=True)
    insert_date = models.DateTimeField(default=now)

    def __str__(self):
        return self.ship_mode_name

class LibraryUnit(models.Model):
    unit_name = models.CharField(max_length=200, null=True)
    insert_date = models.DateTimeField(default=now)

    def __str__(self):
        return self.unit_name
    
class LibraryQualityLabel(models.Model):
    quality_label_name = models.CharField(max_length=200, null=True)
    insert_date = models.DateTimeField(default=now)

    def __str__(self):
        return self.quality_label_name

class LibraryPaymentTerm(models.Model):
    payment_term_title = models.CharField(max_length=200, null=True)
    insert_date = models.DateTimeField(default=now)

    def __str__(self):
        return self.payment_term_title


class LibraryShipmentTerm(models.Model):
    shipment_term_title = models.CharField(max_length=200, null=True)
    insert_date = models.DateTimeField(default=now)

    def __str__(self):
        return self.shipment_term_title

class LibraryDesignSource(models.Model):
    source_title = models.CharField(max_length=200, null=True)
    insert_date = models.DateTimeField(default=now)

    def __str__(self):
        return self.source_title
        
class LibraryCountry(models.Model):
    country_name = models.CharField(max_length=200, null=True)
    insert_date = models.DateTimeField(default=now)

    def __str__(self):
        return self.country_name

class LibraryCountryType(models.Model):
    country = models.ForeignKey(LibraryCountry, on_delete=models.CASCADE)
    type_name = models.CharField(max_length=200, null=True)
    insert_date = models.DateTimeField(default=now)

    def __str__(self):
        return self.type_name

class LibraryCutOff(models.Model):
    cut_off = models.CharField(max_length=200, null=True)
    insert_date = models.DateTimeField(default=now)

    def __str__(self):
        return self.cut_off

class LibraryProduct(models.Model):
    STATUS = (
        ('Active', 'Active'),
        ('Inactive', 'Inactive'),
    )

    product_name = models.CharField(max_length=180, blank=True, null=True)
    product_code = models.CharField(max_length=20, blank=True, null=True)
    item_group = models.CharField(max_length=80, blank=True, null=True)
    unit_of_measure = models.CharField(max_length=80, blank=True, null=True)
    item_category = models.ForeignKey(LibraryProductCate, related_name="prod_category", on_delete=models.CASCADE, blank=True, null=True)
    vat_per_unit = models.CharField(max_length=80, blank=True, null=True)
    rate_per_unit = models.CharField(max_length=80, blank=True, null=True)
    current_stock = models.IntegerField(default=0, blank=True, null=True)
    status_active = models.CharField(max_length=20, choices=STATUS, default="Active", blank=True, null=True)
    insert_date = models.DateTimeField(default=now)
   
    def __str__(self):
        return self.product_name

class LibraryFabrication(models.Model):
    fabrication = models.CharField(max_length=200, null=True)
    insert_date = models.DateTimeField(default=now)

    def __str__(self):
        return self.fabrication

#########################################################
############### Library Table End #####################
##########################################################


#########################################################
############### Core Table start #####################
##########################################################

class OrderEntryInfo(models.Model):
    STATUS = (
        ('Yes', 'Yes'),
        ('No', 'No'),
    )
    
    job_no = models.CharField(max_length=40)
    buyer_name = models.ForeignKey(LibraryBuyer, related_name='lib_buyer', on_delete=models.CASCADE, blank=True, null=True)
    company_name = models.ForeignKey(LibraryCompany, related_name='lib_company', on_delete=models.CASCADE, blank=True, null=True)
    company_location = models.ForeignKey(LibraryCompAddress, related_name='company_address', on_delete=models.CASCADE, blank=True, null=True)
    style_ref = models.CharField(max_length=120, blank=True, null=True)
    style_description = models.TextField(blank=True, null=True)
    product_dept = models.ForeignKey(LibraryProdDept, related_name='lib_prod_dept', on_delete=models.CASCADE, blank=True, null=True)
    sub_dept = models.ForeignKey(LibraryProdSubDept, related_name='lib_sub_dept', on_delete=models.CASCADE, blank=True, null=True)
    sub_dept_code = models.CharField(max_length=200, blank=True, null=True)
    product_cate = models.ForeignKey(LibraryProductCate, related_name='lib_product_cate', on_delete=models.CASCADE, blank=True, null=True)
    currency = models.ForeignKey(LibraryCurrency, related_name='lib_currency', on_delete=models.CASCADE, blank=True, null=True)
    region = models.ForeignKey(LibraryRegion, related_name='lib_region', on_delete=models.CASCADE, blank=True, null=True)
    repeat_job_no = models.CharField(max_length=120, blank=True, null=True)
    team_leader = models.ForeignKey(LibraryTeamLeader, related_name='lib_leader', on_delete=models.CASCADE, blank=True, null=True)
    dealing_merchant = models.ForeignKey(LibraryDealingMerchant, related_name='lib_dealing', on_delete=models.CASCADE, blank=True, null=True)
    factory_merchant = models.ForeignKey(LibraryFactoryMerchant, related_name='lib_factory', on_delete=models.CASCADE, blank=True, null=True)
    bh_merchant = models.CharField(max_length=200, blank=True, null=True)
    remarks = models.CharField(max_length=200, blank=True, null=True)
    ship_mode = models.ForeignKey(LibraryShipMode, related_name='lib_ship_mode', on_delete=models.CASCADE, blank=True, null=True)
    order_uom = models.ForeignKey(LibraryUnit, related_name='lib_unit', on_delete=models.CASCADE, blank=True, null=True)
    tt_set_ratio = models.FloatField(default=0, blank=True, null=True)
    tt_sew_smv = models.FloatField(default=0, blank=True, null=True)
    tt_cut_smv = models.FloatField(default=0, blank=True, null=True)
    tt_fin_smv = models.FloatField(default=0, blank=True, null=True)
    smv = models.FloatField(default=0, blank=True, null=True)
    g_tt_smv = models.FloatField(default=0, blank=True, null=True)
    packing = models.ForeignKey(LibraryPacking, related_name='lib_packing', on_delete=models.CASCADE, blank=True, null=True)
    season = models.ForeignKey(LibrarySeason, related_name='lib_season', on_delete=models.CASCADE, blank=True, null=True)
    agent = models.ForeignKey(LibraryAgent, related_name='lib_agent', on_delete=models.CASCADE, blank=True, null=True)
    client = models.ForeignKey(LibraryClient, related_name='lib_client', on_delete=models.CASCADE, blank=True, null=True)
    image = models.ImageField(upload_to="Order/", blank=True, null=True)
    file = models.FileField(upload_to="Order/", blank=True, null=True)
    internal_ref = models.CharField(max_length=80, blank=True, null=True)
    copy_form = models.CharField(max_length=80, blank=True, null=True)
    working_company = models.ForeignKey(LibraryCompany, related_name='work_company', on_delete=models.CASCADE, blank=True, null=True)
    working_location = models.ForeignKey(LibraryCompAddress, related_name='work_location', on_delete=models.CASCADE, blank=True, null=True)
    design_source = models.ForeignKey(LibraryDesignSource, related_name='lib_source', on_delete=models.CASCADE, null=True, blank=True)
    quality_level = models.ForeignKey(LibraryQualityLabel, related_name='lib_quality', on_delete=models.CASCADE, blank=True, null=True)
    shipment_term = models.ForeignKey(LibraryShipmentTerm, on_delete=models.CASCADE, related_name='shipment_term', blank=True, null=True)
    payment_term = models.ForeignKey(LibraryPaymentTerm, on_delete=models.CASCADE, related_name='payment_term', blank=True, null=True)
    inserted_by = models.ForeignKey(Account, on_delete=models.SET_NULL, related_name="insert_by", null=True, blank=True)
    insert_date = models.DateField(default=now, blank=True, null=True)
    status_active = models.CharField(max_length=20, choices=STATUS, default='Yes', null=True, blank=True)

    def __str__(self):
        return str(self.job_no)

class SmvItems(models.Model):
    STATUS = (
        ('Yes', 'Yes'),
        ('No', 'No'),
    )
    order_smv = models.ForeignKey(OrderEntryInfo, related_name="order_smv", on_delete=models.CASCADE, blank=True, null=True)
    items = models.ForeignKey(LibraryProduct, related_name='smv_products', on_delete=models.CASCADE, blank=True, null=True)
    set_ratio = models.FloatField(default=0, blank=True, null=True)
    sew_smv_pcs = models.FloatField(default=0, blank=True, null=True)
    cut_smv_pcs = models.FloatField(default=0, blank=True, null=True)
    fin_smv_pcs = models.FloatField(default=0, blank=True, null=True)
    complexity = models.CharField(max_length=20, choices=STATUS, default="No", blank=True, null=True)
    smv_print = models.CharField(max_length=20, choices=STATUS, default="No", blank=True, null=True)
    print_days = models.FloatField(default=0, blank=True, null=True)
    embro = models.CharField(max_length=20, choices=STATUS, default="No", blank=True, null=True)
    embro_days = models.FloatField(default=0, blank=True, null=True)
    wash = models.CharField(max_length=20, choices=STATUS, default="No", blank=True, null=True)
    wash_days = models.FloatField(default=0, blank=True, null=True)
    sp_work = models.CharField(max_length=20, choices=STATUS, default="No", blank=True, null=True)
    sp_work_days = models.FloatField(default=0, blank=True, null=True)
    gmts_dyeing = models.CharField(max_length=20, choices=STATUS, default="No", blank=True, null=True)
    gmts_dyeing_days = models.FloatField(default=0, blank=True, null=True)
    aop = models.CharField(max_length=20, choices=STATUS, default="No", blank=True, null=True)
    aop_days = models.FloatField(default=0, blank=True, null=True)
    tt_smv = models.FloatField(default=0, blank=True, null=True)

class PO_Details(models.Model):
    ORDER_STATUS = (
        ('Confirmed', 'Confirmed'),
        ('Projected', 'Projected'),
    )
    PROJECTED_STATUS = (
        ('Yes', 'Yes'),
        ('No', 'No'),
    )
    STATUS = (
        ('Active', 'Active'),
        ('Inactive', 'Inactive'),
    )
    TNA_STATUS = (
        ('Yes', 'Yes'),
        ('No', 'No'),
    )
    po_job_no = models.ForeignKey(OrderEntryInfo, related_name='order_entry', on_delete=models.CASCADE, blank=True, null=True)
    #po_job_no = models.CharField(max_length=20000, blank=True, null=True)
    order_status = models.CharField(max_length=20, choices=ORDER_STATUS, blank=True, null=True)
    projected_po = models.CharField(max_length=20, choices=PROJECTED_STATUS,blank=True, null=True)
    gsm = models.IntegerField(default= 0, blank=True, null=True)
    po_no = models.CharField(max_length=120, blank=True, null=True)
    po_recieve_date = models.DateField(default=now, blank=True, null=True)
    pub_shipment_date = models.DateField(blank=True, null=True)
    lead_time = models.CharField(max_length=20, blank=True, null=True)
    org_shipment_date = models.DateField(blank=True, null=True)
    fac_recieve_date = models.DateField(blank=True, null=True)
    country = models.ForeignKey(LibraryCountry, related_name="country", on_delete=models.CASCADE, blank=True, null=True)
    country_type = models.ForeignKey(LibraryCountryType, related_name="countrytype_lib", on_delete=models.CASCADE, blank=True, null=True)
    cutoff_date = models.DateField(blank=True, null=True)
    cutoff = models.ForeignKey(LibraryCutOff, related_name='cutoff_lib', on_delete=models.CASCADE, null=True, blank=True)
    country_shipment_date = models.DateField(default=now, blank=True, null=True)
    color_remarks = models.TextField(blank=True, null=True)
    packing = models.ForeignKey(LibraryPacking, related_name="packing", on_delete=models.CASCADE, blank=True, null=True)
    po_quantity = models.CharField(max_length=120, blank=True, null=True)
    avg_price = models.FloatField(default= 0.0, blank=True, null=True)
    amount = models.FloatField(default= 0.0, blank=True, null=True)
    excess_cut_pct = models.FloatField(default= 0.0, blank=True, null=True)
    plan_cut_qty = models.FloatField(default=0, blank=True, null=True)
    status_active = models.CharField(max_length=20, choices=STATUS, blank=True, null=True)
    po_packing = models.ForeignKey(LibraryPacking, related_name='po_packing', on_delete=models.CASCADE, blank=True, null=True)
    tna_from_upto = models.CharField(max_length=20, choices=TNA_STATUS,blank=True, null=True)
    internal_ref = models.CharField(max_length=120,blank=True, null=True)
    delay_for = models.CharField(max_length=200, blank=True, null=True)
    file_no = models.CharField(max_length=200,blank=True, null=True)
    sc_or_lc = models.CharField(max_length=120,blank=True, null=True)
    file_add = models.FileField(upload_to="Order/", blank=True, null=True)
    actual_po_no = models.ImageField(upload_to="Order/", blank=True, null=True)
    remarks = models.TextField(blank=True, null=True)
    # for color size
    order_quan = models.FloatField(default= 0, blank=True, null=True)
    tt_rate = models.FloatField(default= 0, blank=True, null=True)
    amt = models.FloatField(default= 0, blank=True, null=True)
    exc = models.FloatField(default= 0, blank=True, null=True)
    plan_cut = models.FloatField(default=0, blank=True, null=True)

    inserted_by = models.ForeignKey(Account, on_delete=models.SET_NULL, related_name="po_insert_by", null=True, blank=True)
    insert_date = models.DateTimeField(default=now, blank=True, null=True)

    def __str__(self):
        return str(self.id)


class ColorSizeItems(models.Model):
    STATUS = (
        ('Active', 'Active'),
        ('Inactive', 'Inactive'),
    )
    po_color_size = models.ForeignKey(PO_Details, related_name="color_size", on_delete=models.CASCADE, blank=True, null=True)
    gmt_items = models.ForeignKey(LibraryProduct, related_name="items", on_delete=models.CASCADE,  blank=True, null=True)
    article_number = models.CharField(max_length=120,  blank=True, null=True)
    color = models.CharField(max_length=120,  blank=True, null=True)
    fabrication =  models.ForeignKey(LibraryFabrication, related_name="lib_fabrication", on_delete=models.CASCADE, blank=True, null=True)
    size = models.CharField(max_length=120,  blank=True, null=True)
    order_qty = models.IntegerField(default=0, blank=True, null=True)
    rate = models.FloatField(default=0, blank=True, null=True)
    amount = models.FloatField(default=0, blank=True, null=True)
    excess_cut = models.FloatField(default=0, blank=True, null=True)
    plan_cut_qty = models.FloatField(default=0, blank=True, null=True)
    status_active = models.CharField(max_length=20, choices=STATUS,  blank=True, null=True)
    
    def __str__(self):
        return str(self.po_color_size)
