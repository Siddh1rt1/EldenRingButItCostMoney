from PIL import ImageGrab, Image
import numpy
import time
#img = Image.open('test.png')
import pyttsx3
from random import randrange
engine = pyttsx3.init()



ctest=[81,13,12]
cpe=20

left = 50
top = 52
right = 800
bottom = 53
lengthofarray=right-left
beleidigung=["failed","Du bist eine enttäuschung","Ich wünschte du wärest nicht so schlecht","Du legostein ohne noppen","ich glaube du bist einfach nur schlecht","Worst gamer ever","Wenn Jesus dich gerade sehen würde, wäre er sehr traurig"]
timeticker=0
lastvar=0
#time.sleep(5)
while True:
    print(timeticker)
    counter=0
    timeticker=timeticker+1
    img=ImageGrab.grab()
    width, height = img.size
    cropped = img.crop((left, top, right, bottom))
    #cropped.show()
    cropped.convert('RGB')
    x=0
    for x in range(0,lengthofarray,5):
        #print(x)
        r, g, b = cropped.getpixel((x,0))
        #print(r,g,b)
        #print(ctest)
        if ((ctest[0]-cpe)<=r<=(ctest[0]+cpe)) and ((ctest[1]-cpe)<=g<=(ctest[1]+cpe)) and ((ctest[2]-cpe)<=b<=(ctest[2]+cpe)) :
            
            counter=counter+1
    print(lastvar,counter)
    if lastvar >counter+5:
        print("OH NOO")

        text=beleidigung[randrange(len(beleidigung))]
        engine.say(text)
        engine.runAndWait()
    lastvar=counter
    print("redpixel: "+str(counter))
    time.sleep(0.5)
#r, g, b = cropped.getpixel((20,0))
#print(r,g,b)
