def make_full_key(key, data):
    full_key = []
    for i in range(len(data)):
        full_key.append(key[i % len(key)])
    return full_key


def analize(numbers, keyword):
    full_key = make_full_key(keyword, numbers)
    print(full_key)

    for i in range(len(numbers)):
        key_val = ord(full_key[i])
        current_number = numbers[i]
        ##print("current number = " + str(current_number))
        print(chr(current_number - key_val), end="")


if __name__ == '__main__':
    numbers = [148, 154, 155, 172, 145, 152, 152, 157, 154, 159, 174, 160, 148]
    # numbers = [148, 174, 154, 149, 149, 159, 163, 142, 169]
    keyword = "PUZZLED"

    print(max(numbers))
    print(min(numbers))
    analize(numbers, keyword)
