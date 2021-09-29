import iridi

iridi.print("testing for whatever", iridi.presets.instagram)
res = iridi.input("type any word: ", iridi.presets.aquatic)
print(res)

gradient = iridi.preset(["#D3959B", "#BFE6BA"])
gradient.print("Testing with preset constructors.", bold=True)
gradient.input("Test an input: ")
