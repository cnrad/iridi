# ![image](https://user-images.githubusercontent.com/83192247/135200147-afd3f684-a650-4dca-9eed-b9fc82dcb517.png)

### Install:

```
pip install iridi
```

### Usage:

```py
from iridi import *

# Create gradient text
# iridi(message, colors, options)

iridi("This is an example message. Colorful, huh?", ["#8A2387", "#E94057", "#F27121"], bold=True)
```

The above should result in this:

![image](https://user-images.githubusercontent.com/83192247/135200457-e81fb417-1dde-4ab0-92ad-c26fba9dd003.png)

# Options:

The array can be an array of hex strings, or objects with r, g, and b values. This...
```
# This works:
iridi("Try it with RGB objects!", ["#7350b3", "#2ebf91"])

# So does this:
iridi("Try it with hex values!", [{"r": 250, "g": 0, "b": 100}, {"r": 60, "g": 255, "b": 0}])
```
...results in the following:

![image](https://user-images.githubusercontent.com/83192247/135200666-e92da91a-a4a0-4b02-832d-0f9a0e0c2c53.png)

Want the output in bold? No problem, just add `bold=True` as the third argument to the function (shown in examples above).

## Presets

There are included presets when importing the module, access them by doing ```presets.[name]```. Example:

```py
from iridi import *

iridi("Nice preset!", presets.wiretap)
```

![image](https://user-images.githubusercontent.com/83192247/135200859-12f802fb-22d6-4e2a-9fb6-4bd0769fce18.png)

*If you'd like to contribute or add preset gradients to this project, feel free to fork this and make a PR!*

If you end up using this or think it's cool, why not drop a :star:? It means a lot :)


