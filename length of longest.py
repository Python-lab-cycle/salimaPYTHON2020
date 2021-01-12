str = input("Enter the list of words(Comma separated): ")
list = str.split()
print(list)
max1 = len(list[0])
temp = list[0]
for i in list:
    if (len(i) > max1):
        max1 = len(i)
        temp = i
print("Longest word in the list is: ", temp)
print("Length of ", temp, "is: ", len(temp))
