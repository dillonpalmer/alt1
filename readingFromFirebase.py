from firebase import firebase
firebase = firebase.FirebaseApplication('https://alt1-8f179.firebaseio.com/MyTemperatures/', None)

#reads the full database
result = firebase.get('/MyTemperatures', None)
print(result)
print("  ")


#finds the path to get TEMPERATURE
result = firebase.get('-Lt-aUgmnhj-0j_Yd40c/Temperature', None)

#puts temperature in a string
result1 = (str(result))
print("Temperature: " + result1)

#finds the path to get TIME
result2 = firebase.get('-Lt-aUgmnhj-0j_Yd40c/Time', None)

#puts time in a string
result_2 = str(result2)
print("Time: " + result_2)

