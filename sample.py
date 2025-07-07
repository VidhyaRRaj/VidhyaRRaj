def factorial(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def factorial_of_two_numbers(a, b):
    return factorial(a), factorial(b)

# Example usage:
num1 = 5
num2 = 3
fact1, fact2 = factorial_of_two_numbers(num1, num2)
print(f"Factorial of {num1} is {fact1}")
print(f"Factorial of {num2} is {fact2}")