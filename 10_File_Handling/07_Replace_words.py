with open ("Replace.txt") as f:
    content =f.read()

content=content.replace("replace","Sample")

with open("Replace.txt", "w") as f:
    f.write(content )