# Write a program that counts the number of vowels in a sentence.

# To count the number of vowels in a sentence, I first define a set containing the vowels ('a', 'e', 'i', 'o', 'u'). Then, I convert the input sentence to lowercase to ensure consistent comparison with lowercase vowels. After initializing a counter for vowels, I iterate through each character in the sentence, incrementing the counter whenever a vowel is encountered. Finally, I return the total count of vowels in the sentence, providing a simple and efficient solution to determine the number of vowels present.

def count_vowels(sentence):
    # Define a set of vowels
    vowels = {'a', 'e', 'i', 'o', 'u'}

    # Convert the sentence to lowercase to handle both lowercase and uppercase vowels
    sentence = sentence.lower()

    # Initialize a counter for vowels
    vowel_count = 0

    # Iterate through each character in the sentence
    for char in sentence:
        # Check if the character is a vowel
        if char in vowels:
            vowel_count += 1

    return vowel_count

def main():
    # Prompt the user to enter a sentence
    sentence = input("Enter a sentence: ")

    # Call the function to count vowels
    num_vowels = count_vowels(sentence)

    # Print the number of vowels in the sentence
    print("Number of vowels:", num_vowels)

if __name__ == "__main__":
    main()
