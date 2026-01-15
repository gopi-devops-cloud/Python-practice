# # import random
# # random_integer = random.randint(1,10)
# # print(random_integer)
# # # 1 & 10 both included

# # #float number
# # random_number_0_to_1= random.random()
# # print(random_number_0_to_1) 
# # # include o but not 1

# # random_float=random.uniform(1,10)
# # print(random_float)
 
# # random_integar=random.randint(1,2)
# # if random_integar==1:
# #  print("heads")
# # else:
# #  print("tails")


# # fruits=(["cherry","apple","pear","orange"])
# # fruits.append(["mango","orange"])
# # fruits[0]="banana"
# # print (fruits[0])
# # print(fruits)

# # challange 
# friends=("alice","bob","charlie","david","emanuel")
# import random
# random_int=random.randint(0,4)
# print (friends[random_int])



# #combined
# fruits=["apple","mango","banana","pineapple","peach"]
# vegetables=["tomato","potato","onion",]
# fruits_vegetables=[fruits,vegetables]
# print(fruits_vegetables)

# day 4 projects
import random
user_choose=int(input("choose 0 for rock,1 for paper and 2 for scissors.\n"))
if user_choose==0:
  print("you choose rock")
elif user_choose==1:
  print("you choose paper")
elif user_choose==2:
  print("you choose scissors")
else:
  print("you typed invalid no")
computer_choose=random.randint(0,2)
if computer_choose==0:
  print("computer choose rock")
elif computer_choose==1:
  print("computer choose paper")
elif computer_choose==2:
  print("computer choose scissors")
if user_choose == computer_choose:
    print("draw")
elif (user_choose == 0 and computer_choose == 2) or \
     (user_choose == 1 and computer_choose == 0) or \
     (user_choose == 2 and computer_choose == 1):
    print("you win")
else:
    print("you lose")
