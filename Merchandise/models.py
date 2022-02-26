from functools import total_ordering
from pyexpat import model
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
    color = models.CharField(max_length=100, null=True, blank=True)
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

############# Budget Library ###########

class LibraryCostingPer(models.Model):
    costing_per = models.CharField(max_length=200, null=True)
    insert_date = models.DateTimeField(default=now)

    def __str__(self):
        return self.costing_per

class LibraryBodyPart(models.Model):
    body_part_name = models.CharField(max_length=200, null=True)
    bp_Type = models.CharField(max_length=200, blank=True, null=True)
    insert_date = models.DateTimeField(default=now)

    def __str__(self):
        return self.body_part_name

class LibraryBodyPartType(models.Model): #### it should be exclude
    bp_Type_name = models.CharField(max_length=200, null=True)
    insert_date = models.DateTimeField(default=now)

    def __str__(self):
        return self.bp_Type_name
        
class LibraryFabNature(models.Model):
    fab_nature_name = models.CharField(max_length=200, null=True)
    insert_date = models.DateTimeField(default=now)

    def __str__(self):
        return self.fab_nature_name

class LibraryColorType(models.Model):
    color_type = models.CharField(max_length=200, null=True)
    insert_date = models.DateTimeField(default=now)

    def __str__(self):
        return self.color_type

class LibraryFabricSource(models.Model):
    fabric_source = models.CharField(max_length=200, null=True)
    insert_date = models.DateTimeField(default=now)

    def __str__(self):
        return self.fabric_source

class LibraryFabricDescription(models.Model):
    fab_nature = models.ForeignKey(LibraryFabNature, on_delete=models.CASCADE)
    construction = models.CharField(max_length=200)
    gsm_weight = models.PositiveIntegerField(default=0)
    color_range = models.CharField(max_length=200, null=True, blank=True)
    stich_length = models.CharField(max_length=200, null=True, blank=True)
    process_loss = models.CharField(max_length=200, null=True, blank=True)
    yarn_one_pct = models.PositiveIntegerField(default=0, blank=True, null=True)
    yarn_one = models.CharField(max_length=120, blank=True, null=True)
    yarn_count_one = models.CharField(max_length=120, blank=True, null=True)
    yarn_type_one = models.CharField(max_length=120, blank=True, null=True)
    yarn_two_pct = models.PositiveIntegerField(default=0, blank=True, null=True)
    yarn_two = models.CharField(max_length=120, blank=True, null=True)
    yarn_count_two = models.CharField(max_length=120, blank=True, null=True)
    yarn_type_two = models.CharField(max_length=120, blank=True, null=True)
    insert_date = models.DateTimeField(default=now)

    def __str__(self):
        return self.construction 

class LibraryNominatedSupp(models.Model):
    supplier_name = models.CharField(max_length=200, null=True)
    insert_date = models.DateTimeField(default=now)

    def __str__(self):
        return self.supplier_name

class LibraryDiaTypes(models.Model):
    width_dia_name = models.CharField(max_length=200, null=True)
    insert_date = models.DateTimeField(default=now)

    def __str__(self):
        return self.width_dia_name

class LibraryConsumptionBasis(models.Model):
    consumption_basis = models.CharField(max_length=200, null=True)
    insert_date = models.DateTimeField(default=now)

    def __str__(self):
        return self.consumption_basis

class LibraryColorSizeSensitive(models.Model):
    color_size_sensitive = models.CharField(max_length=200, null=True)
    insert_date = models.DateTimeField(default=now)

    def __str__(self):
        return self.color_size_sensitive

############# Yarn Cost Library ##########
class LibraryYarnType(models.Model):
    type_name = models.CharField(max_length=200, null=True)
    insert_date = models.DateTimeField(default=now)

    def __str__(self):
        return self.type_name

class LibraryYarnSupplier(models.Model):
    supplier_name = models.CharField(max_length=200, null=True)
    insert_date = models.DateTimeField(default=now)

    def __str__(self):
        return self.supplier_name

############# Convertion Cost Library ##########
class LibraryProcess(models.Model):
    process_name = models.CharField(max_length=200, null=True)
    insert_date = models.DateTimeField(default=now)

    def __str__(self):
        return self.process_name
    

