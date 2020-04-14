from django.shortcuts import render
from .models import *
# Create your views here.

def home(request):
    customers = Customer.objects.all()
    orders = Order.objects.all()

    total_orders = orders.count()
    delivered = orders.filter(status="Delivered").count()
    pending = orders.filter(status="Pending").count()


    context = {'customers':customers,'orders':orders, 'total_orders':total_orders,'delivered':delivered,'pending':pending}

    return render(request, 'accounts/dashboard.html', context)

def customer(request, pk_id):
    customer = Customer.objects.get(id=pk_id)
    orders = customer.order_set.all()
    total_order = orders.count()

    context = {'customer':customer,'orders':orders,'total_order':total_order}

    return render(request, 'accounts/customer.html',context)

def product(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'accounts/product.html', context)