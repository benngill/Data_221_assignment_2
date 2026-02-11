import requests
from bs4 import BeautifulSoup

headers = {'User-Agent': "benng/1.0"} # wiki permission source

machine_learning_wiki = requests.get("https://en.wikipedia.org/wiki/Machine_learning", headers=headers) # pull machine learning wiki page
parsed_html = BeautifulSoup(machine_learning_wiki.text, "html.parser") # parse page
machine_learning_content = parsed_html.find("div", id="mw-content-text") # add main content text to variable
machine_learning_tables = machine_learning_content.find_all("table") # find all instances of <table> tag in main content

'''
for line in machine_learning_tables:
    table_row = line.find_all("tr")
    table_headers = []

    if len(table_row) >= 3:
        table_headers = table_row[0].find_all("th")

        if len(table_headers) == 0:
            first_row_cells = table_row[0].find_all(["th", "td"])
            number_of_rows = len(first_row_cells)
            for i in range(number_of_rows):
                table_headers.append(f"col{i + 1}")

        print(table_headers)  # <-- moved inside
'''

target_table = None

# find first table with >= 3 data rows (<tr> excluding header row)
for table in machine_learning_tables:
    rows = table.find_all("tr")
    # count number of data rows (excluding header row if any)
    data_row_count = sum(1 for r in rows if r.find_all("td"))
    if data_row_count >= 3:
        target_table = table
        break

# if no table found, exit
if target_table is None:
    print("No table with at least 3 data rows found.")
    exit()

rows = target_table.find_all("tr")

# extract headers
first_row = rows[0]
header_cells = first_row.find_all("th")

if header_cells:
    headers = [cell.get_text(strip=True) for cell in header_cells]
else:
    # no header row, invent col names based on number of cells in first row
    first_cells = first_row.find_all(["th", "td"])
    headers = [f"col{i+1}" for i in range(len(first_cells))]

# build data rows (including header if needed)
table_data = []

# include header row
table_data.append(headers)

max_cols = len(headers)

# process all rows
for row in rows:
    cells = row.find_all(["th", "td"])
    if not cells:
        continue
    row_text = [c.get_text(strip=True) for c in cells]
    # pad missing values with ""
    if len(row_text) < max_cols:
        row_text += [""] * (max_cols - len(row_text))
    table_data.append(row_text)

# write to CSV
file = open(file="wiki_table.csv", mode="w") # opens and creates new .csv file in write mode
for row in table_data:
# ensure everything is a string
    row = [str(cell) for cell in row]
    line = ",".join(row) # join with commas
    file.write(line + "\n")

file.close()