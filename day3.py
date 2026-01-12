# print("welcome to the rollercoaster!")
# hight=int(input("what is your hight in cm? "))
# bill=0
# if hight>=120:
#     print("you can ride")
#     age=int(input("enter a age "))
#     if age<=12:
#      bill=5
#      print("child tickets are $5")
#     elif age <= 18:
#      bill=7
#      print("youth tickets are $7")
#     else :
#      bill=12
#      print("adults ticket are $12")
#     wants_photo=input("do you want to take a photo y for yes n for no ")
#     if wants_photo == "y":
#        bill+=3
#     print(f"your final bill is ${bill}")  
# else :
#  print("sorry you can't ride ")
    # module operator check odd and even
# num=int(input("enter a number"))
# if num%2==0:
#     print("even")
# else:
#     print("odd")

#pizza yummy
print("welcome to the pizza deliveries!")
size=input("what size do you want? S, M or L: ")
bill=0
if size == "S":
 bill=15
elif size=="M":
 bill=20
else:
 bill=25
pepperoni=input("do you want pepperoni for your pizza y for yes n for no ") 
if pepperoni== "y":
    if size=="S":
     bill+=2
    else:
      bill+=3
extra_cheese =input("do you want extra_cheese y for yes n for no ")
if extra_cheese=="y":
 bill+=1
print(f" your total bill is ${bill}")


    
