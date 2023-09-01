# Define the morse code mapping for letters
morse_code_dict = {
    "A": ".-", "B": "-...", "C": "-.-.", "D": "-..", "E": ".", "F": "..-.", "G": "--.", "H": "....", "I": "..",
    "J": ".---", "K": "-.-", "L": ".-..", "M": "--", "N": "-.", "O": "---", "P": ".--.", "Q": "--.-", "R": ".-.",
    "S": "...", "T": "-", "U": "..-", "V": "...-", "W": ".--", "X": "-..-", "Y": "-.--", "Z": "--..",
    "1": ".----", "2": "..---", "3": "...--", "4": "....-", "5": ".....",
    "6": "-....", "7": "--...", "8": "---..", "9": "----.", "0": "-----"
}

# Inverse mapping of morse code dictionary (for decoding)
inverse_morse_code_dict = {v: k for k, v in morse_code_dict.items()}


def generate_key_map(key_number):
    # Define the default key_map
    default_key_map = {
        "3": "..", "2": ".-", "7": ".X", "9": "-.", "6": "--", "8": "-X", "4": "X.", "1": "X-", "5": "XX"
    }

    # Convert the key_number to a string to iterate through its digits
    key_number_str = str(key_number)

    # Generate the new key_map based on the given key_number
    new_key_map = {}
    for i, digit in enumerate(key_number_str):
        new_key_map[digit] = list(default_key_map.values())[i]

    return new_key_map


def cipher_to_plain_text_v3(cipher_text_with_spaces, key_number, inverse_morse_code_dict):
    # Remove spaces from the cipher_text
    cipher_text = cipher_text_with_spaces.replace(" ", "")

    # Generate key_map based on the provided key_number
    key_map = generate_key_map(key_number)

    # Convert cipher text to morse code
    morse_code = "".join([key_map.get(c, "") for c in cipher_text])

    # Initialize variables
    plain_text = ""
    current_morse_char = ""

    # Decode morse code to plain text
    for char in morse_code:
        if char != "X":
            current_morse_char += char
        else:
            plain_text += inverse_morse_code_dict.get(current_morse_char, "?")
            current_morse_char = ""
            if morse_code[morse_code.index(char) + 1] == "X":
                plain_text += " "

    # Append the last character if exists
    if current_morse_char:
        plain_text += inverse_morse_code_dict.get(current_morse_char, "?")

    return plain_text


def write_to_file(string_to_write):
    with open("out_put_stuff.txt", "a") as file:
        file.write(string_to_write + "\n")


if __name__ == '__main__':

    # Test the function with new cipher_text_with_spaces
    cipher_text_with_spaces = """
    4  2  7  6  8  7  4  6  8  2  7  6  2  6  3  6
    2  4  7  7  6  8  6  8  7  8  6  5  7  5  6  1
    7  2  1  5  6  4  7  6  5  7  4  6  5  7  4  3
    1  4  2  6  8  2  4  1  7  6  5  6  7  3  1  4
    """

    key_number = 327968415
    plain_text_v3 = cipher_to_plain_text_v3(cipher_text_with_spaces, key_number, inverse_morse_code_dict)

    write_to_file(plain_text_v3)



