fn=open("text1.txt","r") #open file in read mode

fn1=open("odd.txt","w"); #open file in write mode

#read the content of the file line by line
content=fn.readlines()
print("Content\n",content) #Print the content of first file

for i in range(0, len(content)):
    if(i%2 == 0):
        fn1.write(content[i])
    else:
        pass
fn1.close()

fn1=open("odd.txt","r") #open file in read mode
cont1=fn1.read() #read the content of the file
print("\n\n Odd lines\n\n",cont1) #Print the content of the second file
fn.close()
fn1.close()
