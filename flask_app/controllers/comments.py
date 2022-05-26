from pymysql import NULL
from flask import render_template, redirect, session, request, flash
from flask_app import app
from flask_app.models import comment, group, post, user
# from flask_bcrypt import Bcrypt

# bcrypt = Bcrypt(app)


@app.route('/create_comment', methods=['POST'])
def create_comment():
    if 'user_id' not in session:
        return redirect('/logout')
    if not comment.Comment.validate_comment(request.form):
        return redirect('/g/groupnamehere/' + request.form['post_id'])
    data = {
        "user_id": request.form['user_id'],
        "post_id": request.form['post_id'],
        "content": request.form['content']
    }
    comment.Comment.create_comment(data)
    return redirect('/g/groupnamehere/' + request.form['post_id'])
