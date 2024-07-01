def calculator():
    while True:
        print("Welcome to the calculator app!")
        start = input("Press 's' to start or 'q' to quit: ").lower()

        if start == 'q':
            print("Exiting the app. Goodbye!")
            break

        if start == 's':
            try:
                num1 = int(input("Enter the first number: "))
                num2 = int(input("Enter the second number: "))
                operator = input("Enter the operator (+, -, *, /, //, **): ")

                if operator == "+":
                    print(f"The result is: {num1 + num2}")
                elif operator == "-":
                    print(f"The result is: {num1 - num2}")
                elif operator == "*":
                    print(f"The result is: {num1 * num2}")
                elif operator == "/":
                    print(f"The result is: {num1 / num2}")
                elif operator == "//":
                    print(f"The result is: {num1 // num2}")
                elif operator == "**":
                    print(f"The result is: {num1 ** num2}")
                else:
                    print("Invalid operator")
            except ValueError:
                print("Invalid input. Please enter numerical values.")
        else:
            print("Invalid input. Please press 's' to start or 'q' to quit.")

# Run the calculator app
calculator()