class LibraryKnitting(models.Model):
    STATUS = (
        ('Active', 'Active'),
        ('Inactive', 'Inactive'),
    )
    company_name = models.CharField(max_length=200, null=True)
    body_part = models.CharField(max_length=200, null=True)
    const_and_comp = models.CharField(max_length=200, null=True)
    gsm = models.PositiveIntegerField(default=0)
    yarn_desc = models.CharField(max_length=200, null=True)
    uom = models.CharField(max_length=80, null=True)
    inhouse_rate = models.FloatField(default=0)
    bdt_to_usd = models.FloatField(default=0)
    status = models.CharField(max_length=50, choices=STATUS, default="Active", blank=True, null=True)
    insert_date = models.DateTimeField(default=now)


    def __str__(self):
        return self.body_part

class LibraryDyeing(models.Model):
    STATUS = (
        ('Active', 'Active'),
        ('Inactive', 'Inactive'),
    )
    company_name = models.CharField(max_length=200, null=True)
    const_and_comp = models.CharField(max_length=200, null=True)
    process_type = models.CharField(max_length=200, null=True)
    process_name = models.CharField(max_length=200, null=True)
    color = models.CharField(max_length=200, null=True)
    width_dia_type= models.CharField(max_length=200, null=True)
    inhouse_rate = models.FloatField(default=0)
    bdt_to_usd = models.FloatField(default=0)
    uom = models.CharField(max_length=80, null=True)
    rate_type = models.CharField(max_length=200, null=True)
    status = models.CharField(max_length=50, choices=STATUS, default="Active", blank=True, null=True)
    insert_date = models.DateTimeField(default=now)


    def __str__(self):
        return self.color

############# Trim Cost Library ##########
class LibraryGroupsItem(models.Model):
    group_item_name = models.CharField(max_length=200, null=True)
    group_item_uom = models.CharField(max_length=80, null=True)
    trims_type = models.CharField(max_length=80, null=True)
    insert_date = models.DateTimeField(default=now)

    def __str__(self):
        return self.group_item_name

class LibraryTrimSource(models.Model):
    source_name = models.CharField(max_length=200, null=True)
    insert_date = models.DateTimeField(default=now)

    def __str__(self):
        return self.source_name
    
############# Embellishment Cost Library ##########

class LibraryEmbCostName(models.Model):
    cost_name = models.CharField(max_length=200, blank=True, null=True)
    insert_date = models.DateTimeField(default=now)
    
    def __str__(self):
        return self.cost_name

class LibraryEmbCostType(models.Model):
    cost_name = models.ForeignKey(LibraryEmbCostName, related_name="emb_cost_name", on_delete=models.CASCADE, blank=True, null=True)
    type_name = models.CharField(max_length=200, blank=True, null=True)
    insert_date = models.DateTimeField(default=now)
    
    def __str__(self):
        return self.type_name

############# Wash Cost Library ##########
class LibraryWash_CostName(models.Model):
    w_cost_name = models.CharField(max_length=200, blank=True, null=True)
    insert_date = models.DateTimeField(default=now)
    
    def __str__(self):
        return self.w_cost_name

class LibraryWash_CostType(models.Model):
    w_cost_name = models.ForeignKey(LibraryWash_CostName, related_name="wash_cname", on_delete=models.CASCADE, blank=True, null=True)
    w_type_name = models.CharField(max_length=200, blank=True, null=True)
    insert_date = models.DateTimeField(default=now)
    
    def __str__(self):
        return self.w_cost_name
#########################################################
############### Library Table End #####################
##########################################################

# Budget cost item piece library
class LibraryPcsQty(models.Model):
    pcs_amount = models.PositiveIntegerField(default=12)
    insert_date = models.DateTimeField(default=now)

    def __str__(self):
        return str(self.pcs_amount)
# Doller rate library 
class LibraryDoller(models.Model):
    usd_rate = models.FloatField(default=0)
    insert_date = models.DateTimeField(default=now)

    def __str__(self):
        return str(self.usd_rate)

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
    projected_po = models.CharField(max_length=20, choices=PROJECTED_STATUS, default="No", blank=True, null=True)
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
    
    # def total_qty(self):
    #     job = OrderEntryInfo.objects.all()
    #     po = PO_Details.objects.filter(po_job_no__job_no=job.job_no)
    #     po_qty = po.annotate(sum('po_quantity'))
    #     print(po_qty)
    #     return po_qty

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

#################### Budget Costing All DB ######################
#################################################################

