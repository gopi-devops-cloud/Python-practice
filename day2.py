# # # subscripting also work on backward -1 still gives o
print("hello"[4])

# string inside string all treat same as like simpel text even number
print ("123" + "345")


# integer = whole number
print (123+456)


# large integers
print(123_456_789)

#FLOAT=Floating point number
print(3.14159)

# Boolean
print(True)
print(False)

# DATA TYPES FINDES
print (type("hellow"))
print (type(12345))
print(type(True))
print(type(3.148))

# mathematical operation (+,-,*,/)
print(2**3)
print(5/3) #output=1.66666666667
print(5//3) #output=1

#PEMDAS
# ()
# **
# * OR /
# + OR -

print(3*(3+3)/3-3)

# rounding a number
print(round(3.9))

bmi=84/1.65**2
print(round(bmi,2))

score=0
score += 1
print(score)
print("your score is " + str(score))

 # f-strings
score=0
height=1.8
is_winning = True

print(f"your score is = {score}, your height is {height}, you are winning is {is_winning} ")