
def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def main():
    while True:
        operation_choice = input("Do you need help with addition or subtraction? (Type 'add' or 'subtract'): ").lower()

        if operation_choice in ('add', 'subtract'):
            try:
                num1 = float(input("What is your first number: "))
                num2 = float(input("What is your second number: "))
            except ValueError:
                print("Invalid input. Please enter valid numbers.")
                continue

            if operation_choice == 'add':
                result = add(num1, num2)
                print(f"The sum of {num1} and {num2} is: {result}")
            elif operation_choice == 'subtract':
                result = subtract(num1, num2)
                print(f"The difference between {num1} and {num2} is: {result}")
        else:
            print("Invalid operation choice. Please type 'add' or 'subtract'.")

        another_calculation = input("Do you want to do another calculation? (yes/no): ").lower()
        if another_calculation != 'yes':
            break

if __name__ == "__main__":
    main()