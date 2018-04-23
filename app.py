from flask import Flask, render_template, redirect, url_for, request

from database import getAllPosts
from prepare_response import getDataForRoute
from mail_sender import sendMessageFromContactPage

app = Flask(__name__)

getAllPosts()

@app.route('/')
def showIndexPage():
    return render_template('home.html', data = getDataForRoute('index'))

@app.route('/personalni-treninzi-za-zene-novi-sad')
def showServicesPage():
    return render_template('services.html', data = getDataForRoute('services'))

@app.route('/fitnes-blog-saveti-za-zene')
def showBlogPage():
    return render_template('blog.html', data = getDataForRoute('blog'))

@app.route('/fitnes-blog-saveti-za-zene/<category>')
def showBlogCategoryPage(category):
    data = getDataForRoute('blogCategory', category)
    if data is None:
        return redirect(url_for('showBlogPage'))

    return render_template('blog.html', data = data)

@app.route('/fitnes-blog-saveti-za-zene/<category>/<post>')
def showBlogPost(category, post):
    data = getDataForRoute('blogPost', category, post)
    if data is None:
        return redirect(url_for('showBlogCategoryPage', category = category))

    return render_template('blog.html', data = data)

@app.route('/fitnes-kuvar-zdrava-hrana-recepti')
def showCookPage():
    return render_template('cook.html', data = getDataForRoute('cook'))

@app.route('/fitnes-kuvar-zdrava-hrana-recepti/<category>')
def showCookCategoryPage(category):
    data = getDataForRoute('cookCategory', category)
    if data is None:
        return redirect(url_for('showCookPage')) 

    return render_template('cook.html', data = data)

@app.route('/fitnes-kuvar-zdrava-hrana-recepti/<category>/<post>')
def showCookPostPage(category, post):
    data = getDataForRoute('cookPost', category, post)
    if data is None:
        return redirect(url_for('showCookCategoryPage', category = category))

    return render_template('cook.html', data = data)

@app.route('/kontakt', methods=['GET', 'POST'])
def handleContact():
    if request.method == 'POST':
        sendMessageFromContactPage(request.form)
        return render_template('contact.html', data = getDataForRoute('contact'))

    return render_template('contact.html', data = getDataForRoute('contact'))

@app.route('/<path:path>')
def catch_all(path):
    return redirect(url_for('showIndexPage'))

app.run()
