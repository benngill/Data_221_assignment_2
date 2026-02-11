import requests
from bs4 import BeautifulSoup

headers = {'User-Agent': "benng/1.0"}

data_science_wiki_html = requests.get("https://en.wikipedia.org/wiki/Data_science", headers=headers).text
parsed_html_document = BeautifulSoup(data_science_wiki_html, "html.parser")
data_science_content = parsed_html_document.find("div", id="mw-content-text")

data_science_header = data_science_content.find_all("h2")

file = open(file="headings.txt", mode="w")
headers_to_remove_text = {"References", "See also", "External links", "Notes"} # undesired headers

for i in data_science_header:
    if i.text not in headers_to_remove_text:
        file.writelines(i.text + "\n")

file.close()

