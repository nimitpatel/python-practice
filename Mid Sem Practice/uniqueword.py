fname="sample.txt"
f=open(fname,'r')
st=f.read()
st1=st.lower()
b=st1.split()

myset=set(b)

print("number of unique words",len(myset))
f.close()
f=open("sample.txt","r")
line=0
for lines in f:
    line+=1
print("number of lines",line)    
f.close()


"""fname=input("enter file name")
num_lines=0
with open(fname,"r") as f:
    for line in f:
        num_lines+=1
        print("lines",num_lines)
f.close()        

f=open(fname,"w")        
  for word in words:
      words=f.split()
    if word not in words:
        file.write(str(word)+"\n")

file.close()  
input_file=open("sample.txt","r")
f=input_file.read()
word=f.split()

file=open("sample1.txt","w")

for words in word:
    if words not in word:
        file.write(str(words) + "\n")
#f.close()        
def unique_file(input_filename, output_filename):
    input_file = open("sample.txt", 'r')
    file_contents = input_file.read()
    input_file.close()
    word_list = file_contents.split()
    file = open("sample1.txt", 'w')
    for word in word_list:
        if word not in word_list:
            file.write(str(word) + "\n")
            file.close()
"""
