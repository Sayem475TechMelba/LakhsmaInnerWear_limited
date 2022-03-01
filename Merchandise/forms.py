from django import forms
from django.forms import fields
from .models import *

############### ALL Library Forms #############
class LibBuyerForm(forms.ModelForm):
    class Meta:
        model = LibraryBuyer
        fields = '__all__'

class LibCompanyForm(forms.ModelForm):
    class Meta:
        model = LibraryCompany
        fields = '__all__'
            
        
class LibCompAddressForm(forms.ModelForm):
    class Meta:
        model = LibraryCompAddress
        fields = '__all__'

class LibProdDeptForm(forms.ModelForm):
    class Meta:
        model = LibraryProdDept
        fields = '__all__'

class LibProdSubDeptForm(forms.ModelForm):
    class Meta:
        model = LibraryProdSubDept
        fields = '__all__'
        
class LibProductCateForm(forms.ModelForm):
    class Meta:
        model = LibraryProductCate
        fields = '__all__'

class LibTeamLeaderForm(forms.ModelForm):
    class Meta:
        model = LibraryTeamLeader
        fields = '__all__'

class LibDealingMerchantForm(forms.ModelForm):
    class Meta:
        model = LibraryDealingMerchant
        fields = '__all__'

class LibFactoryMerchantForm(forms.ModelForm):
    class Meta:
        model = LibraryFactoryMerchant
        fields = '__all__'

class LibSeasonForm(forms.ModelForm):
    class Meta:
        model = LibrarySeason
        fields = '__all__'

class LibRegionForm(forms.ModelForm):
    class Meta:
        model = LibraryRegion
        fields = '__all__'

class LibAgentForm(forms.ModelForm):
    class Meta:
        model = LibraryAgent
        fields = '__all__'

class LibClientForm(forms.ModelForm):
    class Meta:
        model = LibraryClient
        fields = '__all__'

class LibCurrencyForm(forms.ModelForm):
    class Meta:
        model = LibraryCurrency
        fields = '__all__'

class LibPackingForm(forms.ModelForm):
    class Meta:
        model = LibraryPacking
        fields = '__all__'

class LibShipModeForm(forms.ModelForm):
    class Meta:
        model = LibraryShipMode
        fields = '__all__'

class LibQualityForm(forms.ModelForm):
    class Meta:
        model = LibraryQualityLabel
        fields = '__all__'

class LibUnitForm(forms.ModelForm):
    class Meta:
        model = LibraryUnit
        fields = '__all__'

class LibShipmentTermForm(forms.ModelForm):
    class Meta:
        model = LibraryShipmentTerm
        fields = '__all__'

class LibDesignSourceForm(forms.ModelForm):
    class Meta:
        model = LibraryDesignSource
        fields = '__all__'

class LibCountryForm(forms.ModelForm):
    class Meta:
        model = LibraryCountry
        fields = '__all__'

class LibCountryTypeForm(forms.ModelForm):
    class Meta:
        model = LibraryCountryType
        fields = '__all__'
        
class LibCutOffForm(forms.ModelForm):
    class Meta:
        model = LibraryCutOff
        fields = '__all__'

class LibProductForm(forms.ModelForm):
    class Meta:
        model = LibraryProduct
        fields = '__all__'

class LibPaymentTermForm(forms.ModelForm):
    class Meta:
        model = LibraryPaymentTerm
        fields = '__all__'

class LibFabricationForm(forms.ModelForm):
    class Meta:
        model = LibraryFabrication
        fields = '__all__'

############# Budget Library Form ###########        
class LibCostingPerForm(forms.ModelForm):
    class Meta:
        model = LibraryCostingPer
        fields = '__all__'

class LibBodyPartForm(forms.ModelForm):
    class Meta:
        model = LibraryBodyPart
        fields = '__all__'

class LibBodyPartTypeForm(forms.ModelForm):
    class Meta:
        model = LibraryBodyPartType
        fields = '__all__'

class LibFabNatureForm(forms.ModelForm):
    class Meta:
        model = LibraryFabNature
        fields = '__all__'

class LibColorTypeForm(forms.ModelForm):
    class Meta:
        model = LibraryColorType
        fields = '__all__'
        
class LibFabricSourceForm(forms.ModelForm):
    class Meta:
        model = LibraryFabricSource
        fields = '__all__'

class LibFabricDescriptionForm(forms.ModelForm):
    class Meta:
        model = LibraryFabricDescription
        fields = '__all__'

class LibNominatedSuppForm(forms.ModelForm):
    class Meta:
        model = LibraryNominatedSupp
        fields = '__all__'

class LibDiaTypesForm(forms.ModelForm):
    class Meta:
        model = LibraryDiaTypes
        fields = '__all__'
        
class LibConsumptionBasisForm(forms.ModelForm):
    class Meta:
        model = LibraryConsumptionBasis
        fields = '__all__'

