from  functools import reduce

from utils import prepareWordForKeywords
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
	elif entity == 'blogCategory':
  		return getBlogCategoryPageMetaTags(url, posts)
	elif entity == 'cookCategory':
  		return getCookCategoryPageMetaTags(url, posts)
	elif entity == 'blogPost':
		return getPostPageMetaTags(url, post)
	elif entity == 'cookPost':
		return getPostPageMetaTags(url, post)
	elif entity == 'contact':
		return getContactPageMetaTags(url)
	elif entity == 'admin':
  		return getAdminPageMetaTags(url)
	elif entity == 'gallery':
  		return getGalleryPageMetaTags(url)
  		


def getHomePageMetaTags(url):
	return {
		'title': 'Jelena Stevanovic - Novi Sad - Licni Fitnes Trener Za Zene',
		'description': 'Personalni treninzi za zene u Novom Sadu, lako do savrsene figure, programi za osobe sa povredama ledja i lumbalnog dela kicme, mrsavljenje, zatezanje i pravljenje plana ishrane za brze rezultate',
		'url': baseUrl,
		'image': imageUrl,
		'keywords': 'jelena,stevanovic,individualni,treninzi,novi,sad,kako,je,svaka,osoba,individua,za,sebe,,moramo,razlikovati,osobe,kojima,je,potrebna,dodatna,motivacija,i,konstantna,podrška,u,vezbanju'
	}
def getGalleryPageMetaTags(url):
  	return {
		'title': 'Jelena Stevanovic - Novi Sad - Moja Fitnes Galerija',
		'description': 'Personalni treninzi za zene u Novom Sadu, moja fitnes galerija, pogledajte fotografije sa mojih licnih treninga, i prijavite se se za personalne trening za zene u Novom Sadu',
		'url': baseUrl,
		'image': imageUrl,
		'keywords': 'jelena,stevanovic,individualni,treninzi,novi,sad,kako,je,svaka,osoba,individua,fitnes,sebe,,moramo,razlikovati,osobe,kojima,je,potrebna,dodatna,motivacija,galerija,konstantna,podrška,u,vezbanju'
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
		'title': 'Fitnes Blog Za Zene - Personalni Trener Jelena Stevanovic - Licni Trener Novi Sad',
		'description': 'Najnoviji tesktovi i odgovori na pitanja: kako napredovati u teretani, kako brzo smrsati, dijete za ravan stomak, lako do trbusnjaka, zatezanje zadnjice, kako se resiti celulita.',
		'url': baseUrl + url,
		'image': imageUrl,
		'keywords': generateKewordsForPage(posts)
	}

def getCookPageMetaTags(url, posts):
	return {
		'title': 'Fitnes Kuvar Za Zene - Personalni Trener Jelena Stevanovic',
		'description': 'Najnoviji recepti i saveti kako da budete vitki, imate savrsenu liniju i kako da ishranom dovedete svoje telo do savrsene forme',
		'url': baseUrl + url,
		'image': imageUrl,
		'keywords': generateKewordsForPage(posts)
	}

def getBlogCategoryPageMetaTags(url, category):
  return {
		'title': category['title'],
		'description': category['description'],
		'url': baseUrl + url,
		'image': imageUrl,
		'keywords': generateKewordsForPage(category['posts'])
	}

def getCookCategoryPageMetaTags(url, category):
  return {
		'title': 'Fitness Blog Za Zene - Personalni Trener Jelena Stevanovic - Licni Trener Novi Sad',
		'description': 'Najnoviji tesktovi i odgovori na pitanja: kako napredovati u terertani, kako brzo smrsati, dijete za ravan stomak, lako do trbusnjaka, zatezanje zadnjicem, kako se resiti celulita.',
		'url': baseUrl + url,
		'image': imageUrl,
		'keywords': generateKewordsForPage(category['posts'])
	}

def getPostPageMetaTags(url, post):
	return {
		'title': post['title'],
		'description': post['description'],
		'url': baseUrl + url,
		'image': post['imgUrl'],
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

def addSeoEntitiesForCategory(baseUrl, category, posts):
    if category == 'fitnes-treninzi-saveti-i-vezbe':
        categoryWithSeoEntities = {
            'title': 'Fitnes Blog Za Žene - Fitness Treninzi, Saveti i Vežbe',
            'description': 'Fitness treninzi, saveti i vežbe, odgovori na pitanja: kako napredovati u teretani, kako brzo smršati, treninzi za ravan stomak, kako doći do izvajane zadnjice i savršenih nogu'
        }
    elif category == 'zdravlje-i-zdrave-navike':
         categoryWithSeoEntities = {
            'title': 'Fitnes Blog Za Žene - Zdravlje i Zdrave Navike',
            'description': 'Zdravlje i zdrave navike, saznajte kako da sačuvate vaše zdravlje, koje zdrave navike vam mogu ojacati imunitet, koje su navike najbolje za vaš organizam'
        }
    elif category == 'zdrava-hrana-i-zdrava-ishrana':
         categoryWithSeoEntities = {
            'title': 'Fitnes Blog Za Žene - Zdrava Hrana i Zdrava Ishrana',
            'description': 'Zdrava hrana i zdrava ishrana, saznajte sta je najbolje jesti pre ili posle treninga, koja je najbolja hrana za mršavljenje, kako da dijetom istopite masti'
        }
    elif category == 'najbolji-recepti-za-fitnes-dorucak':
         categoryWithSeoEntities = {
            'title': 'Fitnes Kuvar Za Žene -Najbolji Recepti Za Vaš Fitnes Doručak',
            'description': 'Najbolji recepti za vaš fitnes doručak, kako da brzo i lako napravite zdravi obrok za savršen početak dana'
        }
    elif category == 'najbolji-recepti-za-fitnes-rucak':
        categoryWithSeoEntities = {
            'title': 'Fitnes Kuvar Za Žene -Najbolji Recepti Za Vaš Fitnes Ručak',
            'description': 'Najbolji recepti za vaš fitnes ručak, kako da brzo i lako napravite zdravi obrok, pun proteina i pružite svome telu negu kakvu zaslužuje'
        }
    elif category == 'najbolji-recepti-za-fitnes-veceru':
        categoryWithSeoEntities = {
            'title': 'Fitnes Kuvar Za Žene -Najbolji Recepti Za Vašu Fitnes Večeru',
            'description': 'Najbolji recepti za vašu fitnes večeru, kako da brzo i lako napravite sjajnu i zdravu večeru koja će omogućiti vašem telu odmor koji mu je potreban'
        }

    categoryWithSeoEntities['posts'] = posts
    categoryWithSeoEntities['link'] = baseUrl + '/' + category

    return categoryWithSeoEntities

def getContactPageMetaTags(url):
	return {
		'title': 'Kontakt - Jelena Stevanovic - Licni Fitnes Trener Za Zene',
		'description': 'Jelena Stevanovic - Licni fitnes trener za zene, zakazite svoj trening vec danas. Budite slobodni da me kontaktirate ako imate pitanja u vezi pravilne ishrane ili fitnes treninga',
		'url': baseUrl + url,
		'image': imageUrl,
		'keywords': 'jelena,stevanovic,individualni,treninzi,novi,sad,kontakt,zakazi,trening,personalni,zene'
	}
def getAdminPageMetaTags(url):
  	return {
		'title': 'Amin - Jelena Stevanovic - Licni Fitnes Trener Za Zene',
		'description': 'Admin Zona Aplikacije',
		'url': baseUrl + url,
		'image': imageUrl,
		'keywords': 'jelena,stevanovic,individualni,treninzi,novi,sad,kontakt,zakazi,trening,personalni,zene'
	}