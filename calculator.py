#Add the numbers

def add(x,y):
    return x+y

#Substract the numbers

def subtract(x,y):
    return x-y

#Multiply the numbers

def multiply(x,y):
    return x*y

#Divide the numbers

def divide(x,y):
    return x/y

#Remainder of numbers after division

def remainder(x,y):
    return x%y

#Raise to the power of

def power(x,y):
    return x**y

print("From below, choose the operation you want to be performed: ")
print("1 : For Addition")
print("2: For Subtraction")
print("3: For Multiplication")
print("4: For Division")
print("5: For finding remainder after division")
print("6: For finding power raised to another number")

while True:
    choose=input("Choose your number from above points: ")
    if choose in ("1","2","3","4","5","6"):
        n1=int(input("Type first number: "))
        n2=int(input("Type Second number: "))
        if choose=="1":
            print(n1, "+",n2,"=",add(n1,n2))
        elif choose=="2":
            print(n1, "-",n2,"=",subtract(n1,n2))
        elif choose=="3":
            print(n1, "*",n2,"=",multiply(n1,n2))
        elif choose=="4":
            print(n1, "/",n2,"=",divide(n1,n2))
        elif choose=="5":
            print(n1, "%",n2,"=",remainder(n1,n2))
        elif choose=="6":
            print(n1, "to the power",n2,"=",power(n1,n2))
        next=input("Do you want to do more calculations (Yes/No) : ")
        if(next=="No" or next=="no" or next=="NO"):
            break
    else:
        print('''Please, give the write input..
              This is wrong Input''')