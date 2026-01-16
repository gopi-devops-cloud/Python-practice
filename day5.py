# fruits=( "apple","mango","banana","peach","pineapple")
# for fruit in fruits:
#     print(fruit)
#     print(fruit + ' pie r')
  
# print(fruits)

# student_scores=[185,123,456,999,987,985,467,484,478,380]
# student_sum=sum(student_scores)
# print(student_sum)
# max_score=0
# for score in student_scores:
#   if score>max_score:
#    max_score=score
# print(max_score)

# sum_number=0
# for number in range(1,101):
#   sum_number+=number
# print(sum_number)

# day5 project
import random
letters= ['a','b','c','d','e','f','g','A','B','C','D','L']
number=['0','1','2','3','5','6','7']
symbol=['!','$','#','*']

print("welcome to the pypassword Generator!")
nr_letter=int(input("how many letter do you want.\n"))
nr_symbol=int(input("how many symbol do you want.\n"))
nr_number=int(input("how many number do you want.\n"))
# easy level
password=""
for char in range(0,nr_letter):
  password+=random.choice(letters)
for char in range(0,nr_symbol):
  password+=random.choice(symbol)
for char in range(0,nr_number):
  password+=random.choice(number)
print(password)