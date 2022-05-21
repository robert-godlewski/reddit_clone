from flask import render_template, redirect, session, request, flash
from flask_app import app
#from flask_app.models import user
#from flask_bcrypt import Bcrypt

#bcrypt = Bcrypt(app)


@app.route('/')
def index():
    # Note to group - Just made a temporary home page layout to test out HTML iframe tag.
    # Will probably need a search all posts here by newest on top in the models for the home page.
    # for the api to work we need to review https://developers.google.com/youtube/iframe_api_reference
    temp_data = {
        "link": "https://www.youtube.com/watch?v=uwyRxK0htpI"
    }
    return render_template("index.html", posts=temp_data)
