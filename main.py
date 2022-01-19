import json 


with open('users.test.json', "rb") as file: 
    db = json.load(file)
    items = {}
    for i in range(len(db)):
        items[db[i]["id"]] = db[i]
    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        """if db[i]["flags"] == None: 
            del[db[i]["flags"]]
        if db[i]["system"] == None: 
            del[db[i]["system"]]
        if type(db[i]["createdTimestamp"]) == int: 
            del[db[i]["createdTimestamp"]]
        if db[i]["avatar"] == None: 
            del[db[i]["avatar"]]
        if db[i]["lastMessageChannelID"] == None: 
            del[db[i]["lastMessageChannelID"]]
        if type(db[i]["discriminator"]) == str: 
            del[db[i]["discriminator"]]"""
            
       
            
open("updated.text.json", "w").write(
    json.dumps(items, sort_keys=True, indent=4, separators=(',', ': '))
)
    
    






