#Count the occurrences of each word in a line of text.
line=input("Enter the line:")
counts={}
sentence=line.split()
for word in sentence:
             if word in counts:
                     counts[word]+=1
             else:
                     counts[word] = 1
for k, v in counts.items():
          print(k, v)
