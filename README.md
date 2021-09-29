![image](https://user-images.githubusercontent.com/83192247/135200147-afd3f684-a650-4dca-9eed-b9fc82dcb517.png)

# Basics

### Install:

```
pip install iridi
```

### Usage:

```py
import iridi

# Create gradient text
# iridi.print(message, colors, options)

# Ask for input with gradient text:
# iridi.input(message, colors, options)

iridi.print("This is an example message. Colorful, huh?", ["#8A2387", "#E94057", "#F27121"], bold=True)
response = iridi.input("What's your favorite color?", ["#8A2387", "#E94057", "#F27121"])
print(response)
```

The above should result in this:

![image](https://user-images.githubusercontent.com/83192247/135343462-f157627d-6e66-4781-a943-67122233c237.png)


# Presets

There are included presets when importing the module, access them by doing ```iridi.presets.[name]```. Example:

```py
import iridi

iridi.print("Nice preset!", iridi.presets.wiretap)
```

![image](https://user-images.githubusercontent.com/83192247/135200859-12f802fb-22d6-4e2a-9fb6-4bd0769fce18.png)

*If you'd like to contribute or add official preset gradients to this project, feel free to fork this and make a PR!*

## Make your own presets:

Iridi comes with the ability to create your own gradients and reuse them.

```py
gradient = iridi.preset(["#D3959B", "#BFE6BA"])

gradient.print("Testing with preset constructors.", bold=True)
response = gradient.input("Test an input: ")
print(response)
```

Output:

![image](https://user-images.githubusercontent.com/83192247/135343903-53bd1f89-6606-4c1b-a601-ad68c4ad4dd1.png)


# Options:

The array can be an array of hex strings, or objects with r, g, and b values. This...
```py
# This works:
iridi.print("Try it with RGB objects next!", ["#7350b3", "#2ebf91"])

# So does this:
iridi.print("Try it with hex values if you haven't!", [{"r": 250, "g": 0, "b": 100}, {"r": 60, "g": 255, "b": 0}])
```
...results in the following:

![image](https://user-images.githubusercontent.com/83192247/135344299-f84f5417-58f6-45a0-b0db-be47e6eea67a.png)

Want the output in bold? No problem, just add `bold=True` as the third argument to the function (shown in examples above).

--------

If you end up using this, or just think it's cool, feel free to :star: this repo, it means a lot :)
