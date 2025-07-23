# views/mstd.py
from django.shortcuts import render, redirect, get_object_or_404
from ..models.master import Product
from ..forms.mstd_forms import ProductForm

# View untuk menampilkan semua produk dan menambah produk baru
def product_list(request):
    products = Product.objects.all().order_by('name')
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_list') # Kembali ke halaman list setelah berhasil
    else:
        form = ProductForm()
        
    return render(request, 'yieldapp/mstd/product_list.html', {
        'form': form,
        'products': products
    })

# View untuk mengedit produk yang sudah ada
def product_edit(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm(instance=product)
        
    return render(request, 'yieldapp/mstd/product_edit.html', {'form': form})