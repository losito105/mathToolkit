def convert():
    x=input("Type your values in here: ")
    base,power,exponent,which_one=x.split(",")
    if which_one=='0':#log->exp
        print(base + " ^ " + exponent + " = "+ power)
    elif which_one=='1':#exp->log
        print("log base " + base + " of " + power + " = " + exponent)
    else:
        print("ERROR")

def print_instruc():
    print("Instructions: ")
    print("\nType in your values in the following order: ")
    print("\n\tfor log->exp: the base of the log,the thing you're taking the log of,the thing on the other side of the =")
    print("\n\tfor exp->log: the thing you're raising to a power,the thing on the other side of the =,the exponent")
    print("\nDo not use any spaces in your input\n")
    convert()

print_instruc()
