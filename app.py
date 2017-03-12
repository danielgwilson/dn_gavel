"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/

This file creates your application.
"""

import os
import csv
from collections import OrderedDict
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'this_should_be_configured')

app.debug = True

###
# Routing for your application.
###

@app.route('/')
def home():
    """Render website's home page."""

    return 'hihihihi'


@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html')


###
# The functions below should be applicable to all Flask apps.
###

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.route('/<app_id>')
def id_page(app_id):
    fin = open('s_uuid.csv', 'rt')
    reader = csv.reader(fin, delimiter=',', quotechar='"')
    user_table = OrderedDict()
    for row in reader:
        user_table[row[-1]] = row
    app.logger.debug(user_table[app_id])
    user = OrderedDict()
    for index, item in enumerate(user_table[app_id]):
        user[user_table['UUID'][index]] = item

    return render_template('result.html', result = user)

@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=600'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(debug=True)
