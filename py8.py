fname = open('cap.txt', 'r')

capital = fname.read()

print('Before : \n', capital)

print('After : \n',capital.upper())

fname.close()
