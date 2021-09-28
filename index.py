import sys, math

# # Print all colors
# for i in range(0, 16):
#     for j in range(0, 16):
#         code = str(i * 16 + j)
#         sys.stdout.write(u"\u001b[38;5;" + code + "m " + code.ljust(4))
#     print (u"\u001b[0m")

def testgradient(string, colorArr, bold=False):

    length = len(string)
    colorStops = len(colorArr);
    sectionLength = math.floor(length/(colorStops - 1))
    diffs = {}

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

    print('\033[1m') if bold else ''

    index = 0

    for i in range(1, colorStops):

        for j in range(0, sectionLength):

            print(f"\x1b[38;2;{r};{g};{b}m" + string[j + index], end = '')

            r += int((colorArr[i]["r"] - r)/sectionLength)
            g += int((colorArr[i]["g"] - g)/sectionLength)
            b += int((colorArr[i]["b"] - b)/sectionLength)

        index += sectionLength

    print (u"\u001b[0m")


testgradient("iridi - beautify your command line interfaces\n", ["#12c2e9", "#c471ed", "#f64f59"], bold=True)
testgradient("iridi - beautify your command line interfaces\n", ["#ff00cc", "#ff0000"], bold=True)
