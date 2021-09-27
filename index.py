import sys, math

# # Print all colors
# for i in range(0, 16):
#     for j in range(0, 16):
#         code = str(i * 16 + j)
#         sys.stdout.write(u"\u001b[38;5;" + code + "m " + code.ljust(4))
#     print (u"\u001b[0m")

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

# gradient("Hello, tester.", colors.red_to_pink)
# gradient("iridi - beautify your console.logs", colors.orange_to_magenta)



def testgradient(string, colorArr, bold=False):

    length = len(string)
    colorStops = len(colorArr);

    if type(colorArr[0]) == str and colorArr[0].startswith("#"):
        for i in range(0, colorStops):
            color = colorArr[i].lstrip("#")
            rgbColors = tuple(int(color[i:i+2], 16) for i in (0, 2, 4))

            colorArr[i] = {
                "r": rgbColors[0],
                "g": rgbColors[1],
                "b": rgbColors[2],
            }

    r = int(colorArr[0]["r"])
    g = int(colorArr[0]["g"])
    b = int(colorArr[0]["b"])

    for i in range(0, colorStops):
        diffR = int(colorArr[1]["r"] - r)
        diffG = int(colorArr[1]["g"] - g)
        diffB = int(colorArr[1]["b"] - b)

    print('\033[1m') if bold else ''

    for i in range(0, length):

        print(f"\x1b[38;2;{r};{g};{b}m" + string[i], end = '')

        r += int(diffR/length)
        g += int(diffG/length)
        b += int(diffB/length)

    print (u"\u001b[0m")

testgradient("Try this string I suppose maybe even a longer one if I want", [{"r": 238, "g": 9, "b": 121}, {"r": 255, "g": 106, "b": 0}], bold=True)
testgradient("Try this string I suppose maybe even a longer one if I want", [{"r": 238, "g": 9, "b": 121}, {"r": 255, "g": 106, "b": 0}])
testgradient("Try this string I suppose maybe even a longer one if I want", ["#fafa3b", "#ab8290"])