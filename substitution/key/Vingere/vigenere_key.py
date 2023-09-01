import math


def convert_letter(letter, key_letter):
    # the letter we want will be the
    # index of: (letter + the index of the key_letter - 1) mod 26 (:
    position_letter = ord(letter) - ord("A")
    position_key_letter = ord(key_letter) - ord("A")
    desired_index = ((position_letter - position_key_letter) % 26)
    letter = chr(desired_index + ord("A"))
    return letter


def make_full_key(key, data):
    full_key = []
    for i in range(len(data)):
        full_key.append(key[i % len(key)])
    return full_key


def solve_using_key(key):
    with open('/Users/jack/git/present/oprkyts/substitution/key/Vingere/cipher.txt', 'r') as file:
        # Read the content of the file and store it as a list of strings
        lines = file.readlines()

    # Join the list of strings into a single string
    data = ' '.join(lines)


    # will convert the key to the full key for the cipher
    # ie; newton -> newtonnetwtonnewtonne...
    full_key = make_full_key(key, data)

    for i in range(len(data)):
        with open('/Users/jack/git/present/oprkyts/substitution/key/Vingere/test_results.txt', 'a') as f:
            letter = convert_letter(data[i], full_key[i])

            f.write(letter)


if __name__ == '__main__':
    key = "ONETHINGWASCERTAINTHATTHEWHITEKITTENHADHADNOTHINGT"
    solve_using_key(key)
