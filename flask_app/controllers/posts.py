from flask import render_template, redirect, session, request, flash
from flask_app import app
from flask_app.models import comment, group, post, user
#from flask_bcrypt import Bcrypt

#bcrypt = Bcrypt(app)


@app.route('/')
def index():
    all_posts = post.Post.getAllPosts()
    return render_template("index.html", posts=all_posts)
