import math

def show_menu():
    print("\n--- Python Power Calculator ---")
    print("1. Add (+)")
    print("2. Subtract (-)")
    print("3. Multiply (*)")
    print("4. Divide (/)")
    print("5. Remainder (%)")
    print("6. Exponent (**)")
    print("7. Floor Division (//)")
    print("8. Exit")

def start_calculator():
    while True:
        show_menu()
        choice = input("\nPick an operator (1-8): ")

        if choice == '8':
            print("Goodbye!")
            break

        # Check if the choice is a valid number between 1 and 7
        if choice in ('1', '2', '3', '4', '5', '6', '7'):
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))

                if choice == '1':
                    print(f"Result: {num1} + {num2} = {num1 + num2}")
                elif choice == '2':
                    print(f"Result: {num1} - {num2} = {num1 - num2}")
                elif choice == '3':
                    print(f"Result: {num1} * {num2} = {num1 * num2}")
                elif choice == '4':
                    if num2 != 0:
                        print(f"Result: {num1} / {num2} = {num1 / num2}")
                    else:
                        print("Error: You can't divide by zero!")
                elif choice == '5':
                    print(f"Result: Remainder of {num1}/{num2} is {num1 % num2}")
                elif choice == '6':
                    print(f"Result: {num1} to the power of {num2} is {num1 ** num2}")
                elif choice == '7':
                    if num2 != 0:
                        print(f"Result: Integer division is {num1 // num2}")
                    else:
                        print("Error: Cannot perform floor division by zero.")
            except ValueError:
                print("Invalid input! Please enter numeric values.")
        else:
            print("Invalid selection, please pick 1-8.")

# Run the program
start_calculator()