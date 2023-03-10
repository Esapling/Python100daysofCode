contents = ""
with open("metin.txt") as file:
    contents = file.read()

with open("new.txt", mode="w") as new_file:
    new_file.write(contents)

with open("new.txt", mode="r") as file:
    print(file.read())
