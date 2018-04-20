from flask import Flask, render_template

from seo import getMetaTagsForEntyty
from database import getAllBlogPosts, getBlogPostPagePosts, getAllPosts, getBlogPageSidebar
from utils import kebabCase

app = Flask(__name__)

getAllPosts()


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
        'blogCategories': getBlogPostPagePosts(),
        'meta': getMetaTagsForEntyty('blog', '/fitnes-blog-saveti-za-zene', getAllBlogPosts()),
        "sidebar": getBlogPageSidebar(),
        "helpers": {
            "kebabCase": kebabCase
        }
    }

    return render_template('blog.html', data=data)


app.run()
