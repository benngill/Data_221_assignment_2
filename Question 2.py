import token
from bs4 import BeautifulSoup

file = open(file="sample-file.txt", mode="r")

content = file.read().lower() # reads file content and converts all char to lowercase
tokenList = [] # empty list to store tokens
tokenCountDict = {} # empty dict to store word-count pairs

for p in ".,!?;:": # removes punctuation from around tokens
    content = content.replace(p, " ")

tokenList = content.split() # adds each word as a token in the list
file.close() # file is no longer accessed directly

for i in range(1,len(tokenList)):
    if len(tokenList[i]) >= 2: # checks that word is >= 2 characters
        word1 = tokenList[i-1] # sets first word of pair
        word2 = tokenList[i] # sets second word of pair
        if f"{word1} {word2}" in tokenCountDict.keys(): # checks if word pair is in dict
            tokenCountDict[f"{word1} {word2}"] += 1 # adds 1 to counter for word pair
        if f"{word1} {word2}" not in tokenCountDict: # checks if word pair is NOT in dict
            tokenCountDict[f"{word1} {word2}"] = 1 # creates dict key of word pair, sets count to 1

orderedTokenCount = sorted(tokenCountDict.items(), key=lambda count: count[1], reverse=True) # sorts the dict in descending order

for word, count in orderedTokenCount[:5]: # iterates through the first 5 key-value pairs in the sorted dict
    print(f"{word} -> {count}")