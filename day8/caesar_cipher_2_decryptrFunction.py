alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

encrypted_text = ""

def encrypt(text_message, shift_number):
    global encrypted_text 
    # to solve unbound local error for encrypted_text
#https://docs.python.org/3/faq/programming.html#why-am-i-getting-an-unboundlocalerror-when-the-variable-has-a-value
    for i in text_message:
        prev_index = alphabet.index(i)
        new_index = (prev_index + shift_number) % 26
        encrypted_text += alphabet[new_index]
    print("The encoded text is " + encrypted_text)


decrypted_text = ""
def decrypt(text, shift_number):
    global decrypted_text
    for i in text:
        prev_index =  alphabet.index(i)
        new_index = (prev_index - shift_number) % 26
        decrypted_text += alphabet[new_index]
    print("The decoded text is " + decrypted_text)
 
while True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt or stop to end the program:\n")
    if direction == "encode":
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        encrypt(text, shift)
    elif direction == "decode":
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        decrypt(text, shift)
    else:
        print("Bye!")
        break