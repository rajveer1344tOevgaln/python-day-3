# stores only immutable data
# ignores dublicate data
# it is important to place a , after a singlr data to insure set otherwise it becomes as a dictinory

a = set() # to create an empty set 
data = {1,2,3,4,5,6,7,8,9,10,1,6,8,4}
print(data)
print(type(data))
print(len(data))