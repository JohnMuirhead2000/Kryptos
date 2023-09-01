# This function assumes potential answers are in a file called potential_answers.txt. I line per potential answer
# It will write the result to test_results.txt. It uses thr 100 most common English words.


def sort():
    # Open the input file for reading
    with open('test_results.txt', 'r') as input_file:
        # Read the lines of the input file into a list
        lines = input_file.readlines()

    # Sort the lines by the second word in each line (converted to an integer)
    sorted_lines = sorted(lines, key=lambda line: int(line.split()[1]), reverse=True)

    # Open the output file for writing
    with open('sorted_test_results.txt', 'w') as output_file:
        # Write the sorted lines to the output file
        output_file.writelines(sorted_lines)


def check_line(guess):
    total_matches = 0
    words = guess.split()
    last_word = words[-1]
    matches = []
    with open("common_words.txt") as file:
        for line in file:
            word = line.rstrip().upper()
            if word in last_word:
                matches.append(word)
                total_matches = total_matches + 1

    print(last_word + " had " + str(total_matches) + " matches : " + str(matches))

    # now total matches should be the number of English words in the line

    # we can now write this information to a file
    with open('test_results.txt', 'a') as f:
        f.write(guess[:-1] + " " + str(total_matches) + "\n")

    #sort()


def check_potential_answers():
    # first read in the strings
    with open('potential_answers.txt', 'r') as file:
        # Read the content of the file and store it as a list of strings
        lines = file.readlines()

    for line in lines:
        # for each line see how many English words (form the 1000 most common) it has
        check_line(line)


if __name__ == '__main__':
    check_potential_answers()