class BudgetPreCost(models.Model):
    STATUS = (
        ('Yes', 'Yes'),
        ('No', 'No'),
    )
    job_no = models.ForeignKey(OrderEntryInfo, related_name="budget_cost", on_delete=models.CASCADE, null=True)
    quotation_id = models.CharField(max_length=120, blank=True, null=True)
    er= models.CharField(max_length=120, blank=True, null=True)
    job_qty= models.FloatField(default=0, blank=True, null=True)
    avg_rate = models.FloatField(default=0, blank=True, null=True) # for hiddden field
    order_unit= models.CharField(max_length=120, blank=True, null=True)#have to remove
    item_details= models.CharField(max_length=250, blank=True, null=True)
    costing_date = models.DateField(blank=True, null=True)
    incoterm_place = models.CharField(max_length=250, blank=True, null=True)
    machine_line = models.CharField(max_length=120, blank=True, null=True)
    prod_line = models.CharField(max_length=120, blank=True, null=True)
    costing_per = models.CharField(max_length=120, blank=True, null=True)
    approved = models.CharField(max_length=20,  choices=STATUS,  blank=True, null=True)
    sew_efficiency = models.FloatField(default=0, blank=True, null=True)
    cut_efficiency = models.FloatField(default=0, blank=True, null=True)
    remarks = models.TextField(blank=True, null=True)
    budget_minute = models.IntegerField(default=0, blank=True, null=True)
    file_no = models.CharField(max_length=120, blank=True, null=True)
    internal_ref = models.CharField(max_length=120, blank=True, null=True)#have to remove
    copy_form = models.CharField(max_length=120, blank=True, null=True)
    redy_to_approved = models.CharField(max_length=20,  choices=STATUS,  blank=True, null=True)
    mini_marker_upload = models.FileField(upload_to='Budget/Image', blank=True, null=True)
    inserted_by = models.ForeignKey(Account, on_delete=models.SET_NULL, related_name="bpc_insert_by", null=True, blank=True)
    insert_date = models.DateTimeField(default=now, blank=True, null=True)
    
    def __str__(self):
        return str(self.job_no)
    
class FabricCost(models.Model):
    b_job_no = models.ForeignKey(BudgetPreCost, related_name='fabric_cost', on_delete=models.CASCADE, null=True, blank=True)
    inserted_by = models.ForeignKey(Account, on_delete=models.SET_NULL, related_name="fab_insert_by", null=True, blank=True)
    insert_date = models.DateTimeField(default=now, blank=True, null=True)
    def __str__(self):
        return str(self.b_job_no)

class Fabric_Inline_Item(models.Model):
    SOURCE = (
        ('Foreign', 'Foreign'),
        ('Local', 'Local'),
    )
    fabric_cost = models.ForeignKey(FabricCost, related_name="fabric_inline", on_delete=models.CASCADE, blank=True, null=True)
    gmts_items =models.CharField(max_length=200, blank=True, null=True)
    body_part = models.CharField(max_length=200, blank=True, null=True)
    body_part_type = models.CharField(max_length=200, blank=True, null=True)
    fab_nature = models.ForeignKey(LibraryFabNature, related_name="lib_fn", on_delete=models.CASCADE, blank=True, null=True)
    color_type = models.ForeignKey(LibraryColorType, related_name="lib_ctype", on_delete=models.CASCADE, blank=True, null=True)
    fabric_source = models.ForeignKey(LibraryFabricSource, related_name="lib_fsource", on_delete=models.CASCADE, blank=True, null=True)
    source =  models.CharField(max_length=50, choices=SOURCE,  blank=True, null=True)
    fabric_desc = models.CharField(max_length=200, blank=True, null=True)
    nom_supplier = models.ForeignKey(LibraryNominatedSupp, related_name="lib_nsupplier", on_delete=models.CASCADE, blank=True, null=True)
    width_dia = models.ForeignKey(LibraryDiaTypes, related_name="lib_dia_type", on_delete=models.CASCADE, blank=True, null=True)
    gms = models.CharField(max_length=80, blank=True, null=True)
    cs_sensitive = models.ForeignKey(LibraryColorSizeSensitive, related_name="lib_cs_sensitive", on_delete=models.CASCADE, blank=True, null=True)
    color = models.CharField(max_length=200, blank=True, null=True)
    con_basis = models.ForeignKey(LibraryConsumptionBasis, related_name="lib_con_basis", on_delete=models.CASCADE, blank=True, null=True)
    uom = models.ForeignKey(LibraryUnit, related_name="lib_uom", on_delete=models.CASCADE, blank=True, null=True)
    avg_grey_cons = models.FloatField(default=0, blank=True, null=True)
    rate = models.FloatField(default=0, blank=True, null=True)
    amount = models.FloatField(default=0, blank=True, null=True)
    total_quantity = models.FloatField(default=0, blank=True, null=True)
    total_amount = models.FloatField(default=0, blank=True, null=True)

    def __str__(self):
        return str("%s-%s" %(self.fabric_cost, self.id))

