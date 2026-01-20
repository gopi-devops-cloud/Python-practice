import random
word_list=["gopi","shivam","arun","adi","rohit"]
choosen_word=random.choice(word_list)
print(choosen_word)
placeholder=""
word_length=len(choosen_word)
for position in range(word_length):
    placeholder += "_"
print(placeholder) 
game_over=False
correct_letters=[]
while not game_over :    
    user_guess=(input("guess a letter?\n")).lower()
    display = ""
    for letter in choosen_word:
        if letter == user_guess:
         display += letter
         correct_letters.append(letter)
        elif letter in correct_letters:
           display += letter
        else:
         display += "_"
    print(display)  
    if "_" not in display:
       game_over=True
       print("you win")