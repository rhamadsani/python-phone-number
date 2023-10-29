import json

def search_value (value, data) : 
    return_data = list()
    for i in data : 
        data_value = list(i.values())
        if value in data_value: 
            return_data.append(i)
    
    return return_data

#read json list international code 
try: 
    ic = open("./international_code.json", 'r')
except FileNotFoundError : 
    print("File Not Found, Correction Path File Pleae")

except FileExistsError : 
    print("File does'nt Exist, Correction Path File Pleae")

content = ic.read()

jsonf = list(json.loads(content))

print(search_value("+62", jsonf))
