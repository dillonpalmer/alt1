from time import sleep
from firebase import firebase
firebase = firebase.FirebaseApplication('https://alt1-8f179.firebaseio.com/MyTemperatures/', None)

#reads the full database
result = firebase.get('/MyTemperatures', None)
print(result)
print("  ")

#reads the latest piece of data
names = []

for name in result:
    names.append(name)
    
result1 = (str(result))
print("Latest data recorded...")
sleep(1)
print(" ")

print("Temperature: ", result[names[-1]]['Temperature'])
print("Time: ", result[names[-1]]['Time'])
