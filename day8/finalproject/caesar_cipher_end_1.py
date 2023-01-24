alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Combine the encrypt() and decrypt() functions into a single function called caesar(). 

result_text = ""
def ceasar(text , shift_number , dir):
    global result_text
    if dir == "decode":
        shift_number *=-1
    for i in text:
        prev_index =  alphabet.index(i)
        new_index = (prev_index + shift_number) % 26
        result_text += alphabet[new_index]
    if dir == "encode":
        print(f"The encoded text is {result_text}")
    else:
        print(f"The decoded text is {result_text}")
    # one way to make this if in one line 
    # print(f"The {dir}d text is {result_text}") // {encode}d or {decode}d  
ceasar(text, shift, direction)