class YarnCost(models.Model):
    b_job_no = models.ForeignKey(BudgetPreCost, related_name='yarn_cost', on_delete=models.CASCADE, null=True, blank=True)
    tt_cons_qty = models.FloatField(default=0, blank=True, null=True)
    tt_amount = models.FloatField(default=0, blank=True, null=True)
    inserted_by = models.ForeignKey(Account, on_delete=models.SET_NULL, related_name="yarn_insert_by", null=True, blank=True)
    insert_date = models.DateTimeField(default=now, blank=True, null=True)

    def __str__(self):
        return str(self.b_job_no)
#updated
class Yarn_Inline_Item(models.Model):
    yarn_cost = models.ForeignKey(YarnCost, related_name="yarn_inline", on_delete=models.CASCADE, blank=True, null=True)
    count = models.CharField(max_length=120, blank=True, null=True)
    comp_one = models.CharField(max_length=120, blank=True, null=True)
    pct = models.FloatField(default=100, blank=True, null=True)
    color = models.CharField(max_length=120, blank=True, null=True)
    type = models.CharField(max_length=120, blank=True, null=True)
    cons_qty = models.FloatField(default=0, blank=True, null=True)
    supplier = models.ForeignKey(LibraryYarnSupplier, related_name="lib_ysupplier", on_delete=models.CASCADE, blank=True, null=True)
    rate = models.FloatField(default=0, blank=True, null=True)
    amount = models.FloatField(default=0, blank=True, null=True)

    def __str__(self):
        return str(self.yarn_cost)


class ConversionCost(models.Model):
    b_job_no = models.ForeignKey(BudgetPreCost, related_name='conv_cost', on_delete=models.CASCADE)
    tt_reg_qty = models.FloatField(default=0, blank=True, null=True)
    tt_avg_reg_qty = models.FloatField(default=0, blank=True, null=True)
    tt_charge_unit = models.FloatField(default=0, blank=True, null=True)
    tt_amount = models.FloatField(default=0, blank=True, null=True)
    inserted_by = models.ForeignKey(Account, on_delete=models.SET_NULL, related_name="con_insert_by", null=True, blank=True)
    insert_date = models.DateTimeField(default=now, blank=True, null=True)

    def __str__(self):
        return str(self.b_job_no)

class Conversion_Inline(models.Model):
    STATUS = (
        ('Active', 'Active'),
        ('Inactive', 'Inactive'),
    )
    conversion_cost = models.ForeignKey(ConversionCost, related_name="conver_inline", on_delete=models.CASCADE, blank=True, null=True)
    fab_desc = models.CharField(max_length=120, blank=True, null=True)
    process = models.ForeignKey(LibraryProcess, related_name="lib_cprocess", on_delete=models.CASCADE, blank=True, null=True)
    process_loss = models.FloatField(default=0, blank=True, null=True)
    reg_qty = models.FloatField(default=0, blank=True, null=True)
    avg_reg_qty = models.FloatField(default=0, blank=True, null=True)
    charge_unit = models.FloatField(default=0, blank=True, null=True)
    amount = models.FloatField(default=0, blank=True, null=True)
    status = models.CharField(max_length=50, choices=STATUS, default="Active", blank=True, null=True)

    def __str__(self):
        return str(self.conversion_cost)
    

class Grey_Cons(models.Model):
    b_job_no = models.ForeignKey(BudgetPreCost, related_name="grey_cons", on_delete=models.CASCADE, blank=True, null=True)
    fabric_cost = models.ForeignKey(Fabric_Inline_Item, on_delete=models.CASCADE, blank=True, null=True)
    tt_finish_cons = models.FloatField(default=0, blank=True, null=True)
    tt_process_loss = models.FloatField(default=0, blank=True, null=True)
    tt_grey_cons = models.FloatField(default=0, blank=True, null=True)
    tt_rate = models.FloatField(default=0, blank=True, null=True)
    sub_tt_amount = models.FloatField(default=0, blank=True, null=True)
    tt_pcs = models.FloatField(default=0, blank=True, null=True)
    sub_tt_qty = models.FloatField(default=0, blank=True, null=True)
    gt_tt_qty = models.FloatField(default=0, blank=True, null=True)
    avg_finish_cons = models.FloatField(default=0, blank=True, null=True)
    avg_process_loss = models.FloatField(default=0, blank=True, null=True)
    avg_grey_cons = models.FloatField(default=0, blank=True, null=True)
    avg_rate = models.FloatField(default=0, blank=True, null=True)
    sub_avg_amount = models.FloatField(default=0, blank=True, null=True)
    avg_pcs = models.FloatField(default=0, blank=True, null=True)
    sub_avg_qty = models.FloatField(default=0, blank=True, null=True)
    gt_avg_qty = models.FloatField(default=0, blank=True, null=True)
    inserted_by = models.ForeignKey(Account, on_delete=models.SET_NULL, related_name="grey_insert_by", null=True, blank=True)
    insert_date = models.DateTimeField(default=now, blank=True, null=True)
    
    def __str__(self):
        return str(self.b_job_no)

