import pyrebase

from utils import filterArrayByKey, kebabCase, findInArray, isPostSelected
from seo import addSeoEntitiesForCategory

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
    global breakfastPosts
    global lunchPosts
    global dinnerPosts
    

    allCookPosts = []
    allBlogPosts = []
    workoutPosts = []
    healthPosts = []
    foodPosts = []
    breakfastPosts = []
    lunchPosts = []
    dinnerPosts = []

    blogPosts = database.child('blogPosts').get()
    cookPosts = database.child('cookPosts').get()

    for post in blogPosts.each():
        allBlogPosts.append(post.val())

    for recipe in cookPosts.each():
        allCookPosts.append(recipe.val())

    workoutPosts = filterArrayByKey(allBlogPosts, 'category', 'vežbanje')
    healthPosts = filterArrayByKey(allBlogPosts, 'category', 'zdravlje')
    foodPosts = filterArrayByKey(allBlogPosts, 'category', 'hrana')

    breakfastPosts = filterArrayByKey(allCookPosts, 'category', 'doručak')
    lunchPosts = filterArrayByKey(allCookPosts, 'category', 'ručak')
    dinnerPosts = filterArrayByKey(allCookPosts, 'category', 'večera')

def getAllBlogPosts():
    return allBlogPosts

def getAllCookPosts():
    return allCookPosts

def getBlogHomePagePosts():
    return {
        'workoutPosts': {
            'title': 'Fitness Treninzi, Saveti i Vežbe',
            'posts': workoutPosts[:8],
            'link':
            '/fitnes-blog-saveti-za-zene/fitnes-treninzi-saveti-i-vezbe',
        },
        'healthPosts': {
            'title': 'Zdravlje i Zdrave Navike',
            'posts': healthPosts[:8],
            'link': '/fitnes-blog-saveti-za-zene/zdravlje-i-zdrave-navike'
        },
        'foodPosts': {
            'title': 'Zdrava Hrana i Zdrava Ishrana',
            'posts': foodPosts[:8],
            'link': '/fitnes-blog-saveti-za-zene/zdrava-hrana-i-zdrava-ishrana'
        }
    }


def getBlogPageSidebar():
    return {
        'workoutPosts': {
            'title': 'VEŽBANJE',
            'posts': workoutPosts
        },
        'healthPosts': {
            'title': 'ZDRAVLJE',
            'posts': healthPosts
        },
        'foodPosts': {
            'title': 'HRANA',
            'posts': foodPosts
        }
    }

def getCategoryPosts(baseUrl, categoryUrl):
    if categoryUrl == 'fitnes-treninzi-saveti-i-vezbe':
        posts = workoutPosts
    elif categoryUrl == 'zdravlje-i-zdrave-navike':
        posts = healthPosts
    elif categoryUrl == 'zdrava-hrana-i-zdrava-ishrana':
        posts = foodPosts
    elif categoryUrl == 'najbolji-recepti-za-fitnes-dorucak':
        posts = breakfastPosts
    elif categoryUrl == 'najbolji-recepti-za-fitnes-rucak':
        posts = lunchPosts
    elif categoryUrl == 'najbolji-recepti-za-fitnes-veceru':
        posts = dinnerPosts
    else:
        return None
    
    return addSeoEntitiesForCategory(baseUrl, categoryUrl, posts)

def getSingleBlogPost(categoryUrlSlug, postNameUrlSlug):
    if categoryUrlSlug == 'fitnes-treninzi-saveti-i-vezbe':
        posts = workoutPosts
    elif categoryUrlSlug == 'zdravlje-i-zdrave-navike':
        posts = healthPosts
    else:
        posts = foodPosts
    
    print(categoryUrlSlug)

    return findInArray(
        lambda singlePost: isPostSelected(singlePost, postNameUrlSlug),
        posts
    )

def getCookPagePosts():
    return {
        'breakfastPosts': {
            'title': 'Najbolji Recepti Za Vaš Fitnes Doručak',
            'posts': breakfastPosts[:4],
            'link':
            '/fitnes-kuvar-zdrava-hrana-recepti/najbolji-recepti-za-fitnes-dorucak'
        },
        'lunchPosts': {
            'title': 'Najbolji Recepti Za Vaš Fitnes Ručak',
            'posts': lunchPosts[:4],
            'link': '/fitnes-kuvar-zdrava-hrana-recepti/najbolji-recepti-za-fitnes-rucak'
        },
        'dinnerPosts': {
            'title': 'Najbolji Recepti Za Vašu Fitnes večeru',
            'posts': dinnerPosts[:4],
            'link': '/fitnes-kuvar-zdrava-hrana-recepti/najbolji-recepti-za-fitnes-veceru'
        }
    }

def getCookPageSidebar():
    return {
        'breakfastPosts': {
            'title': 'DORUČAK',
            'posts': breakfastPosts
        },
        'lunchPosts': {
            'title': 'RUČAK',
            'posts': lunchPosts
        },
        'dinnerPosts': {
            'title': 'VEČERA',
            'posts': dinnerPosts
        }
    }
