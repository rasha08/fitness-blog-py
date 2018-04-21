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

def findInArray(callback, array):
    for item in array:
        if callback(item):
            return item

def isPostSelected(post, postSlugFromUrl):
    if post:
        return kebabCase(post['title']) == postSlugFromUrl
    else:
        return None
    
