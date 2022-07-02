import os

#-------Employee Class----------------
class Employee:
    def __init__(self, id, firstName, lastName, hireYear):
        self.id = id
        self.firstName = firstName
        self.lastName = lastName
        self.hireYear = hireYear
    
    def __str__(employee):
        return ("\nEmployee ID: " + employee.id +
            "\nFirst Name: " + employee.firstName +
            "\nLast Name: " + employee.lastName + 
            "\nHire Year: " + employee.hireYear
            )

#--------------------------------------------------------
SIMPLE_PATH = r'C:\Users\atemple\source\repos\DBT230\Group1_SimplePersistence\data\Assignment 1 - data\people\simple/'

#SIMPLE_PATH = r'C:\Users\zhenx\Desktop\Assignment 1 - data (3)\people\simple/'

def print_people_details(path):
    files = os.listdir(path)
    for file in files:
        if os.path.isfile(os.path.join(path, file)):
            f = open(os.path.join(path, file), 'r')
            for x in f: 
                print(x)
            f.close()

def print_employee(path):
    files = os.listdir(path)
    for file in files:
        if os.path.isfile(os.path.join(path, file)):
            f = open(os.path.join(path, file), 'r')
            for x in f: 
                string = x
                information = string.split()
                id = information[0]
                fName = information[1]
                lName = information[2]
                hireYear = information[3]
                employee = Employee(id,fName,lName,hireYear)
                print(employee)
            f.close()

#----------------------Add Employee----------------------------------------

SIMPLE_PATH2 = r'C:\Users\zhenx\Desktop\Assignment 1 - data (3)\people\long/'

def add_employee(ID,firstName,lastName,hireYear):
    location_file = SIMPLE_PATH2
    file_name = "10001.txt"
    newFileLocation = os.path.join(location_file, file_name)
    print(newFileLocation)

    newFile = open(newFileLocation, "w")

    newFile.write(ID + "," + firstName + "," + lastName +"," + hireYear)
    newFile.close()
    


#----------------------Delete Employee----------------------------------------

#----------------------Update Employee----------------------------------------

def update_employee(id, first_name, last_name, hire_date):
    file_name = str(id) + ".txt"
    file_path = SIMPLE_PATH + file_name
    if os.path.isfile(file_path):
        file_reference = open(file_path, "w")
        string_to_write = ", ".join([str(id), first_name, last_name, str(hire_date),])
        file_reference.write(string_to_write)
        file_reference.close()

#-------------------------------------------------------------    

#print_people_details(SIMPLE_PATH)
#print_employee(SIMPLE_PATH)

ID = input("Enter your ID: ")
firstName = input("Enter first name: ")
lastName = input("Enter last name: ")
hireYear = input("Enter hire year: ")
add_employee(ID,firstName,lastName,hireYear)

ID2 = input("Enter your ID: ")
firstName2 = input("Enter first name: ")
lastName2 = input("Enter last name: ")
hireYear2 = input("Enter hire year: ")
update_employee(ID2,firstName2,lastName2,hireYear2)
