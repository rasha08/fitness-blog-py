from flask import Flask, render_template, redirect, url_for, request, session

from database import getAllPosts
from prepare_response import getDataForRoute
from mail_sender import sendMessageFromContactPage, applyForTreninings
from admin import loginAdmin

app = Flask(__name__)

getAllPosts()

@app.route('/')
def showIndexPage():
    return render_template('home.html', data = getDataForRoute('index'))

@app.route('/personalni-treninzi-za-zene-novi-sad', methods=['GET', 'POST'])
def showServicesPage():
    if request.method == 'POST':
        applyForTreninings(request.form)

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
        status = sendMessageFromContactPage(request.form)
        return render_template('contact.html', data = getDataForRoute('contact', None, None, status))

    return render_template('contact.html', data = getDataForRoute('contact'))

@app.route('/admin', methods=['GET', 'POST'])
def showAdminIndexPage():
    if request.method == 'POST':
        status = loginAdmin(request.form)
        if status == 'success':
            session['admin'] = True
            return redirect(url_for('showAdminMainPage'))

        return render_template('admin.html', data = getDataForRoute('admin', None, None, status))

    if 'admin' in session:
        return redirect(url_for('showAdminMainPage'))

    return render_template('admin.html', data = getDataForRoute('admin', None, None))

@app.route('/admin/main')
def showAdminMainPage():
    if not 'admin' in session:
        return redirect(url_for('showAdminIndexPage'))
    
    data = getDataForRoute('admin', None, None)
    data['page'] = 'main';

    return render_template('admin.html', data = data)

@app.route('/admin/main/<section>')
def showAdminSectionPage(section):
    if not 'admin' in session:
        return redirect(url_for('showAdminIndexPage'))
    
    data = getDataForRoute('admin', None, None)
    data['page'] = 'section'
    data['section'] = section

    return render_template('admin.html', data = data)

@app.route('/<path:path>')
def catch_all(path):
    return redirect(url_for('showIndexPage'))

if __name__ == "__main__":
    app.secret_key = '8725cde364e49a09787978a377808c65'
    app.config['SESSION_TYPE'] = 'filesystem'

    app.debug = True
    app.run()
