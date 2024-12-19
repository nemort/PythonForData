import xml.etree.ElementTree as ET


tree = ET.parse('ex_3.xml')
root = tree.getroot()


print("Товары в счет-фактуре:")
for item in root.findall(".//СведТов"):
    name = item.get('НаимТов')
    quantity = item.get('КолТов')
    price = item.get('ЦенаТов')

    print(f"Товар: {name}, Количество: {quantity}, Цена: {price}")
