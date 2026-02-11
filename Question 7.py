import requests
from bs4 import BeautifulSoup

headers = {'User-Agent': "benng/1.0"} # wiki permission source

data_science_wiki_html = requests.get("https://en.wikipedia.org/wiki/Data_science", headers=headers).text # pulls data science wiki page
parsed_html_document = BeautifulSoup(data_science_wiki_html, "html.parser") # parse page
data_science_content = parsed_html_document.find("div", id="mw-content-text") # add all main content text to variable

title = parsed_html_document.title # finds first example of <title> in main content of wiki page
data_science_content = data_science_content.find_all("p") # finds all <p> paragraph lines in wiki page

wikiTitle = title.text
print(wikiTitle)

firstParagraph = ""
for paragraph in data_science_content: # iterates through each line of <p>
    if len(paragraph.text.strip()) >= 50: # checks if current paragraph is >= 50 characters
        firstParagraph = paragraph.text.strip() # declares first passing instance as firstParagraph
        break

print(firstParagraph)