class LibColorSizeSensitiveForm(forms.ModelForm):
    class Meta:
        model = LibraryColorSizeSensitive
        fields = '__all__'

######### Yarn Library Form ########  

class LibYarnTypeForm(forms.ModelForm):
    class Meta:
        model = LibraryYarnType
        fields = '__all__'  

class LibYarnSupplierForm(forms.ModelForm):
    class Meta:
        model = LibraryYarnSupplier
        fields = '__all__'  

######## Conversion Library Form ########

class LibProcessForm(forms.ModelForm):
    class Meta:
        model = LibraryProcess
        fields = '__all__'

class LibKnittingForm(forms.ModelForm):
    class Meta:
        model = LibraryKnitting
        fields = '__all__'  

class LibDyeingForm(forms.ModelForm):
    class Meta:
        model = LibraryDyeing
        fields = '__all__'  

######## Trims Cost Library Form ########

class LibGroupsItemForm(forms.ModelForm):
    class Meta:
        model = LibraryGroupsItem
        fields = '__all__'

class LibTrimSourceForm(forms.ModelForm):
    class Meta:
        model = LibraryTrimSource
        fields = '__all__'

######## Embellishments Cost Library Form ########

class LibEmbCostNameForm(forms.ModelForm):
    class Meta:
        model = LibraryEmbCostName
        fields = '__all__'

class LibyEmbCostTypeForm(forms.ModelForm):
    class Meta:
        model = LibraryEmbCostType
        fields = '__all__'

######## Wash Cost Library Form ########

class LibWashCost_NameForm(forms.ModelForm):
    class Meta:
        model = LibraryWash_CostName
        fields = '__all__'

class LibywashCost_TypeForm(forms.ModelForm):
    class Meta:
        model = LibraryWash_CostType
        fields = '__all__'
############### ALL Merchandising Main Table Forms #############

class OrderEntryForm(forms.ModelForm):
    class Meta:
        model = OrderEntryInfo
        exclude = ['job_no','inserted_by']

class SmvItems_Form(forms.ModelForm):
    
    class Meta:
        model = SmvItems
        fields = '__all__'   

class PoDeatilsForm(forms.ModelForm):

    class Meta:
        model = PO_Details
        exclude = ['inserted_by', 'po_job_no']
        
class colorsize_ItemsForm(forms.ModelForm):
    class Meta:
        model = ColorSizeItems
        fields = '__all__' 

class AddPoDeatilsForm(forms.ModelForm):
    
    class Meta:
        model = PO_Details
        exclude = ['inserted_by']


##### All Budget Costing Form ########
class BudgetPreCostForm(forms.ModelForm):
    
    class Meta:
        model = BudgetPreCost
        exclude = ['inserted_by', 'job_no']
        
class FabricCostForm(forms.ModelForm):
    
    class Meta:
        model = FabricCost
        exclude = ['inserted_by', 'b_job_no']

class FabricItemForm(forms.ModelForm):
    class Meta:
        model = Fabric_Inline_Item
        fields = '__all__' 

class YarnCostForm(forms.ModelForm):
    
    class Meta:
        model = YarnCost
        exclude = ['inserted_by', 'b_job_no']

class YarnItemForm(forms.ModelForm):
    class Meta:
        model = Yarn_Inline_Item
        fields = '__all__' 

class ConversionCostForm(forms.ModelForm):
    
    class Meta:
        model = ConversionCost
        exclude = ['inserted_by', 'b_job_no']

class ConversionItemForm(forms.ModelForm):
    class Meta:
        model = Conversion_Inline
        fields = '__all__' 


class TrimCostForm(forms.ModelForm):
    
    class Meta:
        model = TrimCost
        exclude = ['inserted_by', 'b_job_no']

class TrimItemsForm(forms.ModelForm):
    class Meta:
        model = TrimCostItems
        fields = '__all__' 

class EmbellishmentCostForm(forms.ModelForm):
    class Meta:
        model = EmbellishmentCost
        exclude = ['inserted_by', 'b_job_no']

class EmbellishmentItemsForm(forms.ModelForm):
    class Meta:
        model = EmbellishmentCostItem
        fields = '__all__' 

class WashCostForm(forms.ModelForm):
    class Meta:
        model = WashCost
        exclude = ['inserted_by', 'b_job_no']

class WashCostItemsForm(forms.ModelForm):
    class Meta:
        model = WashCost_Items
        fields = '__all__' 
        
class CommercialCostForm(forms.ModelForm):
    class Meta:
        model = CommercialCost
        exclude = ['inserted_by', 'b_job_no']

class CommercialCostItemsForm(forms.ModelForm):
    class Meta:
        model = CommercialCost_Items
        fields = '__all__' 

class CommissionCostForm(forms.ModelForm):
    class Meta:
        model = CommissionCost
        exclude = ['inserted_by', 'b_job_no']

class CommissionCostItemsForm(forms.ModelForm):
    class Meta:
        model = CommissionCost_Items
        fields = '__all__' 