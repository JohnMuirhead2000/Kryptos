# Press the green button in the gutter to run the script.


def build(rows, columns, message):
    blocks = []
    for i in range(columns):
        print(i)
        if i % rows == 0:
            print(" time to build block " + str(i / 3))
            print("i = " + str(i))
            new_block = []
            new_block.append([message[i], message[i+1], message[i+2]])
            new_block.append([message[i + columns], message[i + columns + 1], message[i + columns + 2]])
            new_block.append([message[i + columns*2], message[i + columns*2 + 1], message[i + columns*2 + 2]])




def do_swag(rows, columns, message):
   blocks = build(rows, columns, message)





if __name__ == '__main__':
    key = [[1, 2, 3],
           [2, 3, 1],
           [3, 1, 2]]
    rows = 3
    columns = 20
    message = "HETTPHUEMHEEZFISIALNHRNAIOSESRLDWESOERRWWTTNOOBIROEDNL"
    do_swag(rows, columns, message)