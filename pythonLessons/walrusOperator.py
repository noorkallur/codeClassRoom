keyList = list() #empty list
while (key := input("Enter a key: ")) != "quit": #walrus operator
    keyList.append(int(key))
print(keyList)