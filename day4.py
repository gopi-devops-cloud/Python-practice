import random
random_integer = random.randint(1,10)
print(random_integer)
# 1 & 10 both included

#float number
random_number_0_to_1= random.random()
print(random_number_0_to_1) 
# include o but not 1

random_float=random.uniform(1,10)
print(random_float)
 
random_integar=random.randint(1,2)
if random_integar==1:
 print("heads")
else:
 print("tails")


fruits=(["cherry","apple","pear","orange"])
fruits.append(["mango","orange"])
fruits[0]="banana"
print (fruits[0])
print(fruits)