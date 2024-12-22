def calculate_total(cart_items):
    if not cart_items: #for 0 items in the cart
        return "Cart is empty. Total Price: 0"
    
    total_price = sum(cart_items.values())
    if len(cart_items) > 5:
        total_price *= 0.9  # Apply 10% discount
    return f"Total Price: {int(total_price)}"

cart_items = {'Laptop': 50000, 'Headphones': 2000, 'Mouse': 500, 'Keyboard': 1500}
print(calculate_total(cart_items))