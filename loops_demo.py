#using loops in python
#highlights different methods of usin loops to carry out the same task
#methods used here is to define own function and then call it
#to activate each code, call the main function by removing the # value
#the preliminary codes are building up to the last code, which is has been left active

#------------------------------------------------
#method 1: using for loop
def main():
        for _ in range(3):
            print("cat")
#main()

#-------------------------------------------------
#method 2: using *
#print("meow\n" * 3, end="")

#----------------------------------------------------
#method 3: using while loop
def main():
    i = 1
    while i <= 3:
        print("yes")
        i = i + 1
#main()
#----------------------------------------------------
#method 3: print number of times given by user
def main():
    x = input("What would you like to print out? ")
    x = x * 3
    print(x)
   
#main()

#------------------------------------------------------
#method 4: asking user what to print and also the number of times to do so
def main():
    times = int(input("How many times to print 'yes'? "))
    print("yes\n" * times, end=(""))

#main()

#------------------------------------------------------

#method 5: asking for input which should be a positive (+) integer
#useful when you want an input that matches a certain expectation
#in this case, we ask for a  (+) integer 

#induce an infinite loop: while loop
def main():
    while True:
        n = int(input("How many times do you want to print 'A'? "))
        #recall the prompt for input if the number given is a negative (-) integer
        if n > 0:
            #if negative, it will continue to stay within this loop
            #if the integer is positive, break from the loop
            break
    #to print the input n number of times
    for _ in range(n):
        print("A" )
        
#main()

#--------------------------------------------------------------------
#method 6: defining functions and calling them

def main():
    times = get_number()
    B(times)

def get_number():
    while True:
        n = int(input("How many times do you want to print 'B'? "))
        #recall the prompt for input if the number given is a negative (-) integer
        if n > 0:
            #if negative, it will continue to stay within this loop
            #if the integer is positive, return the value
            break
    #return the value if positive so that it can be used
    return n

def B(n):
    for _ in range(n):
        print("B")

main()



