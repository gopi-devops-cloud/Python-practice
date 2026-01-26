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

def encrypt(original_text, shift_amount):
    cipher_text = ""
    for letter in original_text:
        if letter in alphabet:
            shifted_position = (alphabet.index(letter) + shift_amount) % len(alphabet)
            cipher_text += alphabet[shifted_position]
        else:
            cipher_text += letter
    print(f"Here is your encoded result: {cipher_text}")

def decrypt(original_text, shift_amount):
    output_text = ""
    for letter in original_text:
        if letter in alphabet:
            shifted_position = (alphabet.index(letter) - shift_amount) % len(alphabet)
            output_text += alphabet[shifted_position]
        else:
            output_text += letter
    print(f"Here is your decoded result: {output_text}")


should_continue = True
while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    if direction == "encode":
        encrypt(original_text=text, shift_amount=shift)
    elif direction == "decode":
        decrypt(original_text=text, shift_amount=shift)
    else:
        print("Invalid choice. Please type 'encode' or 'decode'.")

    restart = input("Do you want to continue? Type 'yes' or 'no':\n").lower()
    if restart == "no":
        should_continue = False
        print("Goodbye ")



  