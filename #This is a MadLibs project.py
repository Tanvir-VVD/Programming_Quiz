#This is a MadLibs project 
#My name: Tanvir Singh 
#Who I collaborated with: Patrick Santos

print("************************************")
print("|                                  |")
print("|      Welcome to MadLibs          |") 
print("|                                  |")
print("************************************")

('''MadLibs is a fill-in-the-blanks story
game. The player must choose words based on the 
given prompts, and the computer will return a 
short story that includes the words the user chose.''')

play = input("Do you want to play MadLibs?(y/n) ")

if play == "y":
    person_name = input("Choose a name for a person: ")
    place = input("Choose a place: ")
    noun_1 = input("Choose a singlular noun: ")
    animal_1 = input("Choose an animal: ")
    adjective_1 = input("Choose an adjective for a feeling: ")
    adjective_2 = input("Choose an adjective: ")
    adjective_3 = input("Choose an adjective: ")
    animal_2 = input("Choose an animal: ")
    food = input("Choose a food: ")
    
    print("""
    Over break I am going camping with """ +person_name+""". It is important 
    to be prepared when camping at """+place+""" , so I made sure to pack a 
    sleeping bag, flashlight, and a """ +noun_1+""". The possibility of seeing a 
    """ +animal_1+""" makes me feel """ +adjective_1+""". I am excited to go 
    hiking on the """ +adjective_2+""" trail. If I see a """ +adjective_3 +""" """ +animal_2+"""
    on the hike, I will take it home as my new pet! The best part of 
    camping is eating """ +food+""" by the campfire!
    """)
    
    print("Thanks for playing! Goodbye!")
    
else:
    print("Goodbye!")