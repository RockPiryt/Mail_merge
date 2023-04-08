#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


PLACEHOLDER = "[name]" # word to change


#READLINES() METHOD
#change name file to list
with open("./Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines() # change text file to list
    print(names)
#['Aang\n', 'Zuko\n', 'Appa\n', 'Katara\n', 'Sokka\n', 'Momo\n', 'Uncle Iroh\n', 'Toph']

# REPLACE()and STRIP() METHOD
#open letter
with open("./Input/Letters/starting_letter.txt") as letter_file:
    letter_content = letter_file.read()
    for name in names:
        stripped_name = name.strip()#take away (remove) any spaces at the beginning and at the end
        letter_change_word = letter_content.replace(PLACEHOLDER, stripped_name)#Replace the word in text
        print(letter_change_word)
        with open(f"./Output/ReadyToSend/Letter_for_{stripped_name}", mode="w") as completed_letter:
           completed_letter.write(letter_change_word)# create new letter with names



