import math

# --- Basic Operations ---
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b

def square_root(x):
    return math.sqrt(x)

def factorial(x):
    return math.factorial(int(x))

def natural_log(x):
    return math.log(x)

def power(x, b):
    return math.pow(x, b)

def menu():
    print("\n--- Extended Scientific Calculator ---")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Square Root (root(x))")
    print("6. Factorial (x!)")
    print("7. Natural Log (ln(x))")
    print("8. Power (x^b)")
    print("9. Exit")

    choice = input("Enter choice: ")
    if choice == '9': return False

    num1 = float(input("Enter first value: "))

    if choice in ['1', '2', '3', '4', '8']:
        num2 = float(input("Enter second value (exponent/divisor/etc): "))
        if choice == '1': print("Result:", add(num1, num2))
        elif choice == '2': print("Result:", subtract(num1, num2))
        elif choice == '3': print("Result:", multiply(num1, num2))
        elif choice == '4': print("Result:", divide(num1, num2))
        elif choice == '8': print("Result:", power(num1, num2))
    else:
        if choice == '5': print("Result:", square_root(num1))
        elif choice == '6': print("Result:", factorial(num1))
        elif choice == '7': print("Result:", natural_log(num1))

    return True

if __name__ == "__main__":
    while menu():
        pass