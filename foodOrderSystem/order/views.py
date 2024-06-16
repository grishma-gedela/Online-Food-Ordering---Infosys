from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from restaurant.models import foodItems

@login_required
def Cart(request):
    if 'cart' not in request.session:
        request.session['cart'] = {}
    
    cart = request.session['cart']
    cartDetails = {}
    totalCost = 0
    
    if request.method == 'POST':
        action = request.POST.get('action')
        item_id = request.POST.get('item_id')

        if action == 'add':
            if item_id in cart:
                cart[item_id] += 1
            else:
                cart[item_id] = 1
        elif action == 'remove':
            if item_id in cart:
                del cart[item_id]
        elif action == 'increment':
            if item_id in cart:
                cart[item_id] += 1
        elif action == 'decrement':
            if item_id in cart and cart[item_id] > 1:
                cart[item_id] -= 1

        request.session['cart'] = cart
        return redirect('cart')  # Redirect to the cart page to reflect changes
    
    for item_id, quantity in cart.items():
        item = foodItems.objects.get(id=item_id)
        totalCost += quantity * item.price
        cartDetails[item_id] = {"item": item, "quantity": quantity}

    return render(request, 'cart.html', {'cart': cartDetails, "totalCost": totalCost})
