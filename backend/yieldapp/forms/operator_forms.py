# yieldapp/forms/operator_forms.py
from django import forms
from ..models.operator import OperatorYieldData
from ..models.master import Product

# ... (import dan form lainnya biarkan sama) ...

class CreateBatchForm(forms.Form):
    batch_number = forms.CharField(
        label="Nomor Batch", 
        max_length=50,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Contoh: BATCH-001'})
    )
    product = forms.ModelChoiceField(
        queryset=Product.objects.all(), 
        label="Pilih Produk",
        empty_label="--- Pilih Produk ---",
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    tanggal_proses = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}), 
        label="Tanggal Proses"
    )

    # --- TAMBAHKAN INPUT INI ---
    formulation_output_kg = forms.FloatField(
        label="Hasil Formulasi Aktual (Kg)",
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )
    formulation_output_pcs = forms.IntegerField(
        label="Hasil Formulasi (setara Pcs)",
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )
    # ---------------------------

    filling_output = forms.IntegerField(
        label="Hasil Filling Aktual (Pcs)", 
        min_value=0,
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )

class InspectionForm(forms.ModelForm):
    class Meta:
        model = OperatorYieldData
        fields = ['inspection_output']

class AssemblyForm(forms.ModelForm):
    class Meta:
        model = OperatorYieldData
        fields = ['assembly_output']

class BlisteringForm(forms.ModelForm):
    class Meta:
        model = OperatorYieldData
        fields = ['blistering_output']

class PackagingForm(forms.ModelForm):
    class Meta:
        model = OperatorYieldData
        fields = ['packaging_output']

class HandoverForm(forms.ModelForm):
    class Meta:
        model = OperatorYieldData
        fields = ['handover_output']