# Write a program that takes an integer as input and returns true if the input is a power of two.

# I determined if a given integer is a power of two by checking if it's positive and if its binary representation contains only one '1' bit, achieved by performing a bitwise AND operation with the integer's predecessor. In the main function, I prompted the user for an integer input, then checked if it's a power of two using the `is_power_of_two` function, and printed the result.

def is_power_of_two(n):
    # Check if the number is positive and a power of two
    return n > 0 and (n & (n - 1)) == 0

def main():
    # Prompt the user to enter an integer
    num = int(input("Enter an integer: "))

    # Check if the input is a power of two
    result = is_power_of_two(num)

    # Print the result
    print("Is", num, "a power of two?", result)

if __name__ == "__main__":
    main()
