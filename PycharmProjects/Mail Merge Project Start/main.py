#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
PLACEHOLER ="[name]"

with open("./Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines()

with open("./Input/Letters/starting_letter.txt") as letter_file:
    letter_content = letter_file.read()
    for name in names:
        stripped_name = name.strip()
        new_letter = letter_content.replace(PLACEHOLER, stripped_name)
        with open(f"./Output/ReadyToSend/letter_for_{stripped_name}.txt", mode="w") as completed_letter:
            completed_letter.write(new_letter)


















# #print(f.readlines())
# for line in names:
#     letter = open("./Output/ReadyToSend/example.txt", "r")
#     new_letter = letter.replace(old_name, line)
#     old_name = line
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".


