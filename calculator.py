# Simple Calculator

def calculator():
    # Prompting user to input two numbers
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    
    # Displaying available operations
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    
    # Taking operation input from the user
    choice = input("Enter your choice (1/2/3/4): ")
    
    # Performing calculation based on user's choice
    if choice == '1':
        result = num1 + num2
        print(f"The result of addition is: {result}")
    
    elif choice == '2':
        result = num1 - num2
        print(f"The result of subtraction is: {result}")
    
    elif choice == '3':
        result = num1 * num2
        print(f"The result of multiplication is: {result}")
    
    elif choice == '4':
        if num2 != 0:
            result = num1 / num2
            print(f"The result of division is: {result}")
        else:
            print("Error! Division by zero is not allowed.")
    
    else:
        print("Invalid input! Please select a valid operation.")

# Running the calculator function
calculator()
