fname = open('py3.txt', 'a')

data = input('Enter data: ')

txt = fname.write(data)
# print('User data: ', txt)

fname.close()

fname = open('py3.txt', 'r')

read = fname.read()
print(read)

fname.close()
