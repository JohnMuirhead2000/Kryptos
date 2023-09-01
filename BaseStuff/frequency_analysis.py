import matplotlib.pyplot as plt

global frequency_dict
frequency_dict = {}

# information obtained from https://www3.nd.edu/~busiforc/handouts/cryptography/letterfrequencies.html
global real_frequency
real_frequency = [('E', .12), ('T', .09), ('A', .08), ('O', .077), ('I', .073), ('N', .0695), ('S', .0628), ('R', .0602),
                  ('H', .0592),
                  ('D', .0432), ('L', .0398), ('U', .0288), ('C', .0271), ('M', .0261), ('F', .0230), ('Y', .0211), ('W', .0209),
                  ('G', .0203),
                  ('P', .0182), ('B', .0149), ('V', .0111), ('K', .0069), ('X', .0017), ('Q', .0011), ('J', .001),
                  ('Z', .0007)]


def process(char):
    global frequency_dict
    if char in frequency_dict:
        frequency_dict[char] = frequency_dict[char] + 1
    else:
        frequency_dict[char] = 1


def fill_dict():
    global frequency_dict

    f = open("/Users/jack/git/present/oprkyts/BaseStuff/cipher.txt")
    char = f.read(1)
    while char:
        print("here")
        process(char)
        char = f.read(1)
    f.close()


def convert_to_percent(frequency_list):
    total = 0
    for val in frequency_list:
        total = total + val[1]
    new_list = []
    for val in frequency_list:
        new_list.append((val[0], val[1] / total))
    return new_list


def make_bar_graph(frequency_list):
    plt.rcParams["figure.figsize"] = [7.00, 3.50]
    plt.rcParams["figure.autolayout"] = True
    ind = []
    fre = []
    for item in frequency_list:
        ind.append(item[0])
        fre.append(item[1])

    plt.bar(ind, fre)

    plt.show()


def update_char(char, frequency_list):
    global real_frequency
    # real_frequency is reality
    # frequency_list is what we have
    # char is what we are updating

    for i in range(len(frequency_list)):
        if frequency_list[i][0] == char:
            # we have found the correct index
            return real_frequency[i][0]
    return char


def generate_potential_solution(frequency_list):
    f1 = open("/Users/jack/git/oprkyts/BaseStuff/cipher.txt")
    f2 = open("semi_plain.txt", "w")
    char = f1.read(1)
    while char:
        new_char = update_char(char, frequency_list)
        f2.write(new_char)
        char = f1.read(1)
    f1.close()
    f2.close()


def perform_analysis():
    global frequency_dict

    # first fill the dictionary
    fill_dict()

    # first eliminate non=letters and sort it
    frequency_dict = {k: v for k, v in frequency_dict.items() if k.isalpha() and k.isupper()}
    frequency_list = sorted(frequency_dict.items(), key=lambda x: x[1], reverse=True)
    frequency_list = convert_to_percent(frequency_list)
    print(frequency_list)

    # plot the letter frequency for the cipher text
    make_bar_graph(frequency_list)
    make_bar_graph(real_frequency)

    generate_potential_solution(frequency_list)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    perform_analysis()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
