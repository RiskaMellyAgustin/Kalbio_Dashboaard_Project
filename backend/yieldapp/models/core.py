# yieldapp/models/core.py

from django.db import models
from .master import Product

class BatchInfo(models.Model):
    # Pilihan untuk field status, agar konsisten
    PROCESS_STAGES = [
        ('Formulation', 'Formulasi'),
        ('Filling', 'Filling'),
        ('Inspection', 'Inspeksi'),
        ('Assembly', 'Assembly'),
        ('Blistering', 'Blistering'),
        ('Packaging', 'Packaging'),
        ('Handover', 'Handover'),
        ('Completed', 'Selesai'),
    ]

    batch_number = models.CharField(max_length=50, unique=True)
    product = models.ForeignKey(Product, on_delete=models.PROTECT, related_name="batches")
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)

    # --- INI ADALAH FIELD BARU YANG DITAMBAHKAN ---
    status = models.CharField(
        max_length=50,
        choices=PROCESS_STAGES,
        default='Formulation', # Status awal saat batch pertama kali dibuat
        verbose_name="Status Proses"
    )
    # ----------------------------------------------

    def __str__(self):
        return f"{self.batch_number} - {self.product.name}"

    class Meta:
        verbose_name = "Informasi Batch"
        verbose_name_plural = "Informasi Batch"