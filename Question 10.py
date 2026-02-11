def find_lines_containing(filename, keyword):
    keyword = str(keyword.lower().strip())
    file=open(str(filename))
    line_number = 1
    lines_with_keyword = []
    for line in file:
        line_text = line.lower()
        if keyword in line_text:
            lines_with_keyword.append([line_number,line_text.strip()])
        line_number += 1
    file.close()

    return lines_with_keyword

keywordData = find_lines_containing("sample-file.txt", "Machine learning")

print(len(keywordData))
print(keywordData[:3])