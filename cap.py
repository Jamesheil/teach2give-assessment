# Write a program that accepts a string as input, capitalizes the first letter of each word in the  string, and then returns the result string.

# I solved the problem by splitting the input string into words, capitalizing the first letter of each word using the `capitalize()` method, and then joining the capitalized words back into a single string.

def capitalize_first_letter_of_each_word(input_string):
    # Split the input string into individual words
    words = input_string.split()

    # Capitalize the first letter of each word and join them back together
    capitalized_words = [word.capitalize() for word in words]

    # Join the capitalized words into a single string
    result = ' '.join(capitalized_words)

    return result

def main():
    # Prompt the user to enter a string
    input_string = input("Enter a string: ")

    # Capitalize the first letter of each word
    result = capitalize_first_letter_of_each_word(input_string)

    # Print the result
    print("Result:", result)

if __name__ == "__main__":
    main()
