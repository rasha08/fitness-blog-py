import pyrebase

allBlogPosts = []
allCookPosts = []

config = {
  'apiKey': 'AIzaSyC_Mba3-WKoP0XHz-XjCNDf3yc8FIiUa7g',
  'authDomain': 'jelenastevanovic-cd802.firebaseapp.com',
  'databaseURL': 'https://jelenastevanovic-cd802.firebaseio.com',
  'projectId': 'jelenastevanovic-cd802',
  'storageBucket': 'jelenastevanovic-cd802.appspot.com',
  'messagingSenderId': '300544889679'
}
firebase = pyrebase.initialize_app(config)

database = firebase.database()
auth = firebase.auth()
storage = firebase.storage()

def getAllPosts():
	blogPosts = database.child('blogPosts').get()
	cookPosts = database.child('cookPosts').get()

	for post in blogPosts.each():
		allBlogPosts.append(post.val())

	for recipe in cookPosts.each():
		allCookPosts.append(recipe.val())

getAllPosts()