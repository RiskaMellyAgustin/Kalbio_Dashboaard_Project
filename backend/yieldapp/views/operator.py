# yieldapp/views/operator.py
# yieldapp/views/operator.py
from django.shortcuts import render, get_object_or_404, redirect
from ..forms.operator_forms import * # <--- UBAH MENJADI SEPERTI INI
from ..models.operator import OperatorYieldData
from django.shortcuts import render, get_object_or_404, redirect
from django.db import transaction
from ..forms.operator_forms import * # Impor semua form yang benar
from ..models.operator import OperatorYieldData
from ..models.core import BatchInfo

@transaction.atomic
def input_filling(request):
    if request.method == 'POST':
        form = CreateBatchForm(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data

            # 1. Buat objek BatchInfo baru
            new_batch = BatchInfo.objects.create(
                batch_number=cleaned_data['batch_number'],
                product=cleaned_data['product'],
                start_date=cleaned_data['tanggal_proses']
            )

            # 2. Buat objek OperatorYieldData yang terhubung
            yield_instance = OperatorYieldData.objects.create(
                batch=new_batch,
                tanggal_proses=cleaned_data['tanggal_proses'],
                
                # --- PASTIKAN BAGIAN INI MENYIMPAN DATA BARU ---
                formulation_output_kg=cleaned_data['formulation_output_kg'],
                formulation_output_pcs=cleaned_data['formulation_output_pcs'],
                # ---------------------------------------------
                
                filling_output=cleaned_data['filling_output']
            )

            # 3. Arahkan ke form selanjutnya
            return redirect('operator_dashboard')
    else:
        form = CreateBatchForm()
    
    return render(request, 'yieldapp/operator/input_form.html', {
        'form': form, 
        'proses': 'Langkah 1: Formulasi & Filling (Mulai Batch Baru)'
    })


def input_inspection(request, pk):
    data = get_object_or_404(OperatorYieldData, pk=pk)
    if request.method == 'POST':
        form = InspectionForm(request.POST, instance=data)
        if form.is_valid():
            form.save()
            data.batch.status = 'Inspection'
            data.batch.save()
            return redirect('batch_process_view', batch_pk=data.batch.pk)
    else:
        form = InspectionForm(instance=data)
    # Render template partial untuk modal
    return render(request, 'yieldapp/operator/partials/form_partial.html', {
        'form': form, 'proses': 'Input Hasil Inspeksi'
    })

def input_assembly(request, pk):
    data = get_object_or_404(OperatorYieldData, pk=pk)
    if request.method == 'POST':
        form = AssemblyForm(request.POST, instance=data)
        if form.is_valid():
            form.save()
            data.batch.status = 'Assembly'
            data.batch.save()
            return redirect('batch_process_view', batch_pk=data.batch.pk)
    else:
        form = AssemblyForm(instance=data)
    return render(request, 'yieldapp/operator/partials/form_partial.html', {
        'form': form, 'proses': 'Input Hasil Assembly'
    })

def input_blistering(request, pk):
    data = get_object_or_404(OperatorYieldData, pk=pk)
    if request.method == 'POST':
        form = BlisteringForm(request.POST, instance=data)
        if form.is_valid():
            form.save()
            data.batch.status = 'Blistering'
            data.batch.save()
            return redirect('batch_process_view', batch_pk=data.batch.pk)
    else:
        form = BlisteringForm(instance=data)
    return render(request, 'yieldapp/operator/partials/form_partial.html', {
        'form': form, 'proses': 'Input Hasil Blistering'
    })

def input_packaging(request, pk):
    data = get_object_or_404(OperatorYieldData, pk=pk)
    if request.method == 'POST':
        form = PackagingForm(request.POST, instance=data)
        if form.is_valid():
            form.save()
            data.batch.status = 'Packaging'
            data.batch.save()
            return redirect('batch_process_view', batch_pk=data.batch.pk)
    else:
        form = PackagingForm(instance=data)
    return render(request, 'yieldapp/operator/partials/form_partial.html', {
        'form': form, 'proses': 'Input Hasil Packaging'
    })

def input_handover(request, pk):
    data = get_object_or_404(OperatorYieldData, pk=pk)
    if request.method == 'POST':
        form = HandoverForm(request.POST, instance=data)
        if form.is_valid():
            form.save()
            data.batch.status = 'Completed'
            data.batch.save()
            return redirect('operator_dashboard')
    else:
        form = HandoverForm(instance=data)
    return render(request, 'yieldapp/operator/partials/form_partial.html', {
        'form': form, 'proses': 'Input Hasil Handover'
    })