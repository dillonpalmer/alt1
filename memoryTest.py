import time
from time import time as the_timer
import datetime
import random
import time

from time import sleep

now = datetime.datetime.now()  #function that gets the current time and date
print (str(now)) #prints date and tie

print ("current year: {}".format(now.year))
print ("current month: {}".format(now.strftime("%B")))
print ("current day: {}".format(now.strftime("%A")))       
print ("current hour: {}".format(now.strftime("%H")))
print ("current minute: {}".format(now.strftime("%M")))

print("")
print ("REACTION GAME")
print("")
sleep(1)

print ("Level 1:")
sleep(1)
print ("Instructions:\nYou will press 'ENTER' to start the game.\nAfter a random amount of seconds the game will ask you to press 'ENTER' to stop.\nThe game will record your time but be fast!") 
sleep(3)
print("")

while True:
    input ("Please press 'ENTER' to start")
    print("  ")

    wait_time = random.randint(1,6)  #gets programme to wait a random amount of seconds between 1-6 seconds
    time.sleep(wait_time)
    start_time = the_timer()  #gets start time

    input ("Please press 'ENTER' to END")
    print("  ")

    end_time = the_timer()  #gets end time

    print("Game started at " + time.strftime("%X", time.localtime(start_time)))
    sleep(2)
    print("Game ended at " + time.strftime("%X", time.localtime(end_time)))
    sleep(2)
    print("  ")
    print ("Your reaction time was {}".format(end_time - start_time))  #finds reaction time by subtracting end time from start time
    sleep(2)

    reactionTime = end_time - start_time
    if reactionTime < 1:
        print ("You PASSED Level 1. Well Done.")
        break

    else:
        print ("You FAILED Level 1. Not good enough.")
        print("  ")
        sleep(1)
        x = input("Try again?\n*please enter 'yes' or 'no'*")
        print("  ")
        
        if x == "yes":
            print ("Very well...")
            print (" ")
        
        else:
            print("    ┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼ ")
            print("    ███▀▀▀██┼███▀▀▀███┼███▀█▄█▀███┼██▀▀▀ ")
            print("    ██┼┼┼┼██┼██┼┼┼┼┼██┼██┼┼┼█┼┼┼██┼██┼┼┼ ")
            print("    ██┼┼┼▄▄▄┼██▄▄▄▄▄██┼██┼┼┼▀┼┼┼██┼██▀▀▀ ")
            print("    ██┼┼┼┼██┼██┼┼┼┼┼██┼██┼┼┼┼┼┼┼██┼██┼┼┼ ")
            print("    ███▄▄▄██┼██┼┼┼┼┼██┼██┼┼┼┼┼┼┼██┼██▄▄▄ ")
            print("    ┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼ ")
            print("    ███▀▀▀███┼▀███┼┼██▀┼██▀▀▀┼██▀▀▀▀██▄┼ ")
            print("    ██┼┼┼┼┼██┼┼┼██┼┼██┼┼██┼┼┼┼██┼┼┼┼┼██┼ ")
            print("    ██┼┼┼┼┼██┼┼┼██┼┼██┼┼██▀▀▀┼██▄▄▄▄▄▀▀┼ ")
            print("    ██┼┼┼┼┼██┼┼┼██┼┼█▀┼┼██┼┼┼┼██┼┼┼┼┼██┼ ")
            print("    ███▄▄▄███┼┼┼─▀█▀┼┼─┼██▄▄▄┼██┼┼┼┼┼██▄ ")
            print("    ┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼ ")
            exit()
        
sleep(2)        
print("  ")

print("  .--.      .-'.      .--.      .--.      .--.      .--.      .`-.      .--.   ")
print(":::::.\::::::::.\::::::::.\::::::::.\::::::::.\::::::::.\::::::::.\::::::::.\  ")
print("'      `--'      `.-'      `--'      `--'      `--'      `-.'      `--'      ` ")

print("  ")

import random
from time import sleep

theList = ['shoe', 'desk', 'bed', 'mattress', 'poster', 'book',
           'copybook', 'watch', 'bottle', 'shoebox', 'sunglasses', 'newspaper',
           'trophy', 'television', 'speaker', 'bag', 'lamp', 'hairspray', 'chair',
           'girl', 'sock', 'card', 'clothes', 'pool', 'game', 'mirror',
           'computer', 'painting', 'sticker', 'laptop', 'pen', 'pencil']



