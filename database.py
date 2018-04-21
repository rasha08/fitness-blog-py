import pyrebase

from utils import filterArrayByKey, kebabCase, findInArray, isPostSelected

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

def getAllBlogPosts():
    return allBlogPosts

def getBlogHomePagePosts():
    return {
        'workoutPosts': {
            'title': 'Fitness Treninzi, Saveti i Vežbe',
            'posts': workoutPosts[:8],
            'link':
            '/fitnes-blog-saveti-za-zene/fitnes-treninzi-saveti-i-vezbe'
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

def getBlogCategory(category):
    if category == 'fitnes-treninzi-saveti-i-vezbe':
        return {
            'title': 'Fitnes Blog Za Žene - Fitness Treninzi, Saveti i Vežbe',
            'description': 'Fitness treninzi, saveti i vežbe, odgovori na pitanja: kako napredovati u teretani, kako brzo smršati, treninzi za ravan stomak, kako doći do izvajane zadnjice i savršenih nogu',
            'posts': workoutPosts,
            'link': '/fitnes-blog-saveti-za-zene/fitnes-treninzi-saveti-i-vezbe'
        }
    elif category == 'zdravlje-i-zdrave-navike':
        return {
            'title': 'Fitnes Blog Za Žene - Zdravlje i Zdrave Navike',
            'description': 'Zdravlje i zdrave navike, saznajte kako da sačuvate vaše zdravlje, koje zdrave navike vam mogu ojacati imunitet, koje su navike najbolje za vaš organizam',
            'posts': healthPosts,
            'link': '/fitnes-blog-saveti-za-zene/zdravlje-i-zdrave-navike'
        }
    elif category == 'zdrava-hrana-i-zdrava-ishrana':
        return {
            'title': 'Fitnes Blog Za Žene - Zdrava Hrana i Zdrava Ishrana',
            'description': 'Zdrava hrana i zdrava ishrana, saznajte sta je najbolje jesti pre ili posle treninga, koja je najbolja hrana za mršavljenje, kako da dijetom istopite masti',
            'posts': foodPosts,
            'link': '/fitnes-blog-saveti-za-zene/zdrava-hrana-i-zdrava-ishrana'
        }
    else:
        return[]

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
       