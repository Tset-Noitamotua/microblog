from flask import Flask

app = Flask(__name__)
app.config.from_object('config')

from my_app import views
