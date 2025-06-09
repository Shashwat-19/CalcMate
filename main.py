print("Welcome to Calculator 1956")
print("--------------------------")
print("Operations Available:")
print("--------------------------")

result = None  

while True:
    try:
        if result is None:
            a = float(input("Enter the first number: "))
        else:
            print(f"\nCurrent result: {result}")
            a = result

        b = float(input("Enter the second number: "))
    except ValueError:
        print("Invalid input! Please enter valid numbers.")
        continue

    print("\nChoose an operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        result = a + b
        operation = "Addition"
    elif choice == '2':
        result = a - b
        operation = "Subtraction"
    elif choice == '3':
        result = a * b
        operation = "Multiplication"
    elif choice == '4':
        if b != 0:
            result = a / b
            operation = "Division"
        else:
            print("Error: Division by zero!")
            continue
    elif choice == '5':
        print("Exiting calculator...")
        break
    else:
        print("Invalid choice! Please enter a number from 1 to 5.")
        continue

    print(f"\n{operation} result: {result}")
    print("----------------------------")

    while True:
        cont = input("Do you want to continue using the result? (yes/new/exit): ").lower()
        if cont == 'yes':
            break  # Use the current result as the next 'a'
        elif cont == 'new':
            result = None  # Reset result to allow new input
            break
        elif cont == 'exit':
            print("Exiting calculator...")
            exit()
        else:
            print("Invalid input! Please enter 'yes', 'new' or 'exit'.")

print("Thank you for using Calculator 1956!")
