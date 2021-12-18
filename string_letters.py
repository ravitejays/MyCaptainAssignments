# Write Python code to create a function called most_frequent that takes a string and prints the letters in decreasing order of frequency. Use dictionaries.
n = input("Please enter a String: ")

def most_frequent(string):
    d = dict()
    for i in string:
        if i in d:
            d[i] = d[i] + 1
        else:
            d[i] = 1
    return d

print(most_frequent(n))