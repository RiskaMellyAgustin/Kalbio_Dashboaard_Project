# views/dashboard.py
from django.shortcuts import render
from ..models.operator import OperatorYieldData

def yield_dashboard(request):
    # Ambil semua data yield yang sudah diinput
    # 'select_related' membuat query lebih efisien dengan mengambil data dari tabel BatchInfo dan Product dalam satu kali jalan
    all_yield_data = OperatorYieldData.objects.select_related('batch', 'batch__product').all()
    
    context = {
        'yield_data_list': all_yield_data
    }
    return render(request, 'yieldapp/dashboard/yield_summary.html', context)