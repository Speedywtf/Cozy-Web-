import json 


with open('users.test.json', "rb") as file: 
    db = json.load(file)
    for i in range(len(db)): 
        if type(db[i]["username"]) == str: 
            del[db[i]["username"]]
            
            
            
open("updated.text.json", "w").write(
    json.dumps(db, sort_keys=True, indent=4, separators=(',', ': '))
)
    
    






