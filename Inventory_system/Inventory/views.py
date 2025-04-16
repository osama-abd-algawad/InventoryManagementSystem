from django.shortcuts import render,redirect,get_object_or_404
from django.db import transaction
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import RegistrationForm
from .models import Product,Category,Sales,SalesDetail
from django.db.models import Sum
from django.forms import inlineformset_factory
from .forms import ProductForm,CategoryForm,SalesForm,SalesDetailForm

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            login(request, user)
            messages.success(request, "Registration successful!")
            return redirect('Inventory:product_list')
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = RegistrationForm()

    return render(request, 'registration/register.html', {'form': form})

@login_required
def product_list(request):
    products = Product.objects.all().order_by("name")
    context = {'products':products}
    return render(request,'product/product_list.html',context)

@login_required
def delete_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == 'POST':
        product.delete()
        return redirect('Inventory:product_list') 
    return render(request, 'product/delete_product.html', {'product': product})

@login_required
def manage_product(request, product_id=None):
    if product_id:
        product = get_object_or_404(Product, id=product_id)
    else:
        product = None

    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('Inventory:product_list')  
    else:
        form = ProductForm(instance=product)

    return render(request, 'product/manage_product.html', {'form': form, 'product': product})


# category
@login_required
def category_list(request):
    categories = Category.objects.all().order_by("name")
    context = {'categories':categories}
    return render(request,'category/category_list.html',context)

@login_required
def delete_category(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    if request.method == 'POST':
        category.delete()
        return redirect('Inventory:category_list')
    return render(request, 'category/delete_category.html', {'category': category})

@login_required
def manage_category(request, category_id=None):
    if category_id:
        category = get_object_or_404(Category, id=category_id)
    else:
        category = None

    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('Inventory:category_list')  
    else:
        form = CategoryForm(instance=category)

    return render(request, 'category/manage_category.html', {'form': form, 'category': category})

# Sales Views
@login_required
def sales_list(request):
    sales = Sales.objects.all().order_by('-sale_date')
    return render(request, 'sales/sales_list.html', {'sales': sales})

@login_required
def sales_detail(request, pk):
    sale = get_object_or_404(Sales, pk=pk)
    sales_details = SalesDetail.objects.filter(sale=sale)
    return render(request, 'sales\sales.detail.html', {'sale': sale, 'sales_details': sales_details})


@login_required
def create_sales(request):
    SalesDetailFormSet = inlineformset_factory(
        Sales,
        SalesDetail,
        form=SalesDetailForm,
        extra=3,
        can_delete=False,
    )

    if request.method == 'POST':
        sales_form = SalesForm(request.POST)
        formset = SalesDetailFormSet(request.POST)

        if sales_form.is_valid() and formset.is_valid():
            with transaction.atomic():
                sale = sales_form.save(commit=False)
                sale.user = request.user
                sale.total_amount = 0
                sale.save()
                
                has_errors = False 
                for detail in formset.save(commit=False):
                    
                    
                    if detail.product  and detail.quantity_sold > 0:
                        if detail.quantity_sold > detail.product.quantity:
                            detail.add_error('quantity_sold', f"Not enough stock for {detail.product.name}.")
                            has_errors = True
                            continue

                        detail.sale = sale
                        detail.price = detail.product.price
                        detail.total_price = detail.quantity_sold * detail.price
                        detail.product.quantity -= detail.quantity_sold
                        detail.product.save()
                        sale.total_amount += detail.total_price
                        detail.save()
                
                if has_errors:
                    return render(request, 'sales/create_sales.html', {
                        'sales_form': sales_form,
                        'formset': formset,
                    })
                sale.save()
                return redirect('Inventory:sales_list')

    else:
        sales_form = SalesForm()
        formset = SalesDetailFormSet()

    return render(request, 'sales/create_sales.html', {
        'sales_form': sales_form,
        'formset': formset,
})

@login_required
def inventory_report(request):
    products = Product.objects.all()

    sales_summary = Sales.objects.aggregate(
        total_sales=Sum('total_amount')
    )

    sales_details = SalesDetail.objects.values(
        'product__name'
    ).annotate(
        total_sold=Sum('quantity_sold'),
        total_earnings=Sum('total_price')
    ).order_by('-total_earnings')

    categories = Category.objects.all()

    context = {
        'products': products,
        'sales_summary': sales_summary,
        'sales_details': sales_details,
        'categories': categories,
    }
    return render(request, 'report.html', context)