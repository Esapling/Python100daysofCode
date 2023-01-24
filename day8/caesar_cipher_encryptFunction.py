alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

encrypted_text = ""

def encrypt(text_message, shift_number):
    for i in text_message:
        # to solve unbound local error for encrypted_text
        global encrypted_text #https://docs.python.org/3/faq/programming.html#why-am-i-getting-an-unboundlocalerror-when-the-variable-has-a-value
        prev_index = alphabet.index(i)
        new_index = (prev_index + shift_number) % 26
        encrypted_text += alphabet[new_index]
    print("The encoded text is " + encrypted_text)

    #TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.  
    #e.g. 
    #plain_text = "hello"
    #shift = 5
    #cipher_text = "mjqqt"
    #print output: "The encoded text is mjqqt"

    ##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛
    # solved with modulo 

encrypt(text, shift)