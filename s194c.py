'''
Write a python program that reads a text file containing full-name of the employees
of a company and then from these names it extracts Last-name of employee and
stores them in sorted order in new file.
Input Text file contains names in format: First-name Middle-name Last-name
'''

fname = "oldS194C.txt"
newfname = "newS194C.txt"

with open(fname, 'r') as f:
    for name in f:
        lastName = name.split()
        # print(lastName[2])

        with open(newfname, 'a') as n:
            lastName = str(lastName[2])
            lastName = lastName + '\n'
            n.write(lastName)