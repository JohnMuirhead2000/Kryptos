# This script reads in text from the document text_to_index.txt and prints out the word
# in the index specified by numbers. NOTE, indexing starts form 1 here.
# it delineates by spaces. Case does not matter.
def print_indices(indices):
    # Open the file for reading
    with open('text_to_index.txt', 'r') as file:
        # Read the content of the file and store it as a list of strings
        lines = file.readlines()

    # Join the list of strings into a single string
    data = ' '.join(lines)

    # Split the string into words and store them as a list of strings
    words = data.split()

    for index in indices:
        print(words[index - 1])


if __name__ == '__main__':
    numbers = [1, 3, 5, 7]
    print_indices(numbers)
