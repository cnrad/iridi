import sys, math

# Print all colors
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
    # need to list all gradients, come up with scalable names

def gradient(string, color):

    # if not colors[color]:
    #     print('bruh pick again')

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

gradient("Hello, tester.", colors.red_to_pink)
gradient("iridi - beautify your console.logs", colors.orange_to_magenta)

print("\x1b[38;2;40;177;249m test \u001b[0m")



def testgradient(string, colorArr):

    # if not colors[color]:
    #     print('bruh pick again')

    length = len(string)
    index = 0
    array = []

    red = 100
    green = 0
    blue = 20

    for j in range(0, 105):

        red += 1
        blue += 1
        green += 1

        print(f"\x1b[38;2;{red};{green};{blue}m" + "a")

    print (u"\u001b[0m")

testgradient("Try this string I suppose", [{"r": 200, "g": 255, "b": 100}, {"r": 100, "g": 55, "b": 250}])