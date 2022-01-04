from django import forms
from django.forms import fields
from .models import *

class BankForm(forms.ModelForm):
    class Meta:
        model = Bank
        fields = '__all__'

class BankBranchForm(forms.ModelForm):
    class Meta:
        model = BankBranch
        fields = '__all__'

class BankAddressForm(forms.ModelForm):
    class Meta:
        model = BankAddress
        fields = '__all__'
        
class PurchaseForm(forms.ModelForm):
    class Meta:
        model = PurchaseBank
        exclude = ['purchase_no', 'inserted_by']

class Sh_Form(forms.ModelForm):
    class Meta:
        model = ShipmentChalan
        exclude = ['chalan_no', 'inserted_by']
        
class Sh_ItemsForm(forms.ModelForm):
    class Meta:
        model = ShipmentChalanItems
        fields = '__all__'

        