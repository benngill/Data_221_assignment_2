
file = open(file="sample-file.txt", mode="r")
content = {}
matching = []
matchingLine = {}
rawLine = []
i = 1

for inputLine in file:
    rawLine.append(inputLine) # tracks the original lines for line numbers
    inputLine = inputLine.lower().strip() # standardizes format of lines
    for p in ".,!?;:- ":
        inputLine = inputLine.replace(p, "") #  removes all punctuation
    if inputLine not in "": # checks if line is empty or not
        content[i] = inputLine # adds non-empty lines to a content list
    i = i + 1

file.close()

for key in content:
    for key2 in content:
        if key != key2 and content[key] == content[key2]: # checks if two different keys have the same content
            if [key, key2] not in matching and [key2, key] not in matching: # checks if those two keys have already been recorded
                matchingLine[key] = rawLine[key-1] # adds first matching line # and line
                matchingLine[key2] = rawLine[key2-1] # adds second matching line # and line
                matching.append([key, key2])

for lineNumber, line in list(matchingLine.items())[:4]: # prints the first 4 lines (two pairs)
    print(f"{lineNumber} -> {line}")