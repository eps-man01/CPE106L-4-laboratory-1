def multiply(number, choice, custom_multiplier=None):
    if choice == 1:
        return number * 2
    elif choice == 2:
        return number * 3
    elif choice == 3:
        return number * custom_multiplier


if __name__ == "__main__":
    try:
        num = int(input("Enter an integer: "))

        print("\nChoose an option:")
        print("1. Multiply by 2")
        print("2. Multiply by 3")
        print("3. Multiply by custom number")

        choice = int(input("Enter your choice (1, 2, or 3): "))

        if choice == 1 or choice == 2:
            result = multiply(num, choice)
            print(f"\nResult: {result}")
        elif choice == 3:
            custom_num = int(input("Enter the custom integer multiplier: "))
            result = multiply(num, choice, custom_num)
            print(f"\nResult: {result}")
        else:
            print("\nInvalid choice! Please select 1, 2, or 3.")

    except ValueError:
        print("\nError: Invalid input! Please enter valid integers only.")
