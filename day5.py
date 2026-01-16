fruits=( "apple","mango","banana","peach","pineapple")
for fruit in fruits:
    print(fruit)
    print(fruit + ' pie r')
  
print(fruits)

student_scores=[185,123,456,999,987,985,467,484,478,380]
student_sum=sum(student_scores)
print(student_sum)
max_score=0
for score in student_scores:
  if score>max_score:
   max_score=score
print(max_score)

sum_number=0
for number in range(1,101):
  sum_number+=number
print(sum_number)