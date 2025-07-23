# models/operator.py
from django.db import models
from .core import BatchInfo

class OperatorYieldData(models.Model):
    batch = models.ForeignKey(BatchInfo, on_delete=models.CASCADE, related_name="yield_data") # Tambahkan related_name
    tanggal_proses = models.DateField(help_text="Tanggal dimulainya proses batch ini")
   
    # --- FIELD BARU DITAMBAHKAN DI SINI ---
    formulation_output_kg = models.FloatField(
        null=True, blank=True, verbose_name="Output Formulasi (Kg)"
    )
    formulation_output_pcs = models.PositiveIntegerField(
        null=True, blank=True, verbose_name="Output Formulasi (setara Pcs)"
    )
    # ------------------------------------
    
    # ... (field-field output lainnya tetap sama)
    filling_output = models.PositiveIntegerField(null=True, blank=True)
    inspection_output = models.PositiveIntegerField(null=True, blank=True)
    assembly_output = models.PositiveIntegerField(null=True, blank=True)
    blistering_output = models.PositiveIntegerField(null=True, blank=True)
    packaging_output = models.PositiveIntegerField(null=True, blank=True)
    handover_output = models.PositiveIntegerField(null=True, blank=True, verbose_name="Handover to Warehouse (pcs)")

    created_at = models.DateTimeField(auto_now_add=True)

    # --- LOGIKA PERHITUNGAN DIMULAI DI SINI ---
    
    @property
    def final_yield_percentage(self):
        """Menghitung persentase yield akhir."""
        # Pastikan data yang dibutuhkan ada untuk menghindari error
        if self.handover_output is None or self.batch.product.theoritical_yield_pcs == 0:
            return 0.0
        
        # Rumus: (Output Aktual / Output Teoretis) * 100
        yield_calc = (self.handover_output / self.batch.product.theoritical_yield_pcs) * 100
        return round(yield_calc, 2) # Dibulatkan 2 angka desimal

    @property
    def target_yield(self):
        """Mengambil target yield dari master product."""
        return self.batch.product.target_yield_percent

    @property
    def is_achieved(self):
        """Mengecek apakah yield mencapai target."""
        return self.final_yield_percentage >= self.target_yield

    # Anda juga bisa menambahkan properti untuk setiap yield per proses
    @property
    def filling_yield_percentage(self):
        if self.filling_output is None or self.batch.product.theoritical_yield_pcs == 0:
            return 0.0
        return round((self.filling_output / self.batch.product.theoritical_yield_pcs) * 100, 2)
        
    def __str__(self):
        return f"Batch {self.batch} - {self.tanggal_proses}"

    class Meta:
        verbose_name = "Data Yield Operator"
        verbose_name_plural = "Data Yield Operator"
        ordering = ['-tanggal_proses', 'batch']