# def greet():
#     print("hello gopi")
#     print("you got it")
# greet()

# function that allows input
# def greet_with_name(name):
#     print(f"hello {name}")
#     print(f"what are you doing  {name}")
# greet_with_name("gopi")

#function with more then one input
# def greet_with(name,location):
#     print(f"hello {name}")
#     print(f"i live in {location}")
# greet_with("gopi","babugarh")

# # keyword argument
# greet_with(name="gopi",location="babugarh" )
alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m',
            'n','o','p','q','r','s','t','u','v','w','x','y','z']
direction=input("type 'encode' to encrypt,type 'decode' to decrypt:\n").lower()
text=input("type your message:\n").lower()
shift=int(input("type the shift number:\n"))

def encrypt(original_text,shift_amount):
    cipher_text=""
    for letter in original_text:
        shifted_position=alphabet.index(letter)+shift_amount
        shifted_position %= len(alphabet)
        cipher_text+=alphabet[shifted_position]

    print(f"here is your encode result: {cipher_text}")
encrypt(original_text =text,shift_amount=shift)