def spaceOut():
    for i in range (0,20):  #this prevents the user from seeing the last output
        print("    ")
        
print ("Loading Level 2...")
print("  ")
print("  ")
sleep(3)        


print("Level 2:")
sleep(1)
print("  ")
print ("Instructions:\nThe programme will spit out 10 random words one after another.\nYou must memorise these words in the correct order.\nYou then must type the words back in to the programme one after the other.\nYou will receive a score at the end.")
print("**YOU MUST GET MORE THAN 5 OUT OF 10 TO MOVE TO LEVEL 3**")
print("   ")

while True:
    input("Please press ENTER to begin the countdown.")

    print ("Get ready, the programme will start in 10 seconds!!!")
    sleep(7)
    print("3")
    sleep(1)
    print("2")
    sleep(1)
    print("1")
    sleep(1)

    random.shuffle(theList) #shuffles list


    #print out 10 random words from list
    for i in range (0,10):
        spaceOut()
        print (theList[i])
        spaceOut()
        sleep(3)
        
    spaceOut()

    score = 0 #for keeping score
    
    print("Now we will check your answers.")
    print("  ")
    print("Please type in the first word and press enter...\n*use all lowercase letters in your answers*")
    for i in range(0,10):
        
        yourAns = input()
        if yourAns == theList[i]:
            print("CORRECT!!")
            score = score + 1 #adds one to the score for each correct answer
            
        else:
            print("INCORRECT!! The answer is " + theList[i])
            
    print("Your final score is " + str(score) + " out of 10")
    print ("  ")

    if score >= 5:
        print ("You PASSED level 2. Well done!")
        break
    else:
        print ("You FAILED Level 2. Not good enough.")
        print("  ")
        sleep(1)
        x = input("Try again?\n*please enter 'yes' or 'no'*")
        print("  ")
        
        if x == "yes":
            print ("Very well...")
            print (" ")
        
        else:
            print("    ┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼ ")
            print("    ███▀▀▀██┼███▀▀▀███┼███▀█▄█▀███┼██▀▀▀ ")
            print("    ██┼┼┼┼██┼██┼┼┼┼┼██┼██┼┼┼█┼┼┼██┼██┼┼┼ ")
            print("    ██┼┼┼▄▄▄┼██▄▄▄▄▄██┼██┼┼┼▀┼┼┼██┼██▀▀▀ ")
            print("    ██┼┼┼┼██┼██┼┼┼┼┼██┼██┼┼┼┼┼┼┼██┼██┼┼┼ ")
            print("    ███▄▄▄██┼██┼┼┼┼┼██┼██┼┼┼┼┼┼┼██┼██▄▄▄ ")
            print("    ┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼ ")
            print("    ███▀▀▀███┼▀███┼┼██▀┼██▀▀▀┼██▀▀▀▀██▄┼ ")
            print("    ██┼┼┼┼┼██┼┼┼██┼┼██┼┼██┼┼┼┼██┼┼┼┼┼██┼ ")
            print("    ██┼┼┼┼┼██┼┼┼██┼┼██┼┼██▀▀▀┼██▄▄▄▄▄▀▀┼ ")
            print("    ██┼┼┼┼┼██┼┼┼██┼┼█▀┼┼██┼┼┼┼██┼┼┼┼┼██┼ ")
            print("    ███▄▄▄███┼┼┼─▀█▀┼┼─┼██▄▄▄┼██┼┼┼┼┼██▄ ")
            print("    ┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼ ")
            exit()
sleep(1)                
print("  ")

print("  .--.      .-'.      .--.      .--.      .--.      .--.      .`-.      .--.   ")
print(":::::.\::::::::.\::::::::.\::::::::.\::::::::.\::::::::.\::::::::.\::::::::.\  ")
print("'      `--'      `.-'      `--'      `--'      `--'      `-.'      `--'      ` ")

print("  ")

print("Loading Level 3...")
print("  ")
print("  ")
sleep(3)        

from time import sleep
def spaceOut():
    for i in range (0,20):  #this prevents the user from seeing the last output
        print("    ")
        

print ("Level 3:")
print ("  ")
sleep(1)

