import xmlschema


schema = xmlschema.XMLSchema("Task1/schema.xsd")


def validate_xml(xml_file):
    try:
        schema.validate(xml_file)
        print(f"{xml_file} прошел валидацию.")
    except xmlschema.XMLSchemaValidationError as e:
        print(f"{xml_file} не прошел валидацию.")
        # print("Ошибка:", e)


validate_xml("Task1/ex_1.xml")
validate_xml("Task1/ex_1_invalid.xml")
