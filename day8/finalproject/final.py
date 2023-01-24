# https://en.wikipedia.org/wiki/Caesar_cipher
import art

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(art.logo)
def caesar(text , shift_number , dir):
    result_text = ""
    if dir == "decode":
        shift_number *=-1
    for i in text:
        if not i in alphabet:
            result_text += i
        else:
            prev_index =  alphabet.index(i)
            new_index = (prev_index + shift_number) % 26
            result_text += alphabet[new_index]
    if dir == "encode":
        print(f"The encoded text is {result_text}")
    else:
        print(f"The decoded text is {result_text}")
while True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(text, shift, direction)
    x = input("Type 'yes' if you want to go again. Otherwise type 'no'.")
    if x.lower() == "yes":
        continue
    else:
        print("Bye.")
        break
    