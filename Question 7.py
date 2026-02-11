import requests
from bs4 import BeautifulSoup

headers = {'User-Agent': "benng/1.0"}

data_science_wiki_html = requests.get("https://en.wikipedia.org/wiki/Data_science", headers=headers).text
parsed_html_document = BeautifulSoup(data_science_wiki_html, "html.parser")
data_science_content = parsed_html_document.find("div", id="mw-content-text")

title = parsed_html_document.title
data_science_content = data_science_content.find_all("p")

wikiTitle = title.text
print(wikiTitle)

firstParagraph = ""
for paragraph in data_science_content:
    if len(paragraph.text.strip()) >= 50:
        firstParagraph = paragraph.text.strip()
        break

print(firstParagraph)
