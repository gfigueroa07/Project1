

# Validate user input or prompt user to exit program
def input_to_int_():
    while True:
    # Take 1st valid number from user
        user_choice1 = input("Choose your first number or enter 'q' to exit: ")
    # Exit program if user enters "q"
        if user_choice1.lower() == "q":
            print("Exiting the program")
            return None
        try:
    # Convert input into valid number
            num1 = int(user_choice1)
            break
        except ValueError:
            print("Please enter a valid number or enter 'q' to exit: ")
    while True:
    # Take 2nd valid number from user
        user_choice2 = input("Choose your first number or enter 'q' to exit: ")
    # Exit program if user enters "q"
        if user_choice2.lower() == "q":
            print("Exiting program")
            return None
        try:
    # Convert input into valid number
            num2 = int(user_choice2)
            break
        except ValueError:
            print("Please enter a valid number")
    return num1, num2
calc = input_to_int_()
print(calc)

def calculate():
    while True:
        try:
            num1 = int(input("Enter first number: "))
            num2 = int(input("Enter second number: "))
            user_choice = input("Enter operator (+, -, *, /) or 'q' to exit: ")


            if user_choice == "q".lower():
                break
            elif user_choice == '+':
                result = num1 + num2
            elif user_choice == '-':
                result = num1 - num2
            elif user_choice == '*':
                result = num1 * num2
            elif user_choice == '/':
                if num2 == 0:
                    raise ZeroDivisionError("Dont divide by zero, uncultured mf xD")
                result = num1 / num2
            else:
                raise ValueError("It's a calculator... use numbers instead bruh")

            print("Result:", result)
            break

        except ValueError as e:
            print("Invalid input:", e)
        except ZeroDivisionError as e:
            print("Error:", e)

calculate()
