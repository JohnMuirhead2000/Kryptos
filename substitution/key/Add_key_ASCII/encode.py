
def encode():
    msg = "148 154 155 172 145 152 152 157 154 159 \
            174 160 148 145 159 167 172 169 163 148 \
            154 155 172 145 152 152 169 154 173 173 \
            149 157 148 157 150 174 169 161 151 145 \
            149 154 174 163 154 140 148 156 150 157 \
            159 148 154 155 172 145 152 152 146 167 \
            163 168 147 153 140 149 158 174 159 153 \
            142 146 145 151 166 155 143 144 135 145 \
            168 159 148 154 155 172 145 152 152 167 \
            157 159 172 145 152 140 145 161 166 174 \
            148 138 134 145 152 165 175 156 135 137 \
            148 154 155 172 145 152 152 145 169 174 \
            162 145 136 137 158 169 172 155 152 159 \
            147 159 171 155 166 145 153 156"

    # msg = [137,178,177,190,184,99,152,189,179,185,169,114,177,178,184,110,162,191,170,114,194,178,182,110,165,188,174,192,176,99,181,189,165,174,190]
    msg_nums = []
    # take a message string and use additive keyword technique to encode it
    msg = "Hello World how are you doing today"
    keyword = "AMERICAN"
    numbers = []
    for i in range(len(msg)):
        key_val = ord(keyword[i % len(keyword)])
        current_letter = msg[i]
        print(ord(current_letter), end=",")
        letter = chr(ord(current_letter) + key_val)
        # convert to an ascii number
        msg_nums.append(ord(letter))

    print()
    keyword = "AMERICAN"

    '''
    # Take the msg string and split it into a list of integers
    msg = msg.split()
    
    
    # Convert the list of strings to a list of integers
    msg = [int(i) for i in msg]
    '''

    for i in range(len(msg)):

        key = "AMERICAN"

        current_char = key[i % len(key)]
        # print(current_char)

        # Subtract the current character from the current integer
        try:
            msg_nums[i] -= ord(current_char)
        except TypeError:
            pass

        print(msg_nums[i], end=",")

        # Convert the list of integers to a list of characters
        try:
            msg = [chr(i) for i in msg]
        except TypeError:
            pass

        # Join the list of characters into a string
        msg = "".join(msg)

    print()
    print(msg)

if __name__ == '__main__':
    encode()