

Conversations
Using 0.82 GB
Program Policies
Powered by Google
Last account activity: 9 hours ago
Details

import time
from time import time as the_timer
import datetime
import random
import time

from time import sleep

now = datetime.datetime.now()
print (str(now))

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


input ("Please press 'ENTER' to start")
print("  ")

wait_time = random.randint(1,6)
time.sleep(wait_time)
start_time = the_timer()

input ("Please press 'ENTER' to END")
print("  ")

end_time = the_timer()

print("Game started at " + time.strftime("%X", time.localtime(start_time)))
sleep(1)
print("Game ended at " + time.strftime("%X", time.localtime(end_time)))
sleep(1)
print("  ")
print ("Your reaction time was {}".format(end_time - start_time))

reactionTime = end_time - start_time

#posts the users score to firebase
from firebase import firebase
firebase = firebase.FirebaseApplication('https://alt1-react.firebaseio.com/', None)

postedData = {"Reaction Time": reactionTime}
firebase.post('/alt-react', postedData)

print ("Data posted.")
