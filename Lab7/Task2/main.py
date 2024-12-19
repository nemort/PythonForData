import json


def get_data():
    with open("ex_2_formatted.json") as f:
        data = json.load(f)
        phone_book = {}

        for user in data["users"]:
            phone_book[user["name"]] = user["phoneNumber"]
            
        print(phone_book)


if __name__ == "__main__":
    get_data()
