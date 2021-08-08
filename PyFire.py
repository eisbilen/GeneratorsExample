import pyrebase

firebaseConfig = {
    "apiKey": "AIzaSyD5b16Ejf5wxsaswc8qIaTBXJTLW7xp8Oc",
    "authDomain": "lingomoo.firebaseapp.com",
    "databaseURL": "https://lingomoo.firebaseio.com",
    "projectId": "lingomoo",
    "storageBucket": "lingomoo.appspot.com",
    "messagingSenderId": "886228262297",
    "appId": "1:886228262297:web:4f391f1d1b68d595974708"}

firebase = pyrebase.initialize_app(firebaseConfig)

# Get a reference to the auth service
auth = firebase.auth()

# Log the user in
user = auth.sign_in_with_email_and_password("info@lingomoo.com", "Ece060809")

storage = firebase.storage()
# as admin
storage.child("images/example.jpg").put("background_1.jpg", user['idToken'])
