#Illustration 1: print specific value in a list
def main():
    grades = ["A", "B", "C", "D", "F"]
    #use [] to index into the list
    print(grades[0])

#main()

#Illustration 2: print more than one value in a list
#use for loop to iterate over everything

def main():
    grades = ["A", "B", "C", "D", "F"]
    for grade in grades:
        print(grade)
#main()

#Illustration 3: using 'len' 
def main():
    grades = ["A", "B", "C", "D", "F"]
    #first get the length of the grades list and print it
    for i in range(len(grades)):
        print(grades[i])

#main()

#illustration 4: to show the ranks of the list
def main():
    grades = ["A", "B", "C", "D", "F"]
    #get the ranking beginning at 1
    for i in range(len(grades)):
        print(i + 1, grades[i])

main()



