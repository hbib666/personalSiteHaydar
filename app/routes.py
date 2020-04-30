from flask import render_template
from app import app

@app.route('/')

@app.route('/index')
def index():
    # we pass our variables through the render template call
    # ie a dict called user + a new string
    return render_template('/index.html', title='Home')

@app.route('/about')
def aboutPage():
    return render_template('/about.html', title='About')

@app.route('/illustrate')
def illustrate():
    return render_template('/illustrate.html', title='Illustrations')

@app.route('/lang')
def lang():
    return render_template('/lang.html', title='Mapped Languages')

@app.route('/photoBooth')
def photo():
    return render_template('/photoBooth.html')

@app.route('/projects')
def projects():
    return render_template('/projects.html')

@app.route('/resume')
def resume():
    return render_template('/resume.html')
