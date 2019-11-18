from firebase import firebase
firebase = firebase.FirebaseApplication('https://alt1-8f179.firebaseio.com', None)

firebase.delete('/MyTemperatures/Delete', None)

print ("Delete completed")
