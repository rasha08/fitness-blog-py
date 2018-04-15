from flask import Flask, render_template

from seo import getMetaTagsForEntyty
from database import allBlogPosts, allCookPosts, getAllPosts

app = Flask(__name__)

getAllPosts()

@app.route('/')
def showIndexPage():
	data = {
		'meta': getMetaTagsForEntyty('home', '')
	}

	return render_template('home.html', data = data)

@app.route('/personalni-treninzi-za-zene-novi-sad')
def showServicesPage():
	data = {
		'meta': getMetaTagsForEntyty('services', '/personalni-treninzi-za-zene-novi-sad')
	}

	return render_template('services.html', data = data)

@app.route('/fitnes-blog-saveti-za-zene')
def showBlogPage():
	data = {
		'posts': allBlogPosts,
		'meta': getMetaTagsForEntyty('blog', '/fitnes-blog-saveti-za-zene', allBlogPosts)
	}

	return render_template('blog.html', data = data)

app.run()
