from flask import Flask

admin = Flask(__name__)


@admin.route('/admin/')
def hello():
    return 'Hello Admin'
