# Ask the user for two numbers and an operation
num1 = float(input ("Enter first number: ")) 
num2 = float(input ("Enter second number: ")) 
operation = input("Enter the operation (+, -, *, /): ") 

# Perform the operation based on user input
if operation == "+":
    result = num1 + num2  
    print("Sum: ", result)  
elif operation == '-':
    result = num1 - num2  
    print("Difference: ", result)  
elif operation == '*':
    result = num1 * num2  
    print("Product: ", result) 
elif operation == '/':
    if num2 != 0:
        result = num1 / num2
        print(f"{num1} / {num2} = {result}")
    else:
        print("Error: Division by zero is not allowed.")

else:
     print("Invalid operation")