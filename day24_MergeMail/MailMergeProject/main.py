# some helpful links 
 # https://www.w3schools.com/python/ref_file_readlines.asp
    # https://www.w3schools.com/python/ref_string_replace.asp
        # https://www.w3schools.com/python/ref_string_strip.asp
    
    
location_example_letter = "Input/Letters/starting_letter.txt"
location_new_letters = "Input/Names/invited_names.txt"

example_letter = ""
with open(location_example_letter, "r") as ex:
       example_letter = ex.read()
       #print(example_letter)
       
with open(location_new_letters, "r") as names_file:
    names = names_file.read().splitlines() # a list of names
    for name in names:
        new_letter = example_letter.replace("[name]", name) 
        text_name = "letter_for_" + name
        with open(f"Output/ReadyToSend/{text_name}.txt", "w") as letter:
            letter.write(new_letter)
