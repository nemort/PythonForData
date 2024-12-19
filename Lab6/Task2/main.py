import xml.etree.ElementTree as ET


tree = ET.parse('ex_2.xml')
root = tree.getroot()


new_item = ET.Element('Item')
ET.SubElement(new_item, 'ArtName').text = 'Сыр Алиса'
ET.SubElement(new_item, 'Barcode').text = '2000000000092'
ET.SubElement(new_item, 'QNT').text = '315,15'
ET.SubElement(new_item, 'QNTPack').text = '315,15'
ET.SubElement(new_item, 'Unit').text = 'шт'
ET.SubElement(new_item, 'SN1').text = '00000011'
ET.SubElement(new_item, 'SN2').text = '08.11.2024'
ET.SubElement(new_item, 'QNTRows').text = '10'


detail = root.find('Detail')
detail.append(new_item)
ET.indent(tree, '    ')


total_qnt = 0
total_rows = 0


for item in root.findall('.//Item'):
    qnt = float(item.find('QNT').text.replace(',', '.'))
    qnt_rows = int(item.find('QNTRows').text)
    total_qnt += qnt
    total_rows += qnt_rows


summary = root.find('Summary')
summary.find('Summ').text = f"{total_qnt:.2f}".replace('.', ',')
summary.find('SummRows').text = str(total_rows)


tree.write('ex_2_modified.xml', encoding='UTF-8', xml_declaration=True)
print("файл сохранён как 'ex_2_modified.xml'.")
