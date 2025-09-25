from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.template.loader import render_to_string
from .models import Order, OrderItem
from .forms import OrderCreateForm
from cart.cart import Cart


def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            if request.user.is_authenticated:
                order.user = request.user
                # Pre-fill user information if available
                order.first_name = request.user.first_name or form.cleaned_data['first_name']
                order.last_name = request.user.last_name or form.cleaned_data['last_name']
                order.email = request.user.email or form.cleaned_data['email']
                if hasattr(request.user, 'profile'):
                    profile = request.user.profile
                    order.address = profile.address or form.cleaned_data['address']
                    order.city = profile.city or form.cleaned_data['city']
                    order.postal_code = profile.postal_code or form.cleaned_data['postal_code']
            else:
                order.first_name = form.cleaned_data['first_name']
                order.last_name = form.cleaned_data['last_name']
                order.email = form.cleaned_data['email']
                order.address = form.cleaned_data['address']
                order.city = form.cleaned_data['city']
                order.postal_code = form.cleaned_data['postal_code']
            
            order.save()
            
            for item in cart:
                OrderItem.objects.create(
                    order=order,
                    product=item['product'],
                    price=item['price'],
                    quantity=item['quantity']
                )
            
            # Clear the cart
            cart.clear()
            return render(request, 'orders/order/created.html', {'order': order})
    else:
        form = OrderCreateForm()
        if request.user.is_authenticated:
            # Pre-fill form with user data
            form.fields['first_name'].initial = request.user.first_name
            form.fields['last_name'].initial = request.user.last_name
            form.fields['email'].initial = request.user.email
            if hasattr(request.user, 'profile'):
                profile = request.user.profile
                form.fields['address'].initial = profile.address
                form.fields['city'].initial = profile.city
                form.fields['postal_code'].initial = profile.postal_code
    
    return render(request, 'orders/order/create.html', {'cart': cart, 'form': form})


@login_required
def order_list(request):
    orders = Order.objects.filter(user=request.user)
    return render(request, 'orders/order/list.html', {'orders': orders})


@login_required
def order_detail(request, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user)
    return render(request, 'orders/order/detail.html', {'order': order})
