list = []
n = int(input("Enter the number of elements in the range: "))
print("Enter the elements: ")
for element in range(0,n):
    element=int(input())
    list.append(element)
print("The numbers you have entered is: ", list)

positivelist = [i for i in list if i>= 0]
print("The Positive numbers in the range are: ", positivelist)
