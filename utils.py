import re
from  functools import reduce

def filterArrayByKey(array, key, value):
    return reverseArrayOrder(
        list(
            filter(
                lambda member: compare(member, key, value),
                array
            )
        )
    )


def compare(object, key, value):
    return object[key] == value

def kebabCase(name):
    return (
        name.lower()
        .replace('"', '')
        .replace('...', '')
        .replace('.', '')
        .replace('(', '')
        .replace(')', '')
        .replace('!', '')
        .replace('?', '')
        .replace(':', '')
        .replace(';','')
        .replace(',', '')
        .replace('  ', ' ')
        .strip()
        .replace(' ', '-')
    )

def reverseArrayOrder(array):
    return array[::-1]

def createPostLink(data, post, category='', isSidebar = False):
    if 'blogCategory' in data and not isSidebar and not category:
         return data['blogCategory']['link'] + '/' + kebabCase(post['title'])
    elif 'blogCategories' in data:
        return data['blogCategories'][category]['link'] + '/' + kebabCase(post['title'])
    elif 'cookCategory' in data and not isSidebar and not category:
         return data['cookCategory']['link'] + '/' + kebabCase(post['title'])
    elif  'cookCategories' in data:
        return data['cookCategories'][category]['link'] + '/' + kebabCase(post['title'])

def findInArray(callback, array):
    for item in array:
        if callback(item):
            return item

def isPostSelected(post, postSlugFromUrl):
    if post:
        return kebabCase(post['title']) == postSlugFromUrl
    else:
        return None

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