#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
with open("./Input/Names/invited_names.txt", "r") as names:
    list_of_names = names.readlines()
for name in list_of_names:
    name = name.strip()
    with open("./Input/Letters/starting_letter.txt", "r") as s_letter:
        f_line = s_letter.readline()
        new_line = f_line.replace("[name]", name)
        content = s_letter.readlines()
        text = "".join(content)
        final_text = new_line + text
        with open(f"./Output/ReadyToSend/Letter_for_{name}", "w") as output:
            output.write(f"{final_text}")
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp