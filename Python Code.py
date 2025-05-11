import math

def is_fibonacci_number(num):
    if num < 0:
        return False
    # A number is Fibonacci if and only if one of (5*num^2 + 4) or (5*num^2 - 4) is a perfect square
    def is_perfect_square(x):
        s = int(math.sqrt(x))
        return s * s == x

    return is_perfect_square(5 * num * num + 4) or is_perfect_square(5 * num * num - 4)

# Example usage:
num = int(input("Enter a number to check if it is a Fibonacci number: "))
if is_fibonacci_number(num):
    print(f"{num} is a Fibonacci number.")
else:
    print(f"{num} is not a Fibonacci number.")