class Grey_Cons_Items(models.Model):
    grey_cons = models.ForeignKey(Grey_Cons, related_name="grey_items", on_delete=models.CASCADE, blank=True, null=True)
    color_size = models.ForeignKey(ColorSizeItems, on_delete=models.CASCADE, blank=True, null=True)
    po_no = models.CharField(max_length=80, blank=True, null=True)
    color = models.CharField(max_length=200, blank=True, null=True)
    gmts_size = models.CharField(max_length=200, blank=True, null=True)
    qty = models.FloatField(blank=True, null=True)
    dia = models.CharField(max_length=200, blank=True, null=True)
    item_sizes =  models.CharField(max_length=200, blank=True, null=True)
    fab_cons = models.FloatField(default=0, blank=True, null=True)
    process_loss_pct = models.FloatField(default=0, blank=True, null=True)
    grey_cons_unit = models.FloatField(default=0, blank=True, null=True)
    rate = models.FloatField(default=0, blank=True, null=True)
    amount = models.FloatField(default=0, blank=True, null=True)
    pcs = models.FloatField(default=0, blank=True, null=True)
    total_qty = models.FloatField(default=0, blank=True, null=True)
    total_amount = models.FloatField(default=0, blank=True, null=True)
    remarks = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return str(self.color_size)

class ColorContrast(models.Model):
    b_job_no = models.ForeignKey(BudgetPreCost, related_name="color_contrast", on_delete=models.CASCADE, blank=True, null=True)
    fabric_cost = models.ForeignKey(Fabric_Inline_Item, related_name="fab_cost", on_delete=models.CASCADE, blank=True, null=True)
    inserted_by = models.ForeignKey(Account, on_delete=models.SET_NULL, related_name="contrast", null=True, blank=True)
    insert_date = models.DateTimeField(default=now, blank=True, null=True)

    def __str__(self):
        return str(self.b_job_no)

class ColorContrastItems(models.Model):
    color_contrast = models.ForeignKey(ColorContrast, related_name="contrast_item", on_delete=models.CASCADE, blank=True, null=True)
    gmts_color = models.CharField(max_length=200, blank=True, null=True)
    contrast_color = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return str(self.color_contrast)

class DyeingColor(models.Model):
    b_job_no = models.ForeignKey(BudgetPreCost, related_name="color_popup", on_delete=models.CASCADE, blank=True, null=True)
    conversion_cost = models.ForeignKey(Conversion_Inline, related_name="con_cost", on_delete=models.CASCADE, blank=True, null=True)
    tt_cons = models.FloatField(default=0, blank=True, null=True)
    tt_charge = models.FloatField(default=0, blank=True, null=True)
    avg_tt_cons = models.FloatField(default=0, blank=True, null=True)
    avg_tt_charge = models.FloatField(default=0, blank=True, null=True)
    inserted_by = models.ForeignKey(Account, on_delete=models.SET_NULL, related_name="color_pop", null=True, blank=True)
    insert_date = models.DateTimeField(default=now, blank=True, null=True)

    def __str__(self):
        return str(self.b_job_no)

class DyeingColorItems(models.Model):
    dyeing_color = models.ForeignKey(DyeingColor, related_name="dyeing_item", on_delete=models.CASCADE, blank=True, null=True)
    gmts_color = models.CharField(max_length=200, blank=True, null=True)
    fabric_color = models.CharField(max_length=200, blank=True, null=True)
    cons_rate = models.FloatField(default=0, blank=True, null=True)
    charge_unit = models.FloatField(default=0, blank=True, null=True)

    def __str__(self):
        return str(self.dyeing_color)

class TrimCost(models.Model):
    b_job_no = models.ForeignKey(BudgetPreCost, related_name='trim_cost', on_delete=models.CASCADE, null=True, blank=True)
    tt_cons_unit = models.FloatField(default=0, blank=True, null=True)
    tt_rate = models.FloatField(default=0, blank=True, null=True)
    tt_sub_amount = models.FloatField(default=0, blank=True, null=True)
    tt_grand_quantity = models.FloatField(default=0, blank=True, null=True)
    tt_grand_amount = models.FloatField(default=0, blank=True, null=True)
    inserted_by = models.ForeignKey(Account, on_delete=models.SET_NULL, related_name="trim_insert_by", null=True, blank=True)
    insert_date = models.DateTimeField(default=now, blank=True, null=True)

    def __str__(self):
        return str(self.b_job_no)
    
