import pymongo
from pymongo import MongoClient
 
# Create a Mongodb client
client = MongoClient("localhost", 27017)


# Create a object to connect to a Database
# 1.) Creat a database variable
# 2.) Use the client variable
# 3.) In the brackets enter the name of the database you want to connect to
db = client['Client']


# Access the collection
collection = db["Client"]


# Functions -------------------------------------------------------------
def add_member():
    myperson = {'Name': get_name(),
                "Age": get_age()}
    collection.insert_one(myperson)

def delete_member():
    mydict = {'Name': get_name()}
    collection.delete_one(mydict)

def display():
    for document in collection.find():
        print('Name: ', document["Name"], 
              'Age:', document["Age"])

def sort():
    sort = int(input("How do you want to sort?\n1.)Ascending\n2.)Descending\n"))
    if (sort == 1):
        ascend()
    elif (sort == 2):
        descend()

def query():
    option = input(("What do you want to query? \nOptions:\nName\nAge\n"))
    if(option == "Name"):
        filter = {"Name": get_name()}
    elif(option =="Age"):
        filter = {"Age": get_age()}

    find = collection.find(filter)
    for f in find:
        print('Name: ', f["Name"], 
              'Age:', f["Age"])

def ascend():
    mycol = collection.find().sort("Name")
    for x in mycol:
        print(x["Name"])

def descend():
    mycol = collection.find().sort("Name", -1)
    for x in mycol:
        print(x["Name"])

def update():
    collection.update_one({"Name": get_name()}, {"$set":{"Age": get_age()}})

# Basic Functions-------------------------------------

def get_name():
    name = input("Enter name: ")
    return name

def get_age():
    age = int(input("Enter Age: "))
    return age


# Program ----------------------------------------------
def main():
    print('Hello welcome!')
    print("This a database to keep track of users and their age.")
    choice = 1
    while (choice != 0):
        choice = int(input("1.) Display\n2.) Insert\n3.) Remove\n4.) Sort\n5.) Query\n6.)Modify\n0.) Quit\n"))
        if (choice == 1):
            display()
        elif (choice ==2):
            add_member()
        elif (choice == 3):
            delete_member()
        elif (choice == 4):
            sort()
        elif (choice == 5):
            query()
        elif (choice == 6):
            update()
        elif (choice == 0):
            print("Thank you for coming!")
            print("Please Come again")


main()