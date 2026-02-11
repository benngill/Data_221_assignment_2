import requests
from bs4 import BeautifulSoup

headers = {'User-Agent': "benng/1.0"}

machine_learning_wiki = requests.get("https://en.wikipedia.org/wiki/Machine_learning", headers=headers)
parsed_html = BeautifulSoup(machine_learning_wiki.text, "html.parser")
machine_learning_content = parsed_html.find("div", id="mw-content-text")
machine_learning_tables = machine_learning_content.find_all("table")

for line in machine_learning_tables:
    # print(line.text)
    table_row = line.find_all("tr")
    table_headers = []
    if len(table_row) >= 3:
        table_headers = table_row[0].find_all("th")
        if len(table_headers) == 0:
            first_row_cells = table_row[0].find_all(["th","td"])
            number_of_rows = len(first_row_cells)
            for i in range(number_of_rows):
                table_headers.append(f"col{i+1}")

print(table_headers)

