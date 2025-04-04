



def input_to_int_():
    while True:
        try:
            numbers = ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9")
            num1 = int(input("Choose your first number: "))
            num2 = int(input("Choose your second number: "))
            user_choice = input("Enter operator (+, -, *, /) or 'q' to exit: ")
        
        
        except ValueError as e:
            return None
        except ZeroDivisionError as e:
            print("Can't divide by zero. Choose a valid number")
        except Exception as e:
            print('Error:', e)


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
