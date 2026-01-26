import random
word_list=["gopi","shivam","arun","adi","rohit"]
lives=(6)
choosen_word=random.choice(word_list)
placeholder=""
word_length=len(choosen_word)
for position in range(word_length):
    placeholder += "_"
print(placeholder) 
game_over=False
correct_letters=[]
while not game_over :   
    print(f"{lives}/6 lives remaining") 
    user_guess=(input("guess a letter?\n")).lower()
    if user_guess in correct_letters:
       print(f"you already guessed {user_guess}")
       
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
    if user_guess not in choosen_word:
       lives-=1
       print(f"you guessed {user_guess},is not in the word you lose a life.")
       if lives==0:
          game_over=True
          print(f"It was {choosen_word} you lose ")
    if "_" not in display:
       game_over=True
       print("you win")