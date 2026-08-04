def check_even_odd(number):
    if number % 2 == 0:
        return "Even"
    return "Odd"

if __name__ == "__main__":
    try:
        val = int(input("Enter an integer: "))
        print(f"Result: {val} is {check_even_odd(val)}.")
    except ValueError:
        print("Please enter a valid integer.")
