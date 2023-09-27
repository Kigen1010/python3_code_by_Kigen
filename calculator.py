def main():
    #get user input
    expression = input("Expression: ")
    #convert user input to variables x, y, z with a space inbetween
    x, y, z = expression.split(" ")
    #xonvert the inputs x and z to float
    fl_x = float(x)
    fl_z = float(z)

    # doing the claculations
    if y == "+":
        solution = fl_x + fl_z
        #format the solution to one decimal number
        print(f"{solution:.1f}")
    elif y == "-":
        solution = fl_x - fl_z
        print(f"{solution:.1f}")
    elif y == "*":
        solution = fl_x * fl_z
        print(f"{solution:.1f}")
    elif y == "/":
        z != 0
        solution = fl_x / fl_z
        print(f"{solution:.1f}")



main()
