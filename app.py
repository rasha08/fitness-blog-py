from flask import Flask, render_template, redirect, url_for

from seo import getMetaTagsForEntyty
from database import getAllBlogPosts, getBlogHomePagePosts, getAllPosts, getBlogPageSidebar, getCategoryPosts, getSingleBlogPost, getAllCookPosts, getCookPageSidebar, getCookPagePosts
from utils import createPostLink

app = Flask(__name__)

getAllPosts()

baseBlogUrl = '/fitnes-blog-saveti-za-zene'
baseCookUrl = '/fitnes-kuvar-zdrava-hrana-recepti'

@app.route('/')
def showIndexPage():
    data = {'meta': getMetaTagsForEntyty('home', '')}

    return render_template('home.html', data=data)


@app.route('/personalni-treninzi-za-zene-novi-sad')
def showServicesPage():
    data = {
        'meta': getMetaTagsForEntyty('services', '/personalni-treninzi-za-zene-novi-sad')
    }

    return render_template('services.html', data=data)


@app.route('/fitnes-blog-saveti-za-zene')
def showBlogPage():
    data = {
        'blogCategories': getBlogHomePagePosts(),
        'meta': getMetaTagsForEntyty('blog', baseBlogUrl, getAllBlogPosts()),
        "sidebar": getBlogPageSidebar(),
        "helpers": {
            "createPostLink": createPostLink
        }
    }

    return render_template('blog.html', data=data)

@app.route('/fitnes-blog-saveti-za-zene/<category>')
def showBlogCategoryPage(category):
    blogCategory = getCategoryPosts(baseBlogUrl, category)
    print(blogCategory)
    if blogCategory is None:
        return redirect(url_for('showBlogPage'))

    data = {
        'blogCategories': getBlogHomePagePosts(),
        'blogCategory': blogCategory,
        'meta': getMetaTagsForEntyty('blogCategory', baseBlogUrl + '/' + category, blogCategory),
        'sidebar': getBlogPageSidebar(),
        'helpers': {
            'createPostLink': createPostLink
        }
    }

    return render_template('blog.html', data=data)

@app.route('/fitnes-blog-saveti-za-zene/<category>/<post>')
def showBlogPost(category, post):
    blogPost = getSingleBlogPost(category, post)
    if blogPost is None:
        return redirect(url_for('showBlogCategoryPage', category = category))

    data = {
        'blogCategories': getBlogHomePagePosts(),
        'meta': getMetaTagsForEntyty(
            'blogPost',
            baseBlogUrl + '/' + category + '/' + post,
            None,
            blogPost
        ),
        'blogPost': blogPost,
        'sidebar': getBlogPageSidebar(),
        'helpers': {
            'createPostLink': createPostLink
        }
    }

    return render_template('blog.html', data=data)

@app.route('/fitnes-kuvar-zdrava-hrana-recepti')
def showCookPage():
    data = {
        'meta': getMetaTagsForEntyty('cook' ,baseCookUrl, getAllCookPosts()),
        'cookCategories': getCookPagePosts(),
        'sidebar': getCookPageSidebar(),
        'helpers': {
            'createPostLink': createPostLink
        }
    }

    return render_template('cook.html', data=data)    

@app.route('/fitnes-kuvar-zdrava-hrana-recepti/<category>')
def showCookCategoryPage(category):
    cookCategory = getCategoryPosts(baseCookUrl, category)
    if cookCategory is None:
        return redirect(url_for('showCookPage'))

    data = {
        'cookCategories': getCookPagePosts(),
        'cookCategory': cookCategory,
        'meta': getMetaTagsForEntyty('cookCategory', baseCookUrl + '/' +category, cookCategory),
        'sidebar': getCookPageSidebar(),
        'helpers': {
            'createPostLink': createPostLink
        }
    }

    return render_template('cook.html', data=data)


app.run()