print ("Intructions:\n1. I will tell you a short story")
print ("2. After you have read this story, the programme will ask you questions to see how well you paid attention.")
print ("3. BE CAREFUL because the questions will try to catch you out!!")
print ("*if you get a final score of less than 4 it is GAME OVER. No second chances*")
sleep(3)

print ("  ")
input("Press ENTER when you are ready to begin the story")

print("START")
sleep(1)
print ("  ")
print("One day George was at home alone in his bungalow near the seaside in Laois.")
sleep(8)

spaceOut()

print("He was in his bedroom listening to music.\nHe was listening to his favourite band, The Strokes.")
sleep(8)

spaceOut()

print("His sister was at work in Stradbally.\nHis brother was playing a football match in Portlaoise.")
sleep(8)

spaceOut()
    
print("His mam and dad were in the pub watching the rugby... Ireland Vs Fiji")
sleep(8)

spaceOut()
    
print("Suddenly, George hears a loud BANG in the kitchen. \nHe hears glass smashing and a something crashing to the ground.")
sleep(8)

spaceOut()

print("He grabs his Red Sox baseball bat and heads towards the kitchen.")
sleep(8)

spaceOut()

print("He slowly opens the kitchen door.\nHe finds his pitbull Otto on the table with his mams vase smashed on the ground beside an overturned chair.")
sleep(8)

spaceOut()
print("END")

score = 0 #with each correct answer the score will increase by 1

print ("  ")
input ("Press ENTER to begin the questions")
print ("  ")

print("1. Is there something wrong about the opening sentence...\nOne day George was at home alone in his bungalow near the seaside in Laois ")


while True:
    que1 = input("*please answer 'yes' or 'no'*")
    if que1 == "yes":
        print ("CORRECT. Laois is an inland county. There is no seaside.")
        score = score + 1
        break
    if que1 == "no":
        print("WRONG.  Laois is an inland county. There is no seaside.")
        break
    else:
        print("Could not recognise answer. Please try again.")
        print ("  ")
        
sleep(3)
print ("  ")
print ("  ")

print("2. George was upstairs listening to music when he heard the noise in the kitchen.")

while True:
    que2 = input("*please answer 'true' or 'false'*")
    if que2 == "false":
        print ("CORRECT. His house was a bungalow.")
        score = score + 1
        break
    if que2 == "true":
        print("WRONG. His house was a bungalow.")
        break
    else:
        print("Could not recognise answer. Please try again.")
        print ("  ")
        
sleep (3)

print ("  ")
print ("  ")

print("3. George's sister works in Portlaoise.")

while True:
    que3 = input("*please answer 'true' or 'false'*")
    if que3 == "false":
        print ("CORRECT. She works in Stradbally.")
        score = score + 1
        break
    if que3 == "true":
        print("WRONG. She works in Stradbally.")
        break
    else:
        print("Could not recognise answer. Please try again.")
        print ("  ")
        
sleep(3)

print ("  ")
print ("  ")

print("4. What country were Ireland playing against in the rugby? Was it...")
print("A. Finland\nB. Tonga\nC. Fiji")


while True:
    que4 = input("*please answer 'A', 'B' or 'C'*\n*use uppercase letters please*")
    if que4 == "C":
        print ("CORRECT. They were playing Fiji.")
        score = score + 1
        break
    if que4 == "B":
        print("WRONG. They were playing Fiji.")
        break
    if que4 == "A":
        print("WRONG. They were playing Fiji.")
        break
    else:
        print("Could not recognise answer. Please try again.")
        print ("  ")
        
sleep(3)

print ("  ")
print ("  ")

print("5. When George heard the loud bang, he grabbed a Yankees baseball bat")

while True:
    que5 = input("*please answer 'true' or 'false'*")
    if que5 == "false":
        print ("CORRECT. He grabbed a Red Sox bat.")
        score = score + 1
        break
    if que5 == "true":
        print("WRONG. He grabbed a Red Sox bat.")
        break
    else:
        print("Could not recognise answer. Please try again.")
        print ("  ")

sleep(3)

print ("  ")
print ("  ")

print("6. What breed was George's dog?")
print("A. Pitbull\nB. Bulldog\nC. Shih Tzu")

while True:
    que6 = input("*please answer 'A', 'B' or 'C'*\n*use uppercase letters please*")
    if que6 == "A":
        print ("CORRECT. He was a pitbull.")
        score = score + 1
        break
    if que6 == "B":
        print("WRONG. He was a pitbull.")
        break
    if que6 == "C":
        print("WRONG. He was a pitbull.")
        break
    else:
        print("Could not recognise answer. Please try again.")
        print ("  ")

