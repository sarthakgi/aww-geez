a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
oper = input("Enter -\n\n\"+\" for addition,\n\"-\" for subtraction,\n\"*\" for multiplication,\n\"/\" for division: " )

def solve(a,b,oper):
    if oper == '+':
        return (a+b)
    elif oper == '-':
        return (a-b)
    elif oper == '*':
        return (a*b)
    elif oper == '/':
        return (a/b)
    else :
        return ("Invalid Input")

print(a,oper,b,"=",solve(a,b,oper))