class TrimCostItems(models.Model):
    APVT = (
        ('Yes', 'Yes'),
        ('No', 'No'),
    )
    trim_cost = models.ForeignKey(TrimCost, related_name="trim_items", on_delete=models.CASCADE, blank=True, null=True )
    group = models.CharField(max_length=200, blank=True, null=True)
    country = models.CharField(max_length=200, blank=True, null=True)
    description = models.CharField(max_length=300, blank=True, null=True)
    brand_sup_ref = models.CharField(max_length=200, blank=True, null=True)
    remarks = models.CharField(max_length=200, blank=True, null=True)
    source =  models.ForeignKey(LibraryTrimSource, related_name="lib_tsource", on_delete=models.CASCADE, blank=True, null=True )
    nominated_supp = models.CharField(max_length=200, blank=True, null=True)
    cons_uom = models.CharField(max_length=200, blank=True, null=True)
    cons_unit_gmts = models.FloatField(default=0, blank=True, null=True)
    rate = models.FloatField(default=0, blank=True, null=True)
    amount = models.FloatField(default=0, blank=True, null=True)
    tt_qty = models.FloatField(default=0, blank=True, null=True)
    tt_amt = models.FloatField(default=0, blank=True, null=True)
    apvt_req = models.CharField(max_length=50, choices=APVT, default="Yes", blank=True, null=True)
    image = models.ImageField(upload_to='Budget/Image', blank=True, null=True)

    def __str__(self):
        return str(self.trim_cost)

class Care_Level(models.Model):
    b_job_no = models.ForeignKey(BudgetPreCost, related_name="care_level", on_delete=models.CASCADE, blank=True, null=True)
    trim_cost = models.ForeignKey(TrimCostItems, related_name="ctrim_cost", on_delete=models.CASCADE, blank=True, null=True)
    tt_cons = models.FloatField(default=0, blank=True, null=True)
    tt_ex_pct = models.FloatField(default=0, blank=True, null=True)
    grand_tt_cons = models.FloatField(default=0, blank=True, null=True)
    tt_rate = models.FloatField(default=0, blank=True, null=True)
    sub_tt_amount = models.FloatField(default=0, blank=True, null=True)
    tt_qty_dzn = models.FloatField(default=0, blank=True, null=True)
    grand_tt_amount = models.FloatField(default=0, blank=True, null=True)
    tt_pcs = models.FloatField(default=0, blank=True, null=True)
    avg_tt_cons = models.FloatField(default=0, blank=True, null=True)
    avg_ex_pct = models.FloatField(default=0, blank=True, null=True)
    avg_grand_tt_cons = models.FloatField(default=0, blank=True, null=True)
    avg_tt_rate = models.FloatField(default=0, blank=True, null=True)
    avg_sub_tt_amount = models.FloatField(default=0, blank=True, null=True)
    avg_tt_qty_dzn = models.FloatField(default=0, blank=True, null=True)
    avg_grand_tt_amount = models.FloatField(default=0, blank=True, null=True)
    avg_tt_pcs = models.FloatField(default=0, blank=True, null=True)
    inserted_by = models.ForeignKey(Account, on_delete=models.SET_NULL, related_name="care_insert_by", null=True, blank=True)
    insert_date = models.DateTimeField(default=now, blank=True, null=True)
    
    def __str__(self):
        return str(self.b_job_no)

class Care_level_Items(models.Model):
    care_level = models.ForeignKey(Care_Level, related_name="care_items", on_delete=models.CASCADE, blank=True, null=True)
    color_size = models.ForeignKey(ColorSizeItems, related_name="cl_colorsize", on_delete=models.CASCADE, blank=True, null=True)
    po_no = models.CharField(max_length=200, blank=True, null=True)
    gmts_item = models.CharField(max_length=200, blank=True, null=True)
    country = models.CharField(max_length=200, blank=True, null=True)
    color = models.CharField(max_length=200, blank=True, null=True)
    gmts_size = models.CharField(max_length=200, blank=True, null=True)
    item_color = models.CharField(max_length=200, blank=True, null=True)
    item_sizes = models.CharField(max_length=200, blank=True, null=True)
    cons = models.FloatField(default=0, blank=True, null=True)
    ex_pct = models.FloatField(default=0, blank=True, null=True)
    tt_cons = models.FloatField(default=0, blank=True, null=True)
    rate = models.FloatField(default=0, blank=True, null=True)
    amount = models.FloatField(default=0, blank=True, null=True)
    tt_qty = models.FloatField(default=0, blank=True, null=True)
    tt_amount = models.FloatField(default=0, blank=True, null=True)
    placement = models.FloatField(default=0, blank=True, null=True)
    pcs = models.FloatField(default=0, blank=True, null=True)

    def __str__(self):
        return str(self.care_level)

