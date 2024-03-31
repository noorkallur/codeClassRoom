# # A dictionary in Python is a data structure that stores the value in key:value pairs.
# student = {
#     'name': "Noor Kallur",
#     'age':26,
#     'is_accepted':False,
#     0:13
# }
# student['exp'] = 4.5 #update the dict

# print(student['name'])

# # # Performing list(d) on a dictionary returns a list of all the keys used in the dictionary, in insertion order 
# print(list(student))

# # # if you want it sorted, just use sorted(d) instead, this only works for same data type
# # print(sorted(student))

# # # To check whether a single KEY is in the dictionary, use the in keyword.
# print('name' in student)
# print('Noor Kallur' in student) #only key values can be searched using "in"

# # # using getter function for getting the values of the key is better because code does not throw a error
# print(student.get('name')) #returns the value of the key
# print(student.get('Name')) # returns none if not found in dict
# print(student.get('Name', 'not available')) # returns none if not found in dict, and returns default value given by us in the second arg

# # more on dicts check out https://docs.python.org/3/tutorial/datastructures.html#dictionaries

# # wap to print the input number in string format
# digits_in_string = {
#     '1' :'one',
#     '2' : 'two',
#     '3' : 'three',
#     '4' : 'four'
# }
# phone_number = input('enter your phone number = ')

# output=''
# for ch in phone_number:
#     output +=digits_in_string.get(ch, '!') +" "
# print(output)

# # swear word censor
swear_words= {
    "hell" : "H***",
    "shit" : "💩"
}

input_message = input("Enter your message > ")
words = input_message.split(" ")
output = ""

for word in words:
    output += swear_words.get(word, word) + " "
print(output)


# # dict comprehensions: