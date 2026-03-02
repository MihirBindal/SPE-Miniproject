import math

def square_root(x):
    return math.sqrt(x)

def factorial(x):
    return math.factorial(int(x))

def natural_log(x):
    return math.log(x)

def power(x, b):
    return math.pow(x, b)

def menu():
    print("\n--- Scientific Calculator ---")
    print("1. Square Root (√x)")
    print("2. Factorial (x!)")
    print("3. Natural Log (ln(x))")
    print("4. Power (x^b)")
    print("5. Exit")

    choice = input("Enter choice: ")
    if choice == '5': return False

    num = float(input("Enter value: "))
    if choice == '1': print("Result:", square_root(num))
    elif choice == '2': print("Result:", factorial(num))
    elif choice == '3': print("Result:", natural_log(num))
    elif choice == '4':
        exp = float(input("Enter exponent: "))
        print("Result:", power(num, exp))
    return True

if __name__ == "__main__":
    while menu():
        pass