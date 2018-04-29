from seo import getMetaTagsForEntyty
from database import getAllBlogPosts, getBlogHomePagePosts, getAllPosts, getBlogPageSidebar, getSingleBlogPost, getAllCookPosts, getCookPageSidebar, getCookPagePosts, getSingleCookPost, getCategoryPosts
from utils import createPostLink, formatAlertStatusAndMessage

baseBlogUrl = '/fitnes-blog-saveti-za-zene'
baseCookUrl = '/fitnes-kuvar-zdrava-hrana-recepti'

def getDataForRoute(pageType, categoryUrl = '', postUrl = '', status=''):
  if pageType == 'index':
    return getIndexPageData()
  elif pageType == 'services':
    return getServicesPageData()
  elif pageType == 'blog':
    return getBlogHomePageData()
  elif pageType == 'blogCategory':
    return getBlogCatgeoryData(categoryUrl)
  elif pageType == 'blogPost':
    return getBlogPostData(categoryUrl, postUrl)
  elif pageType == 'cook':
    return getCookHomePageData()
  elif pageType == 'cookCategory':
    return getCookCategoryData(categoryUrl)
  elif pageType == 'cookPost':
    return getCookPostData(categoryUrl, postUrl)
  elif pageType == 'contact':
    return getContactPageData(status)
  elif pageType == 'admin':
    return getAdminPageData(status)

def getIndexPageData():
  return{'meta': getMetaTagsForEntyty('home', '')}

def getServicesPageData():
  return {
        'meta': getMetaTagsForEntyty('services', '/personalni-treninzi-za-zene-novi-sad')
    }

def getBlogHomePageData():
  return {
    'blogCategories': getBlogHomePagePosts(),
    'meta': getMetaTagsForEntyty('blog', baseBlogUrl, getAllBlogPosts()),
    "sidebar": getBlogPageSidebar(),
    "helpers": {
        "createPostLink": createPostLink
    }
  }

def getBlogCatgeoryData(categoryUrl):
  blogCategory = getCategoryPosts(baseBlogUrl, categoryUrl)
  if blogCategory is None:
    return blogCategory
  
  return {
    'blogCategories': getBlogHomePagePosts(),
    'blogCategory': blogCategory,
    'meta': getMetaTagsForEntyty('blogCategory', baseBlogUrl + '/' + categoryUrl, blogCategory),
    'sidebar': getBlogPageSidebar(),
    'helpers': {
        'createPostLink': createPostLink
    }
  }

def getBlogPostData(categoryUrl, postUrl):
  blogPost = getSingleBlogPost(categoryUrl, postUrl)
  if blogPost is None:
    return blogPost
  
  return {
    'blogCategories': getBlogHomePagePosts(),
    'meta': getMetaTagsForEntyty(
        'blogPost',
        baseBlogUrl + '/' + categoryUrl + '/' + postUrl,
        None,
        blogPost
    ),
    'blogPost': blogPost,
    'sidebar': getBlogPageSidebar(),
    'helpers': {
        'createPostLink': createPostLink
    }
  }

def getCookHomePageData():
  return {
    'meta': getMetaTagsForEntyty('cook' ,baseCookUrl, getAllCookPosts()),
    'cookCategories': getCookPagePosts(),
    'sidebar': getCookPageSidebar(),
    'helpers': {
        'createPostLink': createPostLink
    }
  }
  
def getCookCategoryData(categoryUrl):
  cookCategory = getCategoryPosts(baseCookUrl, categoryUrl)
  if cookCategory is None:
    return cookCategory
  
  return {
    'cookCategories': getCookPagePosts(),
    'cookCategory': cookCategory,
    'meta': getMetaTagsForEntyty('cookCategory', baseCookUrl + '/' + categoryUrl, cookCategory),
    'sidebar': getCookPageSidebar(),
    'helpers': {
        'createPostLink': createPostLink
    }
  }

def getCookPostData(categoryUrl, postUrl):
  cookPost = getSingleCookPost(categoryUrl, postUrl)
  if cookPost is None:
    return cookPost
  
  return {
    'cookCategories': getCookPagePosts(),
    'meta': getMetaTagsForEntyty(
        'cookPost',
        baseBlogUrl + '/' + categoryUrl + '/' + postUrl,
        None,
        cookPost
    ),
    'cookPost': cookPost,
    'sidebar': getCookPageSidebar(),
    'helpers': {
        'createPostLink': createPostLink,
    }
  }

def getContactPageData(status):
 return {
    'meta': getMetaTagsForEntyty('contact', '/kontakt'),
    'status': formatAlertStatusAndMessage(status)
  }


def getAdminPageData(status=''):
  return {
    'meta': getMetaTagsForEntyty('admin', '/admin'),
    'status': formatAlertStatusAndMessage(status)
  }
    