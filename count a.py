#Store a list of names. Count the occurrences of ‘a’ within the list
Astr=input("enter the string\n")
char=input("enter the character\n")
print("Given String:\n", Astr)
print("Given Character:\n",char)
res = 0
for i in range(len(Astr)):
    # Checking character in string
    if (Astr[i] == char):
       res = res + 1
print("Number of time character is present in string:\n",res)
