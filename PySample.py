def safe_division():
    while True:
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            result = num1 / num2
            print(f"Result: {result}")
            break  # Exit the loop if successful
        except ZeroDivisionError:
            print("Error: Division by zero is not allowed. Please try again.")
        except ValueError:
            print("Error: Invalid input. Please enter numeric values.")
        except Exception as e:
            print(f"Unexpected error: {e}")
            print("Let's try again...\n")

# Run the function
safe_division() 