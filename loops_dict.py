#creating a python dictionary
#dictionaries use {}
#associate grades to names
def main():
    grades = {
        "Bob": "A", 
        "Lorry": "A", 
        "Joan": "C", 
        "Jerry": "D", 
        "Janine": "F", 
        "Robinson": "B"
        }
#to print out the a particular student
    print(grades["Bob"])
    print(grades["Janine"])
#main()
#___________________________________________________

def main():
    grades = {
        "Bob": "A", 
        "Lorry": "A", 
        "Joan": "C", 
        "Jerry": "D", 
        "Janine": "F", 
        "Robinson": "B"
        }
#using a for loop to iterate over the keys
#in this case, student are the keys
    for student in grades:
        print(student)
#to print out both the key (name) to index into the dictionary
    for student in grades:
        print(student, grades[student], sep=": ")
#main()

#______________________________________________________

#dealing with more data
#having a list of dictionaries/associating more things with the student
def main():
    #create a list of dictionaries
    #having a collection of key value pairs
    grades = [
        #creating list of dictionaries
        {"name": "Bob", "value": "A", "point": "4"},
        {"name": "Lorry", "value": "A", "point": "4"},
        {"name": "Joan", "value": "C", "point": "2"},
        {"name": "Jerry", "value": "D", "point": "1"},
        {"name": "Janine", "value": "F", "point": None},
        {"name": "Robinson", "value": "B", "point": "3"},
        ]
    

#using a for loop to iterate over every student in the list then print out the desired values

    for student in grades:
        print(student["name"], student["value"], student["point"], sep=": ")
    
main()
