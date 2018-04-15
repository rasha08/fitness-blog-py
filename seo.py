import re
from  functools import reduce

# global module variables
baseUrl = 'http://jelenastevanovic.rs'
imageUrl = 'http://res.cloudinary.com/dgq2ohvtq/image/upload/v1474474686/2-min_bsksuq.jpg'
blogPageKeywords = ''
cookPageKeywords = ''

def getMetaTagsForEntyty(entity, url = '', posts = None, post = None):
	if entity == 'home':
		return getHomePageMetaTags(url)
	elif entity == 'services':
		return getServicesPageMetaTags(url)
	elif entity == 'galery':
		return getGaleryPageMetaTags(url)
	elif entity == 'blog':
		return getBlogPageMetaTags(url, posts)
	elif entity == 'cook':
		return getCookPageMetaTags(url, posts)
	elif entity == 'blogPost':
		return getBlogPostPageMetaTags(url, post)
	elif entity == 'cookPost':
		return getcookPostPageMetaTags(url, post)


def getHomePageMetaTags(url):
	return {
		'title': 'Jelena Stevanovic - Novi Sad - Licni Fitnes Trener Za Zene',
		'description': 'Personalni treninzi za zene u Novom Sadu, lako do savrsene figure, programi za osobe sa povredama ledja i lumbalnog dela kicme, mrsavljenje, zatezanje i pravljenje plana ishrane za brze rezultate',
		'url': baseUrl,
		'image': imageUrl,
		'keywords': 'jelena,stevanovic,individualni,treninzi,novi,sad,kako,je,svaka,osoba,individua,za,sebe,,moramo,razlikovati,osobe,kojima,je,potrebna,dodatna,motivacija,i,konstantna,podrška,u,vezbanju'
	}
def getServicesPageMetaTags(url):
	return {
		'title': 'Jelena Stevanovic, Individualni Treninzi - Novi Sad - Personalni Fitnes Trener Za Zene',
		'description': 'Kako je svaka osoba individua za sebe, moramo razlikovati osobe kojima je potrebna dodatna motivacija i konstantna podrška u vezbanju.',
		'url': baseUrl + url,
		'image': imageUrl,
		'keywords': 'jelena,stevanovic,individualni,treninzi,novi,sad,kako,je,svaka,osoba,individua,za,sebe,,moramo,razlikovati,osobe,kojima,je,potrebna,dodatna,motivacija,i,konstantna,podrška,u,vezbanju'
	}

def getGaleryPageMetaTags(url):
	return {
		'title': 'Jelena Stevanovic, Galerija Slika - Novi Sad - Licni Fitnes Trener Za Zene',
		'description': 'Individualni treninzi omogućavaju osobi da napreduje i razvija se u skladu sa svojim zeljama i potrebama na dosta brzi i pravilniji način.',
		'url': baseUrl + url,
		'image': imageUrl,
		'keywords': 'jelena,stevanovic,galerija,slika,novi,sad,individualni,treninzi,omogućavaju,osobi,da,napreduje,i,razvija,se,u,skladu,sa,svojim,zeljama,i,potrebama,na,dosta,brzi,i,pravilniji,način'
	}

def getBlogPageMetaTags(url, posts):
	return {
		'title': 'Fitness Blog Za Zene - Personalni Trener Jelena Stevanovic - Licni Trener Novi Sad',
		'description': 'Najnoviji tesktovi i odgovori na pitanja: kako napredovati u terertani, kako brzo smrsati, dijete za ravan stomak, lako do trbusnjaka, zatezanje zadnjicem, kako se resiti celulita.',
		'url': baseUrl + url,
		'image': imageUrl,
		'keywords': generateKewordsForPage(posts)
	}

def getCookPageMetaTags(url, posts):
	return {
		'title': 'Fitness Kuvar Za Zene - Personalni Trener Jelena Stevanovic',
		'description': 'Najnoviji recepti i saveti kako da budete vitki, imate savrsenu liniju i kako da ishranom dovedete svoje telo do savrsene forme',
		'url': baseUrl + url,
		'image': imageUrl,
		'keywords': generateKewordsForPage(posts)
	}

