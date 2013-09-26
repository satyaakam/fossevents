from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash
from pymongo import MongoClient

app = Flask(__name__)
app.config.from_object(__name__)

def get_all_events():
    c = MongoClient()
    return [dict(title=row[0], text=row[1]) for row in c.local.allevents.find()]

@app.route('/')
def default_view():
    return render_template('index.html',entries=get_all_events())

if __name__ == '__main__':
    app.run()

