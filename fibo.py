# Write a program to generate the Fibonacci sequence up to 100.

# To generate the Fibonacci sequence up to the number 100, I first initialized the sequence with the first two numbers, 0 and 1. Then, using a while loop, I iteratively calculated subsequent Fibonacci numbers by adding the last two numbers in the sequence. I included a condition to break out of the loop when the next Fibonacci number exceeds 100. Finally, I returned the generated Fibonacci sequence containing all numbers up to 100. This approach ensures that the Fibonacci sequence is dynamically generated and efficiently returned within the specified limit.

def generate_fibonacci_sequence():
    # Initialize the first two Fibonacci numbers
    fib_sequence = [0, 1]

    # Generate subsequent Fibonacci numbers until reaching 100
    while True:
        next_fib = fib_sequence[-1] + fib_sequence[-2]
        if next_fib > 100:
            break
        fib_sequence.append(next_fib)

    return fib_sequence

def main():
    # Generate the Fibonacci sequence
    fibonacci_sequence = generate_fibonacci_sequence()

    # Print the Fibonacci sequence
    print("Fibonacci sequence up to 100:")
    print(fibonacci_sequence)

if __name__ == "__main__":
    main()
