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
  elif pageType == 'gallery':
    return getGalleryPageData();

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

def getGalleryPageData():
   return {
    'meta': getMetaTagsForEntyty('gallery', '/moja-fitnes-galerija'),
    # temporarily hardcoded until gallery part of admin section is implemented
    'images': [
      'http://res.cloudinary.com/dgq2ohvtq/image/upload/v1498981366/DSC_0051-min_yxbkrp.jpg',
      'http://res.cloudinary.com/dgq2ohvtq/image/upload/v1498981515/DSC_0111-min_iyebey.jpg',
      'http://res.cloudinary.com/dgq2ohvtq/image/upload/v1498981632/DSC_0148-min_miaon5.jpg',
      'http://res.cloudinary.com/dgq2ohvtq/image/upload/v1498981741/DSC_0157-min_vhftn3.jpg',
      'http://res.cloudinary.com/dgq2ohvtq/image/upload/v1498981856/DSC_0187-min_yyjxbl.jpg',
      'http://res.cloudinary.com/dgq2ohvtq/image/upload/v1498981960/DSC_0226a-min_y0erjq.jpg',
      'http://res.cloudinary.com/dgq2ohvtq/image/upload/v1498982072/DSC_0254-min_afoms0.jpg',
      'http://res.cloudinary.com/dgq2ohvtq/image/upload/v1498982175/12809559_445050005703516_8476667965764072254_n_ttiq9w.jpg',
      'http://res.cloudinary.com/dgq2ohvtq/image/upload/v1498982228/10422148_445050009036849_2574643638262623362_n_gzfzio.jpg',
      'http://res.cloudinary.com/dgq2ohvtq/image/upload/v1498982284/12795492_445050035703513_4508566350799193176_n_xhvzz7.jpg',
      'http://res.cloudinary.com/dgq2ohvtq/image/upload/v1498982326/12800205_445050059036844_5734113033230004046_n_1_hakjbz.jpg',
      'http://res.cloudinary.com/dgq2ohvtq/image/upload/v1498982349/12799263_445050095703507_3258923399304042572_n_sxq2ia.jpg'
    ]
  }