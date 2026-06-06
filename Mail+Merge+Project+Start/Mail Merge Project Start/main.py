#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
with open("./input/letters/starting_letter.txt", "r") as letters:
    letters = letters.read()


with open("./input/Names/invited_names.txt", "r") as names:
    names = names.readlines()
    for name in names:
        stripped_name = name.strip()
        with open(f"./output/readytosend/{stripped_name}_letter.txt", "w") as new_letters:
            new_letters.write(letters.replace("[name]",stripped_name))
