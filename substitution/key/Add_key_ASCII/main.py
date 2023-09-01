
## NOTE, RENAME FILE AND METHODS. CODE HERE  NOTE COMPLETE
def print_hi(numbers):
    print(len(numbers))
    seen_vals = []
    val = 0
    for number in numbers:
        print(number_to_letter((number % 26) + 1) + " ", end='')
    print(" ")

    # get the unique numbers
    for number in numbers:
        if number not in seen_vals:
            seen_vals.append(number)
            val = val + 1
    print(val)
    
    for number in numbers:
        if number not in seen_vals:
            seen_vals.append(number)
            val = val + 1


def number_to_letter(num):
    return chr(num + 96)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
