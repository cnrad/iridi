import sys, math

for i in range(0, 16):
    for j in range(0, 16):
        code = str(i * 16 + j)
        sys.stdout.write(u"\u001b[38;5;" + code + "m " + code.ljust(4))
    print (u"\u001b[0m")

# ansi colors: 0-16 base colors. 17+ are gradients in groups of 5
# idea: split string into 5 sections, gradient it

class colors:
    red_to_pink = 160
    orange_to_magenta = 202
    green_to_blue = 28

def gradient(string, color):

    # if color not in colors:
    #     return print("not a color bruh lmfao u dumb")

    length = len(string)
    index = 0
    section = math.ceil(length/5) + index
    array = []

    for i in range(0, 5):
        array.append(string[index:section])
        index += math.ceil(length/5)
        section = math.ceil(length/5) + index

    for j in range(0, 5):
        code = str(color + j)
        sys.stdout.write(u"\u001b[38;5;" + code + "m" + array[j])

    print (u"\u001b[0m")


gradient("This is a test for gradient strings.", colors.red_to_pink)
gradient("This is a another test for gradient strings, but longer.", colors.orange_to_magenta)
gradient("Very cool af.", colors.green_to_blue)
