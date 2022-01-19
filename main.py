import json 


with open('users.test.json', "rb") as file: 
    db = json.load(file)
    for i in range(len(db)): 
        if db[i]["flags"] == None: 
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
            del[db[i]["discriminator"]]
            
            
            
open("updated.text.json", "w").write(
    json.dumps(db, sort_keys=True, indent=4, separators=(',', ': '))
)
    
    






