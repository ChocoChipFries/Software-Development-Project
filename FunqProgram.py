# Final Data Structures
class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

# Side-effect-free functions
def calculate_total_price(cart):
    return sum(item['price'] for item in cart.items)

# Higher-order function
def apply_discount(discount):
    def calculate_discounted_price(price):
        return price * (1 - discount)
    return calculate_discounted_price

# Function as parameter and return value
def process_items(cart, item_processor):
    return [item_processor(item) for item in cart.items]

# Use of closures / anonymous functions
def generate_discounted_prices(cart, discount):
    return process_items(cart, apply_discount(discount))

# Example usage
if __name__ == "__main__":
    # Initializing the shopping cart
    my_cart = ShoppingCart()

    # Adding items to the cart
    my_cart.add_item({'name': 'Laptop', 'price': 1200})
    my_cart.add_item({'name': 'Headphones', 'price': 100})
    my_cart.add_item({'name': 'Mouse', 'price': 20})

    # Calculating total price
    total_price = calculate_total_price(my_cart)
    print(f"Total Price: ${total_price}")

    # Applying a 10% discount
    discount_rate = 0.1
    discounted_prices = generate_discounted_prices(my_cart, discount_rate)
    print(f"Discounted Prices: {discounted_prices}")