sleep(3)

print ("  ")
print ("  ")

print ("For 2 points, can you tell me the name of the dog?")
print ("A. Oscar\nB. Otto \nC. Olli")

while True:
    que7 = input("*please answer 'A', 'B' or 'C'*\n*use uppercase letters please*")
    if que7 == "A":
        print ("WRONG. His name was Otto.")
        break
    if que7 == "B":
        print("CORRECT. His name was Otto.")
        score = score + 2
        break
    if que7 == "C":
        print("WRONG. His name was Otto.")
        break
    else:
        print("Could not recognise answer. Please try again.")
        print ("  ")
sleep(3)

print ("  ")
print ("  ")
        
print ("Calculating final score...")
sleep(4)

print(score)

if score >= 4:
    print ("WELL DONE. You passed.")
    sleep(3)
    print("You have passed all 3 levels and completed the Memory and reaction test.")

if score < 3:
    print ("You failed the level.")
    sleep(3)
    print("    ┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼ ")
    print("    ███▀▀▀██┼███▀▀▀███┼███▀█▄█▀███┼██▀▀▀ ")
    print("    ██┼┼┼┼██┼██┼┼┼┼┼██┼██┼┼┼█┼┼┼██┼██┼┼┼ ")
    print("    ██┼┼┼▄▄▄┼██▄▄▄▄▄██┼██┼┼┼▀┼┼┼██┼██▀▀▀ ")
    print("    ██┼┼┼┼██┼██┼┼┼┼┼██┼██┼┼┼┼┼┼┼██┼██┼┼┼ ")
    print("    ███▄▄▄██┼██┼┼┼┼┼██┼██┼┼┼┼┼┼┼██┼██▄▄▄ ")
    print("    ┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼ ")
    print("    ███▀▀▀███┼▀███┼┼██▀┼██▀▀▀┼██▀▀▀▀██▄┼ ")
    print("    ██┼┼┼┼┼██┼┼┼██┼┼██┼┼██┼┼┼┼██┼┼┼┼┼██┼ ")
    print("    ██┼┼┼┼┼██┼┼┼██┼┼██┼┼██▀▀▀┼██▄▄▄▄▄▀▀┼ ")
    print("    ██┼┼┼┼┼██┼┼┼██┼┼█▀┼┼██┼┼┼┼██┼┼┼┼┼██┼ ")
    print("    ███▄▄▄███┼┼┼─▀█▀┼┼─┼██▄▄▄┼██┼┼┼┼┼██▄ ")
    print("    ┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼ ")
    exit()
    
print("Thank you for playing")
sleep(2)

print("    ┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼ ")
print("    ███▀▀▀██┼███▀▀▀███┼███▀█▄█▀███┼██▀▀▀ ")
print("    ██┼┼┼┼██┼██┼┼┼┼┼██┼██┼┼┼█┼┼┼██┼██┼┼┼ ")
print("    ██┼┼┼▄▄▄┼██▄▄▄▄▄██┼██┼┼┼▀┼┼┼██┼██▀▀▀ ")
print("    ██┼┼┼┼██┼██┼┼┼┼┼██┼██┼┼┼┼┼┼┼██┼██┼┼┼ ")
print("    ███▄▄▄██┼██┼┼┼┼┼██┼██┼┼┼┼┼┼┼██┼██▄▄▄ ")
print("    ┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼ ")
print("    ███▀▀▀███┼▀███┼┼██▀┼██▀▀▀┼██▀▀▀▀██▄┼ ")
print("    ██┼┼┼┼┼██┼┼┼██┼┼██┼┼██┼┼┼┼██┼┼┼┼┼██┼ ")
print("    ██┼┼┼┼┼██┼┼┼██┼┼██┼┼██▀▀▀┼██▄▄▄▄▄▀▀┼ ")
print("    ██┼┼┼┼┼██┼┼┼██┼┼█▀┼┼██┼┼┼┼██┼┼┼┼┼██┼ ")
print("    ███▄▄▄███┼┼┼─▀█▀┼┼─┼██▄▄▄┼██┼┼┼┼┼██▄ ")
print("    ┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼ ")

exit()
