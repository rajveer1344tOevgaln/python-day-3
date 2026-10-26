audit = {
    "brand name" :"nike",
    "owner1" : "shivam",
    "avg price" : 5000,
    "is cheked" : True,
    "type" : { 
        "shoe" : "all type",
        "tshirt" : "plain ",
        "bat" : "profassinol",

    }

    }
print(audit)
print("keys :",audit.keys())# prints the keys
print("value :",audit.values()) # prints all values
print("seperate data :",audit.items())# print each value in seperate order
print("specific value :",audit.get("type"))# print specific given value (does not show error if key not found)
audit.update({"Adress" : "Panipath"})#add new data 
print(audit)