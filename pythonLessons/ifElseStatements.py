# weight = input("Weight: ")
# lweight= weight.lower()
# if lweight.find('l') != -1 :
#     print(f'weight is {float(weight[:-1]) *0.45} kg')
# elif lweight.find('k') != -1:
#     print(f'weight is {float(weight[:-1])*(1/0.45)} lbs')
# else:
#     while(1):
#         unit = input("Is it (L)bs or (K)g? ")
#         if(unit.lower() == "l"):
#             print(f'weight  is {float(weight)*0.45} kg')
#             break
#         elif(unit.lower() == "k"):
#             print(f'weight  is {float(weight)*(1/0.45)} lbs')
#             break
#         else:
#             print("enter the right unit, either l or k")


# short hand if else statements

a = 10
b = 2
print("A") if a > b else ""

c = 1 if a > b else 0
print(c)

