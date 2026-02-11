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

for word in tokenList: # filters out unwanted words
    if word in tokenCountDict: # adds count if already in dict
        tokenCountDict[word] += 1
    elif len(word) >= 2 and word not in tokenCountDict: # checks if word in tokenList
        tokenCountDict[word] = 1 # adds filtered results to a new dict

orderedTokenCount = sorted(tokenCountDict.items(), key=lambda count: count[1], reverse=True) # sorts the dict in descending order

for word, count in orderedTokenCount[:10]: # iterates through the first 10 key-value pairs in the sorted dict
    print(f"{word} -> {count}")

