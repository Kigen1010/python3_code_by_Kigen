#using "try" and "except"to identify code vulnerability in terms of unwanted input
#to print an error that the user will easily understand
#this is a form of defensive coding: patching an error that might happen
#_____________________________________________________________________________________
#use try

#try:
    #x = int(input("What's x? "))
    #print(f"x is {x}")
#using 'except' will print the defined message when a value error occurs
#except ValueError:
    #print("x is not an integer")
#__________________________________________________________________________________________
#Method2: using "else" after the exception
#try:
    #x = int(input("What's x? "))
#except ValueError:
    #print("x is not an integer")
#else:
    #print(f"x is {x}")

#main2()

#using a loop
#____________________________________________________________________________________________
#Method 3: induce an infinite loop with a boolean 
#the loop continues if the condition is not met

#while True:
    #try:
        #x = int(input("What's x? "))
    #except ValueError:
        #print("x is not an integer")
    #break out of the loop if the condition is met and proceed to the next line of code instruction
    #else:
        #break
#print(f"x is {x}")
#main3()
#_____________________________________________________________________________________________
#Method 4: using the break without the else
#while True:
    #try:
        #x = int(input("What's x? "))
        #initiate a break when the condition is met
        #break
    #except ValueError:
        #print("x is not an integer")
    #break out of the loop if the condition is met and proceed to the next line of code instruction
       
#print(f"x is {x}")

#___________________________________________________________________________________________________
#method 5: defining own function
#defining function to print outcome when condition is met
def main():
    #associating "x" with the defined function that asks for user input
    x = get_int()
    print(f"x is {x}")

#defining function to get user input
def get_int():
    while True:
        try:
            x = int(input("What's x? "))
        except ValueError:
            print("x is not an integer")
        else:
            #initiate break when the condition is met
            break
    #return the value to be used in the main function
    return x 
#main()
#___________________________________________________________________________________________________
#Method 6: refining the code by shortening
#removing the "else" statement and returning the "x" directly
def main():
    #associating "x" with the defined function that asks for user input
    x = get_int()
    print(f"x is {x}")

#defining function to get user input
def get_int():
    while True:
        try:
            x = int(input("What's x? "))
            return x
        except ValueError:
            print("x is not an integer")
        
#main()
#_______________________________________________________________________________________________________
#Method 7: refining further
#return "x" directly instead of defining it first
def main():
    #associating "x" with the defined function that asks for user input
    x = get_int()
    print(f"x is {x}")

#defining function to get user input
def get_int():
    while True:
        try:
            #return the user input to be applied in the main function
            return int(input("What's x? "))
        except ValueError:
            print("x is not an integer")
        
#main()
#________________________________________________________________________________________________________

#Method 8: using "pass" to ignore giving the user the error message
def main():
    #associating "x" with the defined function that asks for user input
    x = get_int()
    print(f"x is {x}")

#defining function to get user input
def get_int():
    while True:
        try:
            #return the user input to be applied in the main function
            return int(input("What's x? "))
        #catch the error but don't give any message
        except ValueError:
            pass
        
#main()
#_______________________________________________________________________________________________________
#Method 9: prompting directly in the main function
def main():
    #associating "x" with the defined function that asks for user input
    x = get_int(("What's x? "))
    print(f"x is {x}")

#defining function to get user input
def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            pass
        
main()