from flask import Blueprint, render_template

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template('home.html')

@views.route('/author')
def author():
    return render_template('author.html')

@views.route('/map')
def map():
    return render_template('map.html')

@views.route('/newsletter')
def newsletter():
    return render_template('newsletter.html')

@views.route('/tabloid')
def tabloid():
    return render_template('tabloid.html')

@views.route('/travelbrochure')
def travelbrochure():
    return render_template('travelbrochure.html')

@views.route('/essay')
def essay():
    return render_template('essay.html')