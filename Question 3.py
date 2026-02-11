
file = open(file="sample-file.txt", mode="r")
content = {}
matching = []
matchingLine = {}
rawLine = []
i = 1

for inputLine in file:
    rawLine.append(inputLine)
    inputLine = inputLine.lower().strip()
    for p in ".,!?;:- ":  # removes punctuation from around tokens
        inputLine = inputLine.replace(p, "")
    if inputLine not in "":
        content[i] = inputLine
    i = i + 1

file.close()

for key in content:
    for key2 in content:
        if key != key2 and content[key] == content[key2]:
            if [key, key2] not in matching and [key2, key] not in matching:
                matchingLine[key] = rawLine[key-1]
                matchingLine[key2] = rawLine[key2-1]
                matching.append([key, key2])

for lineNumber, line in list(matchingLine.items())[:4]:
    print(f"{lineNumber} -> {line}")