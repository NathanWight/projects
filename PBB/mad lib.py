# Welcome and instructions 
print("Hello welcome to your daily Mad Lib")
info = input("Do you know how Mad Libs work... yes or no? ")
if info == 'yes':
    print("Great lets continue!")
else:  # this makes it so they can understand what the program is doing or skip it.
    print(" ")
    print("You will be asked to give a random noun, adverb, verb or adjective.")
    print("After you select those it will fill them into a story.")
    print("P.S. If you don't laugh the program will Explode!")


# Get inputs to fill in the blanks
print("Fill in the Following...")
print(" ")
noun = input("Noun: ")
adverb = input("Adverb: ")
verb = input("verb: ")
adjective = input("Adective: ")
location = input("Choose a location: ")
noun = noun.capitalize()
# Take inputs and fill in to the mad lib
print(" ")# leaves a line in between the mad liband the inputs 
print(f"I love to visit {location} but only when it is snowing outside,") 
print(f"but I am always scared that I might run into my worst nightmare the {adjective} {noun}")
print(f"Little did I know that {noun} was {adverb} {verb} me!")
print(f"It wasnt untill I had spoken with the {adjective} tree fairy that i found out,")
print(f"that {noun} was acctualy my brother and he lived near {location} but only came out when it was {adverb} snowing!")


