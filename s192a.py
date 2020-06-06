'''
Write a python program that reads a text file and changes
the file by capitalizing each character of file.
'''

fname = open('s192a.txt', 'r')

capital = fname.read()

print('Before : \n', capital)

print('After : \n',capital.upper())

fname.close()
