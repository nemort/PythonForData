import docx

doc = docx.Document("task3.docx")

table = doc.tables[0]
column = 0
ATmega328_data_dict = {}
for i, cell in enumerate(table.rows[0].cells):
    if cell.text.strip() == "ATmega328":
        column = i
        break

for row in table.rows[1:]:
    key = row.cells[0].text.strip()
    value = row.cells[column].text.strip()
    ATmega328_data_dict[key] = value
print(ATmega328_data_dict)
