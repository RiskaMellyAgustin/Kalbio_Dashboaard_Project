from django.contrib import admin
# Impor model yang relevan dari lokasi baru
from .models.core import BatchInfo
from .models.operator import OperatorYieldData
from .models.master import Product

# Daftarkan model yang sekarang digunakan
admin.site.register(Product)
admin.site.register(BatchInfo)
admin.site.register(OperatorYieldData)