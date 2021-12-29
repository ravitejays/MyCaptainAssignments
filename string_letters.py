# Python code to create a function called most_frequent that takes a string and prints the letters in decreasing order of frequency.
import operator

n = input("Enter a string: ")

def most_frequent(n):
    d = dict()
    for i in n:
        if i not in d:
            d[i] = n.count(i)
    return sorted(d.items(), key=operator.itemgetter(1), reverse=True)

print(most_frequent(n))




