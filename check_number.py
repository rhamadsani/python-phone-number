import json

def search_value (value, data) : 
    return_data = list()
    for i in data : 
        data_value = list(i.values())
        if value in data_value: 
            return_data.append(i)
    
    return return_data

#start program
getinput = input("Please Input Phone Number With International Code : ")

#read json list international code 
try: 
    ic = open("./international_code.json", 'r')
except FileNotFoundError : 
    print("File Not Found, Correction Path File Please")

except FileExistsError : 
    print("File does'nt Exist, Correction Path File Please")

content = ic.read()

jsonf = list(json.loads(content))

#check available internatioanl code
for2digit = search_value(getinput[0:3], jsonf)
for3digit = search_value(getinput[0:4], jsonf)
for4digit = search_value(getinput[0:5], jsonf)

# check result
result = []
if (len(for2digit) + len(for3digit) + len(for4digit)) == 0:
    print("International Code Not Found")
else : 
    result = for2digit + for3digit + for4digit

print(result)