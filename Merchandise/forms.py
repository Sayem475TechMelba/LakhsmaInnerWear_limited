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

############# Budget Library ###########        
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

############### ALL Merchandising Forms #############


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
    
########### All Budget Costing Form ###########
class BudgetPreCostForm(forms.ModelForm):
    
    class Meta:
        model = BudgetPreCost
        exclude = ['inserted_by', 'job_no']
