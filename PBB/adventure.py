end = 1
move = False
print("welcome to the ultamite Adventure")
name = input("What is your name? ")
print("You wake up in an unfamiliar place.")
print("A: look up at the tree you are under.")
print("B: look and see what is in your pocket.")
first_move = input("A or B: ") 
if first_move.capitalize() == 'A':
    end = end + 1
    move = True
        
else: 
    end = end - 1 
    move = False
if move:
    print("As you look you feel like someone is watching you.")
    second_move = "B"
    

else:
    print("You find a knife that you have never seen before.")
    print("what do you do with the knife?")
    print(" ")
    print("A: Leaf it by the tree... no pun intended.")
    print("B: keep a hold of it because you are scared.")
    second_move = input("A or B: ")


if second_move.capitalize == 'A':
    move = False
    end = end - 1
else:
    end = end + 1
print(f'You then hear in the middle of the woods a voice say,"{name.capitalize()} you should not have come this far without anyone to help you!')
print("What do you do:")
print("A: Run Away!")
print("B: Walk towrds the noice")
third_move = input("A or B: ")

if third_move.capitalize() == 'A':
    print("you fall and die")
    end = end - 1
        
else:
    end = end + 1


















    if end >= 2:
        print("You WIN!")
    else:
        print("LOOSER")
        
    #break
