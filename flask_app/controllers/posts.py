from flask import render_template, redirect, session, request, flash
from flask_app import app
from flask_app.models import comment, group, post, user
#from flask_bcrypt import Bcrypt

#bcrypt = Bcrypt(app)


# for the api to work we need to review https://developers.google.com/youtube/iframe_api_reference
@app.route('/')
def index():
    all_posts = post.Post.get_all_posts()
    return render_template("index.html", posts=all_posts)
