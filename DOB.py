#GEORGE WEST
#13-02-15
#DOB


import pickle
class record:
    def __init__(self):
        self.name =None
        self.dob = None
    
lists = []
records = record()
records.name = input("Please enter a name: ")
records.dob = int(input("Please enter your DOB: "))
lists.append(records)


with open("DOB.dat", mode= "wb") as my_file:
    pickle.dump(lists,my_file)


with open("DOB.dat", mode= "rb") as my_file:
    data = pickle.load(my_file)

for each in data:
    print(records.name)
    print(records.dob)
