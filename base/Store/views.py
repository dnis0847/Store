from django.shortcuts import render, redirect
from .forms import ProductForm, SearchForm
from .models import Product

def product_list(request):
    available_products = Product.available_objects.all()
    context = {'available_products': available_products}
    return render(request, 'product_list.html', context)

def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            article = form.cleaned_data['article']
            brand = form.cleaned_data['brand']
            description = form.cleaned_data['description']
            rating = form.cleaned_data['rating']
            quantity = form.cleaned_data['quantity']
            existing_product = Product.objects.filter(title=title, article=article).first()
            if existing_product:
                existing_product.quantity += quantity
                existing_product.save()
            else:
                Product.objects.create(title=title, article=article, brand=brand, description=description, rating=rating, quantity=quantity)
            return redirect('Store:product_list')
    else:
        form = ProductForm()
    return render(request, 'add_product.html', {'form': form})

def product_detail(request, product_id):
    product = Product.objects.get(pk=product_id)
    return render(request, 'product_detail.html', {'product': product})

def product_search_view(request):
    form = SearchForm()
    query = None
    results = []
    
    if 'query' in request.GET:
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            results = Product.objects.filter(title__icontains=query)
    
    return render(request, 'product_search.html', {'form': form, 'query': query, 'results': results})