# Write a program that prints the numbers from 1 to 100. For multiples of 3, print "Fizz"; for  multiples of 5, print "Buzz"; and for numbers that are multiples of both 3 and 5, print  "FizzBuzz".

# I solved the FizzBuzz problem by iterating through numbers from 1 to 100, checking each number for divisibility by 3, 5, or both, and printing "Fizz", "Buzz", "FizzBuzz", or the number itself accordingly.

def fizzbuzz():
    for num in range(1, 101):
        # Check if the number is a multiple of both 3 and 5
        if num % 3 == 0 and num % 5 == 0:
            print("FizzBuzz")
        # Check if the number is a multiple of 3
        elif num % 3 == 0:
            print("Fizz")
        # Check if the number is a multiple of 5
        elif num % 5 == 0:
            print("Buzz")
        # If the number is not a multiple of 3 or 5, print the number itself
        else:
            print(num)

def main():
    fizzbuzz()

if __name__ == "__main__":
    main()

