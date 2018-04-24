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
    preparedWord = re.sub(r"/^je$/", '', word)
    preparedWord = re.sub(r"/^a$/", '', preparedWord)
    preparedWord = re.sub(r"/^koji$/", '', preparedWord)
    preparedWord = re.sub(r"/^kao$/", '', preparedWord)
    preparedWord = re.sub(r"/^da$/", '', preparedWord)
    preparedWord = re.sub(r"/^ili$/", '', preparedWord)
    preparedWord = re.sub(r"/^li$/", '', preparedWord)
    preparedWord = re.sub(r"/^pa$/", '', preparedWord)
    preparedWord = re.sub(r"/^od$/", '', preparedWord)
    preparedWord = re.sub(r"/^do$/", '', preparedWord)
    preparedWord = re.sub(r"/^kod$/", '', preparedWord)
    preparedWord = re.sub(r"/^sa$/", '', preparedWord)
    preparedWord = re.sub(r"/^i$/", '', preparedWord)
    preparedWord = re.sub(r"/^iz$/", '', preparedWord)
    preparedWord = re.sub(r"/^pod$/", '', preparedWord)
    preparedWord = re.sub(r"/^po$/", '', preparedWord)
    preparedWord = re.sub(r"/^nad$/", '', preparedWord)
    preparedWord = re.sub(r"/^za$/", '', preparedWord)
    preparedWord = re.sub(r"/^će$/", '', preparedWord)
    preparedWord = re.sub(r"/^ce$/", '', preparedWord)
    preparedWord = re.sub(r"/^tako$/", '', preparedWord)
    preparedWord = re.sub(r"/^kako$/", '', preparedWord)
    preparedWord = re.sub(r"/^na$/", '', preparedWord)
    preparedWord = re.sub(r"/^ako$/", '', preparedWord)
    preparedWord = re.sub(r"/^u$/", '', preparedWord)
    preparedWord = re.sub(r"/^sa$/", '', preparedWord)
    preparedWord = re.sub(r"/^se$/", '', preparedWord)

    return re.sub(r"</[&\/\\#,+()$~%.':*?<>{}]/", '', preparedWord)