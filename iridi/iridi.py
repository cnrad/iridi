import math
from typing import Union, Dict, List
from .presets import presets as iridipresets

class iridi:

    presets = iridipresets

    def print(string: str, colorArr: Union[Dict[str, int], List[str]], bold: bool = False):

        length = len(string)
        colorStopsCount = len(colorArr)
        sectionLength = math.floor(length/(colorStopsCount - 1))

        if isinstance(colorArr[0], str) and colorArr[0].startswith("#"):
            for i in range(0, colorStopsCount):
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

        if bold:
            print('\033[1m', end="")

        index = 0

        for i in range(1, colorStopsCount):
            for j in range(0, sectionLength):
                print(f"\x1b[38;2;{r};{g};{b}m" + string[j + index], end='')

                r += int((colorArr[i]["r"] - colorArr[i - 1]["r"])/sectionLength)
                g += int((colorArr[i]["g"] - colorArr[i - 1]["g"])/sectionLength)
                b += int((colorArr[i]["b"] - colorArr[i - 1]["b"])/sectionLength)

            index += sectionLength

            if (i + 1 == colorStopsCount) and index < length:
                print(f"\x1b[38;2;{r};{g};{b}m" + string[index], end='')

        print(u"\u001b[0m")



    def input(string: str, colorArr: Union[Dict[str, int], List[str]], bold: bool = False):

        length = len(string)
        colorStopsCount = len(colorArr)
        sectionLength = math.floor(length/(colorStopsCount - 1))
        finalStr = ''

        if isinstance(colorArr[0], str) and colorArr[0].startswith("#"):
            for i in range(0, colorStopsCount):
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

        if bold:
            finalStr += ('\033[1m')

        index = 0

        for i in range(1, colorStopsCount):
            for j in range(0, sectionLength):
                finalStr += (f"\x1b[38;2;{r};{g};{b}m" + string[j + index])

                r += int((colorArr[i]["r"] - colorArr[i - 1]["r"])/sectionLength)
                g += int((colorArr[i]["g"] - colorArr[i - 1]["g"])/sectionLength)
                b += int((colorArr[i]["b"] - colorArr[i - 1]["b"])/sectionLength)

            index += sectionLength

            if (i + 1 == colorStopsCount) and index < length:
                finalStr += (f"\x1b[38;2;{r};{g};{b}m" + string[index])

        return input(finalStr + u"\u001b[0m")
