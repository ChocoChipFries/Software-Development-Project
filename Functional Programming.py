# Define a final data structure (immutable list)
immutable_list = [1, 2, 3, 4, 5]

# Define side-effect-free functions
def square(x):
    return x ** 2

def is_even(x):
    return x % 2 == 0

# Higher-order function taking a function as a parameter
def apply_operation(operation, iterable):
    return [operation(x) for x in iterable]

# Function returning a function (closure)
def create_adder(increment):
    def adder(x):
        return x + increment
    return adder

# Example usage of functional programming concepts
squared_values = apply_operation(square, immutable_list)
print("Squared Values:", squared_values)

even_numbers = apply_operation(is_even, immutable_list)
print("Even Numbers:", even_numbers)

# Using a closure to create an adder function
add_five = create_adder(5)
add_ten = create_adder(10)

incremented_values = [add_five(x) for x in immutable_list]
print("Values incremented by 5:", incremented_values)

# Higher-order function with reduce
sum_of_squares = reduce(lambda x, y: x + y, apply_operation(square, immutable_list))
print("Sum of Squares:", sum_of_squares)
