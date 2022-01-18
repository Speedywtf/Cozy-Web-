import json 


with open('users.test.json', "rb") as file: 
    db = json.load(file)
    items = []
    for item in db:
        items.append(item['username'])
    print(items)






