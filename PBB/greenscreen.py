from PIL import Image 
#To start the user picks a bacground and a greenscreen image to overlay 
print("Background choices are: Forest, Earth, Field, Showscape, Beach, Sunset")
print()
background = input("What do you want the back ground to be? ")
print()
print("Greenscreen choices are: Cat, Harvester, Hiker, Spaceshuttle, Penguin, Boat, Cat, Cat_Small, Cactus ")
print()
greenscreen = input("What greenscreen would you like to use? ")
ending = ".jpg"

#the inputs are saved into variables that can then be used to open and load the image
greenscreen = greenscreen.lower() + ending
background = background.lower() + ending

#open and load the images
green = Image.open(greenscreen)
pixals = green.load()

background_image = Image.open(background)
back_pixals = background_image.load()

#This just tells us what green is for the image the user selected and prints it for fun
(r, g, b) = pixals[100, 500]
print(r, g,b)

dog = 5 # this is for fun lol needed the if statment to do something 

#This is where we go through pixal by pixal and select the not green areas and save them
for x in range (0, 800):
    for y in range (0, 600):
        back_pixals[x, y]
        (red, green, blue) = pixals[x, y]
        if red < r + 20 and green > g - 100 and blue < b + 20:
            dog = dog + 1 #Do some fun math that means nothing 
        else:
            back_pixals[x,y] = (red, green, blue)
        
background_image.show()
#Lastly save the image to the name the user wants 
save = input("What would you like to name this file as? ")  
save = save + ending     
background_image.save(save)
