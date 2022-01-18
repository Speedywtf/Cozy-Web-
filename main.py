import json 


with open('users.test.json', "rb") as file: 
    db = json.load(file)
    for elements in db: 
        if 'system' in elements and 'Locale' in elements and 'flags' in elements and 'discriminator' in elements and 'avatar' in elements and 'LastMessageChannelId' in elements: 
            del elements['system']
    
    






