import requests
from bs4 import BeautifulSoup

headers = {'User-Agent': "benng/1.0"} # wiki permission source

data_science_wiki_html = requests.get("https://en.wikipedia.org/wiki/Data_science", headers=headers).text # pull data science wiki page
parsed_html_document = BeautifulSoup(data_science_wiki_html, "html.parser") # parse page
data_science_content = parsed_html_document.find("div", id="mw-content-text") # add all main content text to variable

data_science_header = data_science_content.find_all("h2") # find all <h2> headers in main content

file = open(file="headings.txt", mode="w") # opens and creates new .txt file in write mode
headers_to_remove_text = {"References", "See also", "External links", "Notes"} # undesired headers

for i in data_science_header:
    if i.text not in headers_to_remove_text: # check if header is in to_remove
        file.writelines(i.text + "\n") # if desired, write to file

file.close()

