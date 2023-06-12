from deep_translator import GoogleTranslator
import csv

# translates the text in a txt file named words.txt and
# writes the meaning into a csv as a definition and meaning tuples

def translate_text(text):
    translator = GoogleTranslator(source='en', target='tr')
    translated = translator.translate(text)
    return translated

word_list = []
try:
    with open("words.txt", "r") as word_file:
        for line in word_file:
            # Process each line here
            definition = line.strip()  # removes leading/trailing whitespaces
            #print(definition)
            meaning = translate_text(definition)
            #print(meaning)
            word_tuple = (definition, meaning)
            word_list.append(word_tuple)
        # print(word)
except FileNotFoundError:
    print("File couldnt opened")
else:
    with open("translated_text.csv", mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(word_list)