# Embellishment Cost DB
class EmbellishmentCost(models.Model):
    b_job_no = models.ForeignKey(BudgetPreCost, related_name='embl_cost', on_delete=models.CASCADE, null=True, blank=True)
    tt_rate = models.FloatField(default=0, blank=True, null=True)
    tt_amount = models.FloatField(default=0, blank=True, null=True)
    inserted_by = models.ForeignKey(Account, on_delete=models.SET_NULL, related_name="embl_insert_by", null=True, blank=True)
    insert_date = models.DateTimeField(default=now, blank=True, null=True)

    def __str__(self):
        return str(self.b_job_no)
    
class EmbellishmentCostItem(models.Model):
    STATUS = (
        ('Active', 'Active'),
        ('Inactive', 'Inactive'),
    )
    embellishment_cost = models.ForeignKey(EmbellishmentCost, related_name='embl_items', on_delete=models.CASCADE, null=True, blank=True)
    cost_name = models.CharField(max_length=200, blank=True, null=True)
    type_name = models.CharField(max_length=200, blank=True, null=True)
    body_part = models.CharField(max_length=200, blank=True, null=True)
    country = models.CharField(max_length=200, blank=True, null=True)
    emb_supplier = models.CharField(max_length=200, blank=True, null=True)
    cons_dzn = models.FloatField(default=0, blank=True, null=True)
    rate = models.FloatField(default=0, blank=True, null=True)
    amount = models.FloatField(default=0, blank=True, null=True)
    status = models.CharField(max_length=50, choices=STATUS, default="Active", blank=True, null=True)

    def __str__(self):
        return str("%s-%s" %(self.embellishment_cost, self.id))

class EmbConsCosting(models.Model): #Embellishment consumption entry form for 1 dzn
    b_job_no = models.ForeignKey(BudgetPreCost, related_name="embcons_level", on_delete=models.CASCADE, blank=True, null=True)
    embl_cost = models.ForeignKey(EmbellishmentCostItem, related_name="embcons_cost", on_delete=models.CASCADE, blank=True, null=True)
    tt_cons = models.FloatField(default=0, blank=True, null=True)
    tt_rate = models.FloatField(default=0, blank=True, null=True)
    tt_amount = models.FloatField(default=0, blank=True, null=True)
    avg_tt_cons = models.FloatField(default=0, blank=True, null=True)
    avg_tt_rate = models.FloatField(default=0, blank=True, null=True)
    avg_tt_amount = models.FloatField(default=0, blank=True, null=True)
    inserted_by = models.ForeignKey(Account, on_delete=models.SET_NULL, related_name="embcons_insert_by", null=True, blank=True)
    insert_date = models.DateTimeField(default=now, blank=True, null=True)
    
    def __str__(self):
        return str(self.embl_cost)

class EmbConsCosting_Items(models.Model): #Embellishment consumption entry form items for 1 dzn
    emb_cons_costing = models.ForeignKey(EmbConsCosting, related_name="embcons_items", on_delete=models.CASCADE, blank=True, null=True)
    color_size = models.ForeignKey(ColorSizeItems, related_name="emb_colorsize", on_delete=models.CASCADE, blank=True, null=True)
    po_no = models.CharField(max_length=200, blank=True, null=True)
    country = models.CharField(max_length=200, blank=True, null=True)
    gmts_item = models.CharField(max_length=200, blank=True, null=True)
    color = models.CharField(max_length=200, blank=True, null=True)
    gmts_size = models.CharField(max_length=200, blank=True, null=True)
    cons = models.FloatField(default=0, blank=True, null=True)
    ex_pct = models.FloatField(default=0, blank=True, null=True)
    tt_cons = models.FloatField(default=0, blank=True, null=True)
    rate = models.FloatField(default=0, blank=True, null=True)
    amount = models.FloatField(default=0, blank=True, null=True)

    def __str__(self):
        return str(self.emb_cons_costing)

