from flask import Flask, render_template, redirect, url_for

from seo import getMetaTagsForEntyty
from database import getAllBlogPosts, getBlogHomePagePosts, getAllPosts, getBlogPageSidebar, getBlogCategory, getSingleBlogPost
from utils import createPostLink

app = Flask(__name__)

getAllPosts()

baseBlogUrl = '/fitnes-blog-saveti-za-zene'

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
    blogCatgegory = getBlogCategory(category)
    if len(blogCatgegory) == 0:
        return redirect(url_for('showBlogPage'))

    data = {
        'blogCategories': getBlogHomePagePosts(),
        'blogCategory': blogCatgegory,
        'meta': getMetaTagsForEntyty('blogCategory', baseBlogUrl + '/' +category, blogCatgegory),
        'sidebar': getBlogPageSidebar(),
        'helpers': {
            'createPostLink': createPostLink
        }
    }

    return render_template('blog.html', data=data)

@app.route('/fitnes-blog-saveti-za-zene/<category>/<post>')
def getBlogPost(category, post):
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
    

app.run()
