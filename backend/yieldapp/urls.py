from django.contrib import admin
from django.urls import path
 # mengimpor modul operator dari folder views
from yieldapp.views import operator, mstd, dashboard, dashboard_operator, landing

urlpatterns = [
    path('admin/', admin.site.urls),
      # JADIKAN PATH INI SEBAGAI HALAMAN UTAMA
    path('', landing.home_page, name='home'),
    
    # URLS UNTUK DASHBOARD OPERATOR BARU
    path('operator/dashboard/', dashboard_operator.operator_dashboard, name='operator_dashboard'),
    path('operator/dashboard/batch/<int:batch_pk>/', dashboard_operator.batch_process_view, name='batch_process_view'),
    # URL untuk Operator (Sudah Ada)
    path('input/filling/', operator.input_filling, name='input_filling'),
    path('input/inspection/<int:pk>/', operator.input_inspection, name='input_inspection'),
    # KEMUNGKINAN BESAR BARIS DI BAWAH INI YANG HILANG ATAU SALAH
    path('input/assembly/<int:pk>/', operator.input_assembly, name='input_assembly'),

    path('input/blistering/<int:pk>/', operator.input_blistering, name='input_blistering'),
    path('input/packaging/<int:pk>/', operator.input_packaging, name='input_packaging'),
    path('input/handover/<int:pk>/', operator.input_handover, name='input_handover'),
    # ... URL operator lainnya ...
    
    # Anda perlu halaman sukses setelah handover
    # path('success/', operator.success_view, name='operator_success'),
    
    # --- URL BARU UNTUK MSTD ---
    path('mstd/products/', mstd.product_list, name='product_list'),
    path('mstd/products/edit/<int:pk>/', mstd.product_edit, name='product_edit'),
    
    # --- URL BARU UNTUK DASHBOARD ---
    path('dashboard/', dashboard.yield_dashboard, name='yield_dashboard'),
]
