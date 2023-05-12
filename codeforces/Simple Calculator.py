cont = True
while cont:
    x = input("Please enter your calculations as follows: [number][operator][number]= \n")
    # determining the operator
    op = ""
    for c in x:
        if c in "*/-+^":
            op = c
    if op != "":
        # transforming the string into a list
        X = x.split(op)
        # removing the "=" sign from the lists last element((if the user enters it )) so it can be transformed into string
        y = X[len(X) - 1].split("=")
        X[len(X) - 1] = y[0]
        # does the operation
        if op == "*":
            total = int(X[0]) * int(X[1])
        elif op == "/":
            total = int(X[0]) / int(X[1])
        elif op == "-":
            total = int(X[0]) - int(X[1])
        elif op == "+":
            total = int(X[0]) + int(X[1])
        elif op == "^":
            total = int(X[0]) ** int(X[1])
        print(X[0], op, X[1], "=", total)
    else:
        print("Please enter an operator.")
    # checking if the user is done
    z = input("Do you want to continue?(y/n)\n")
    z = z.lower()
    if z == "n":
        print("thank you exiting")
        cont = False
