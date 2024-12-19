from jsonschema import validate
import json


def validate_json(invalid_json_file, schema_file):
    with open(invalid_json_file) as json_file, open(schema_file) as schema:
        try:
            validate(json.load(json_file), json.load(schema))
            print(f"Файл {json_file} прошел валидацию.")
        except:
            print(f"Файл {json_file} не прошел валидацию.")


if __name__ == '__main__':
    schema_file = "ex_1_shema.json"
    invalid_json_file = "ex_1_invalid.json"
    validate_json(invalid_json_file, schema_file)
