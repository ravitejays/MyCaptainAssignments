n=int(input("Enter How many Fibonacci terms to print: "))
a=0
b=1
i=0
if n<0:
    print("Error! Please enter positive Integers only")
elif n==0:
    print("Fibonacci number: ",a)
else:
    print("Fibonacci numbers are:")
    while n>i:
        print(a)
        add = a + b
        a=b
        b=add
        i = i + 1


