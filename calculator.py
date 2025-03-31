# Multiply
def multiply(x, y):
    answer = x * y
    return answer
# Divide
def division(x, y):
    answer = x / y
    return answer
# Substract
def substract(x,y):
    answer = x - y
    return answer
# Add
def add(x, y):
    answer = x + y
    return answer

# User input to use calculator

user_answer = False

while not user_answer:
    user_answer = input("What would you like to do?\n1. Multiply\n2. Divide\n3. Add\n4. Substract\nEnter your answer (1,2,3,4) or 'q' to Quit:\n")
    if user_answer == "q":
        print("You have exited the program.")
        user_answer = True
    elif user_answer == "1":
        num_1 = int(input("Choose your first number:\n"))
        num_2 = int(input("Choose your second number:\n"))
        print(f"Your total is: {multiply(num_1, num_2)}")
    elif user_answer == "2":
        num_1 = int(input("Choose your first number:\n"))
        num_2 = int(input("Choose your second number:\n"))
        print(f"Your total is: {division(num_1, num_2)}")
    elif user_answer == "3":
        num_1 = int(input("Choose your first number:\n"))
        num_2 = int(input("Choose your second number:\n"))
        print(f"Your total is: {add(num_1, num_2)}")
    elif user_answer == "4":
        num_1 = int(input("Choose your first number:\n"))
        num_2 = int(input("Choose your second number:\n"))
        print(f"Your total is: {substract(num_1, num_2)}")
    else:
        user_answer = False


