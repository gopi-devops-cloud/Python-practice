# print("wlcome to cinemahouse")
# print("enter your top 3 movies")
# movies=[]
# a=input("enter your first movie: ")
# b=input("enter your second movie: ")
# c=input("enter your third movie: ")
# movies.append(a)
# movies.append(b)
# movies.append(c)
# print(movies)


list=[1,2,3,2,1]
copy_list=list.copy()
copy_list.reverse()
if (copy_list==list):
    print("palindrome")
else:
    print("not palindrome")