programming_dictionary ={
    "Function":"recipe of steps.",
    "Loop " : "repeat until condition changes.",
    "Bug":" mistake causing wrong behavior.",
    123:"without ("") this" 
}

print(programming_dictionary["Function"])
# without "" in number
print(programming_dictionary[123])
# adding new item in dictionary
programming_dictionary["item"]="new item"
print(programming_dictionary)
# empty dictionaries
empty_dictionary={}
# #wipe an existing dictionary
programming_dictionary={}
print(programming_dictionary)
# edit an item in dictionary?
programming_dictionary[123]="edited dictionary"
print(programming_dictionary)
# loop through dictionary
# wrong method
# for thing in programming_dictionary:
#     print(thing)
# right method
for key in programming_dictionary:
    print(key)
# but if want def also of key
    print(programming_dictionary[key])