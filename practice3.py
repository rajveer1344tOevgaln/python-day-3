# create a dictionary to get subjects and marks from user 


data = {}

a = int(input("Enter phy :"))
data.update({"phy" : a})

a = int(input("Enter chem :"))
data.update({"chem" : a})

a = int(input("Enter maths :"))
data.update({"maths" : a})

a = int(input("Enter eng :"))
data.update({"eng" : a})




print(data)