

message1 =  "i r a d f e \
            r m w s a e \
            e e t x a p \
            e x" 

message2 = "e o f o a t u t w t a t h b t t h e r w t \
e y i x h n e d x e d l g x s o l e x"


message3 = "o e u n i d r e w o b m i c o a l u x r l \
           m a k s e t t n o o t n r s e e i o t n h \
           h o o"

message = message3

def clean_message(message):
    # remove the spaces from the message
    message = list(filter(lambda x: x != "", message.split(" ")))

    # calculate the number of letters in the message
    num_letters = len(message)

    # list the factorization of num_letters
    factors = []
    for i in range(1, num_letters + 1):
        if num_letters % i == 0:
            factors.append(i)

    # print the factors that most closely match the dimensions of a square
    # print(factors[int(len(factors) / 2) - 1], factors[int(len(factors) / 2)])

    # set the dimensions of the square
    a = factors[int(len(factors) / 2) - 1]
    b = factors[int(len(factors) / 2)]

    return message, a, b


# print the cipher in a square
def print_square(message):
    message, a, b = clean_message(message)
    for i in range(0, a):
        for j in range(0, b):
            print(message[i + j * a], end=" ")
        print(" ")


# print the message column down
def column_down(message):
    message, a, b = clean_message(message)
    for i in range(0, a):
        for j in range(0, b):
            print(message[i + j * a], end="")

# print the message column down
def column_up(message):
    message, a, b = clean_message(message)
    for i in range(a-1, -1, -1):
        for j in range(b-1, -1, -1):
            print(message[i + j * a], end="")

# print the message reversecolumn down
def reverse_column_down(message):
    message, a, b = clean_message(message)
    for i in range(a-1, -1, -1):
        for j in range(0, b):
            print(message[i + j * a], end="")

# print the message in a right to left column
def right_to_left(message):
    message, a, b = clean_message(message)
    for i in range(0, a):
        for j in range(b-1, -1, -1):
            print(message[i + j * a], end="")


def attempt_to_decrypt(message):
    # print the message
    print_square(message)
    print(" ")
    column_down(message)
    print(" ")
    reverse_column_down(message)
    print(" ")
    column_up(message)
    print(" ")
    right_to_left(message)
    print(" ")

attempt_to_decrypt(message1)
attempt_to_decrypt(message2)
attempt_to_decrypt(message3)
