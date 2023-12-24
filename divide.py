def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Cannot divide by zero"

# Example usage for Division
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
print(f"Division: {divide(num1, num2)}")
