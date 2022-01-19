import json 


with open('users.test.json', "rb") as file: 
    db = json.load(file)
    items = {}
    for i in range(len(db)):
        items[db[i]["id"]] = db[i]
    
        
    
            
       
            
open("updated.text.json", "w").write(
    json.dumps(items, sort_keys=True, indent=4, separators=(',', ': '))
)
    
    