# Wash Cost all DB start
class WashCost(models.Model):
    b_job_no = models.ForeignKey(BudgetPreCost, related_name='wash_cost', on_delete=models.CASCADE, null=True, blank=True)
    tt_rate = models.FloatField(default=0, blank=True, null=True)
    tt_amount = models.FloatField(default=0, blank=True, null=True)
    inserted_by = models.ForeignKey(Account, on_delete=models.SET_NULL, related_name="wash_insert_by", null=True, blank=True)
    insert_date = models.DateTimeField(default=now, blank=True, null=True)

    def __str__(self):
        return str(self.b_job_no)

class WashCost_Items(models.Model):
    STATUS = (
        ('Active', 'Active'),
        ('Inactive', 'Inactive'),
    )
    wash_cost = models.ForeignKey(WashCost, related_name='wash_items', on_delete=models.CASCADE, null=True, blank=True)
    cost_name = models.CharField(max_length=200, blank=True, null=True)
    cost_type = models.CharField(max_length=200, blank=True, null=True)
    country = models.CharField(max_length=200, blank=True, null=True)
    cons_dzn = models.FloatField(default=0, blank=True, null=True)
    rate = models.FloatField(default=0, blank=True, null=True)
    amount = models.FloatField(default=0, blank=True, null=True)
    status = models.CharField(max_length=50, choices=STATUS, default="Active", blank=True, null=True)

    def __str__(self):
        return str(self.wash_cost)

class WashConsCosting(models.Model): # Wash cost consumption entry form
    b_job_no = models.ForeignKey(BudgetPreCost, related_name="washcons_cost", on_delete=models.CASCADE, blank=True, null=True)
    wash_cost = models.ForeignKey(WashCost_Items, related_name="washcons_cost", on_delete=models.CASCADE, blank=True, null=True)
    w_tt_cons = models.FloatField(default=0, blank=True, null=True)
    w_tt_ex_pct = models.FloatField(default=0, blank=True, null=True)
    w_grand_tt_cons = models.FloatField(default=0, blank=True, null=True)
    w_tt_rate = models.FloatField(default=0, blank=True, null=True)
    w_sub_tt_amount = models.FloatField(default=0, blank=True, null=True)
    w_grand_tt_qty = models.FloatField(default=0, blank=True, null=True)
    w_grand_tt_amount = models.FloatField(default=0, blank=True, null=True)
    w_avg_tt_cons = models.FloatField(default=0, blank=True, null=True)
    w_avg_ex_pct = models.FloatField(default=0, blank=True, null=True)
    w_avg_grand_tt_cons = models.FloatField(default=0, blank=True, null=True)
    w_avg_tt_rate = models.FloatField(default=0, blank=True, null=True)
    w_avg_sub_tt_amount = models.FloatField(default=0, blank=True, null=True)
    w_avg_grand_tt_qty = models.FloatField(default=0, blank=True, null=True)
    w_avg_grand_tt_amount = models.FloatField(default=0, blank=True, null=True)
    inserted_by = models.ForeignKey(Account, on_delete=models.SET_NULL, related_name="wc_insert_by", null=True, blank=True)
    insert_date = models.DateTimeField(default=now, blank=True, null=True)
    
    def __str__(self):
        return str(self.b_job_no)

class WashConsCosting_Items(models.Model): # Wash cost consumption item entry form
    wash_cons_cost = models.ForeignKey(WashConsCosting, related_name="wcons_items", on_delete=models.CASCADE, blank=True, null=True)
    color_size = models.ForeignKey(ColorSizeItems, related_name="wc_colorsize", on_delete=models.CASCADE, blank=True, null=True)
    w_po_no = models.CharField(max_length=200, blank=True, null=True)
    w_country = models.CharField(max_length=200, blank=True, null=True)
    w_gmts_item = models.CharField(max_length=200, blank=True, null=True)
    w_color = models.CharField(max_length=200, blank=True, null=True)
    w_gmts_size = models.CharField(max_length=200, blank=True, null=True)
    w_item_qty = models.IntegerField(default=0, blank=True, null=True)
    w_cons = models.FloatField(default=0, blank=True, null=True)
    w_ex_pct = models.FloatField(default=0, blank=True, null=True)
    w_tt_cons = models.FloatField(default=0, blank=True, null=True)
    w_rate = models.FloatField(default=0, blank=True, null=True)
    w_amount = models.FloatField(default=0, blank=True, null=True)
    w_tt_qty = models.FloatField(default=0, blank=True, null=True)
    w_tt_amount = models.FloatField(default=0, blank=True, null=True)
    w_pcs = models.FloatField(default=0, blank=True, null=True)

    def __str__(self):
        return str(self.wash_cons_cost)
# Wash Cost all DB end