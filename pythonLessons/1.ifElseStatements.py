weight = input("Weight:-") #90 KG, 90 lb
lweight= weight.lower()
unitIndex = lweight.find("k")
print(unitIndex)
if unitIndex == -1:
    unitIndex = lweight.find("l")
    print(f'weight is {float(weight[:unitIndex]) *0.45} kg')
else:
    print(f'weight is {float(weight[:unitIndex])*(1/0.45)} lbs')


