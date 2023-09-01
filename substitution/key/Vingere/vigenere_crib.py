def convert_letter(cipher, crib):
    position_letter = ord(cipher) - ord("A")
    position_key_letter = ord(crib) - ord("A")
    desired_index = ((position_letter - position_key_letter) % 26)
    letter = chr(desired_index + ord("A"))
    return letter


def check_start(start, crib):
    potential_key = []

    for i in range(len(crib)):
        ket_letter = convert_letter(start[i], crib[i])
        potential_key.append(ket_letter)

    cip = ""
    for x in start:
        cip += x
    key = ""
    for x in potential_key:
        key += x

    with open('/Users/jack/git/present/oprkyts/substitution/key/Vingere/potential_key.txt', 'a') as f:
        f.write("from the letters " + cip + " we would get the key " + key + "\n")
    # write this start to the output file


def get_key_from_crib(crib):
    print(crib)
    with open('/Users/jack/git/present/oprkyts/substitution/key/Vingere/cipher.txt', 'r') as file:
        # Read the content of the file and store it as a list of strings
        lines = file.readlines()

    # Join the list of strings into a single string
    data = ' '.join(lines)

    print(data)
    crib_starts = []
    for i in range(len(data) - len(crib) + 1):
        next_guess = []
        for j in range(len(crib)):
            next_guess.append(data[i + j])
        crib_starts.append(next_guess)
    print(crib_starts)
    for start in crib_starts:
        check_start(start, crib)

if __name__ == '__main__':
    crib = "THEMEETING"
    get_key_from_crib(crib)
