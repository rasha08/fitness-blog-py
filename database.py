import pyrebase

from utils import filterArrayByKey, kebabCase

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
    global allBlogPosts
    global allCookPosts
    global workoutPosts
    global healthPosts
    global foodPosts
    global blogPostsHomePagePosts

    allCookPosts = []
    allBlogPosts = []
    workoutPosts = []
    healthPosts = []
    foodPosts = []
    blogPostsHomePagePosts = []

    blogPosts = database.child('blogPosts').get()
    cookPosts = database.child('cookPosts').get()

    for post in blogPosts.each():
        allBlogPosts.append(post.val())

    for recipe in cookPosts.each():
        allCookPosts.append(recipe.val())

    workoutPosts = filterArrayByKey(allBlogPosts, 'category', 'vežbanje')
    healthPosts = filterArrayByKey(allBlogPosts, 'category', 'zdravlje')
    foodPosts = filterArrayByKey(allBlogPosts, 'category', 'hrana')


def getBlogPostPagePosts():
    return {
        'workoutPosts': {
            'title': 'Fitness Treninzi, Saveti i Vežbe',
            'posts': workoutPosts[:6],
            'link':
            '/fitnes-blog-saveti-za-zene/fitnes-treninzi-saveti-i-vezbe'
        },
        'healthPosts': {
            'title': 'Zdravlje i Zdrave Navike',
            'posts': healthPosts[:6],
            'link': '/fitnes-blog-saveti-za-zene/zdravlje-i-zdrave-navike'
        },
        'foodPosts': {
            'title': 'Zdrava Hrana i Zdrava Ishrana',
            'posts': foodPosts[:6],
            'link': '/fitnes-blog-saveti-za-zene/zdrava-hrana-i-zdrava-ishrana'
        }
    }


def getAllBlogPosts():
    return allBlogPosts


def getWorkoutPosts():
    return workoutPosts


def getHealthPosts():
    return healthPosts


def getFoodPosts():
    return foodPosts


def getBlogPageSidebar():
    return {
        'workoutPosts': {
            'title': 'VEŽBANJE',
            'posts': workoutPosts,
            'link':
            '/fitnes-blog-saveti-za-zene/fitnes-treninzi-saveti-i-vezbe'
        },
        'healthPosts': {
            'title': 'ZDRAVLJE',
            'posts': healthPosts,
            'link': '/fitnes-blog-saveti-za-zene/zdravlje-i-zdrave-navike'
        },
        'foodPosts': {
            'title': 'HRANA',
            'posts': foodPosts,
            'link': '/fitnes-blog-saveti-za-zene/zdrava-hrana-i-zdrava-ishrana'
        }
    }
