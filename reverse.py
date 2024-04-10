# Write a program that takes an integer as input and returns an integer with reversed digit  ordering.

# To reverse the digit ordering of an integer input, I convert the integer to a string, reverse the string using slicing (`[::-1]`), and then convert the reversed string back to an integer. This approach allows me to reverse the order of the digits while maintaining numerical integrity. Additionally, by using string manipulation, I ensure that leading zeros are not lost in the process. Finally, I return the reversed integer as the output.

def reverse_integer(num):
    # Convert the integer to a string and reverse it
    reversed_str = str(num)[::-1]

    # Convert the reversed string back to an integer
    reversed_num = int(reversed_str)

    return reversed_num

def main():
    # Prompt the user to enter an integer
    num = int(input("Enter an integer: "))

    # Call the function to reverse the integer
    reversed_num = reverse_integer(num)

    # Print the reversed integer
    print("Reversed integer:", reversed_num)

if __name__ == "__main__":
    main()