def getBlogPostPageMetaTags(url, post):
	return {
		'title': 'Fitness Blog Za Zene - Personalni Trener Jelena Stevanovic - Licni Trener Novi Sad',
		'description': 'Najnoviji tesktovi i odgovori na pitanja: kako napredovati u terertani, kako brzo smrsati, dijete za ravan stomak, lako do trbusnjaka, zatezanje zadnjicem, kako se resiti celulita.',
		'url': baseUrl + url,
		'image': imageUrl,
		'keywords': generateKewordsForPost(post)
	}

def getCookPostPageMetaTags(url, post):
	return {
		'title': 'Fitness Blog Za Zene - Personalni Trener Jelena Stevanovic - Licni Trener Novi Sad',
		'description': 'Najnoviji tesktovi i odgovori na pitanja: kako napredovati u terertani, kako brzo smrsati, dijete za ravan stomak, lako do trbusnjaka, zatezanje zadnjicem, kako se resiti celulita.',
		'url': baseUrl + url,
		'image': imageUrl,
		'keywords': generateKewordsForPost(post)
	}


def generateKewordsForPage(posts) :
 	return reduce(
 		(lambda prev, curr: prev + ',' + curr),
    	filter(
    		lambda word: prepareWordForKeywords(word),
			list(
				map(
					lambda post: prepareWordForKeywords(post['title'].lower()),
					posts
				)
			)
      	)
    )

def generateKewordsForPost(post):
    return reduce(
    	(lambda prev, curr: prev + ',' + curr),
    	filter(
    		lambda word: prepareWordForKeywords(word),
    		(post['title'].lower() + post['description'].lower()).split(' ')
    	)
    )

def prepareWordForKeywords(word):
    preparedWord = re.sub(r"/^je$/g", '', word)
    preparedWord = re.sub(r"/^a$/g", '', preparedWord)
    preparedWord = re.sub(r"/^koji$/g", '', preparedWord)
    preparedWord = re.sub(r"/^kao$/g", '', preparedWord)
    preparedWord = re.sub(r"/^da$/g", '', preparedWord)
    preparedWord = re.sub(r"/^ili$/g", '', preparedWord)
    preparedWord = re.sub(r"/^li$/g", '', preparedWord)
    preparedWord = re.sub(r"/^pa$/g", '', preparedWord)
    preparedWord = re.sub(r"/^od$/g", '', preparedWord)
    preparedWord = re.sub(r"/^do$/g", '', preparedWord)
    preparedWord = re.sub(r"/^kod$/g", '', preparedWord)
    preparedWord = re.sub(r"/^sa$/g", '', preparedWord)
    preparedWord = re.sub(r"/^i$/g", '', preparedWord)
    preparedWord = re.sub(r"/^iz$/g", '', preparedWord)
    preparedWord = re.sub(r"/^pod$/g", '', preparedWord)
    preparedWord = re.sub(r"/^po$/g", '', preparedWord)
    preparedWord = re.sub(r"/^nad$/g", '', preparedWord)
    preparedWord = re.sub(r"/^za$/g", '', preparedWord)
    preparedWord = re.sub(r"/^će$/g", '', preparedWord)
    preparedWord = re.sub(r"/^ce$/g", '', preparedWord)
    preparedWord = re.sub(r"/^tako$/g", '', preparedWord)
    preparedWord = re.sub(r"/^kako$/g", '', preparedWord)
    preparedWord = re.sub(r"/^na$/g", '', preparedWord)
    preparedWord = re.sub(r"/^ako$/g", '', preparedWord)
    preparedWord = re.sub(r"/^u$/g", '', preparedWord)
    preparedWord = re.sub(r"/^sa$/g", '', preparedWord)
    preparedWord = re.sub(r"/^se$/g", '', preparedWord)

    return re.sub(r"</[&\/\\#,+()$~%.':*?<>{}]/g", '', preparedWord)

