#write a program to read a file line by line and store it into a list

fn=open("text1.txt","r")
#read the content of the file by line
list=fn.readlines()
print("Content of file\n\n",list)
fn.close()
