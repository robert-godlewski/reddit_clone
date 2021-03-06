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


@app.route('/edit_comment/', methods=['POST'])
def edit_comment():
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "id": request.form['comment_id'],
        "content": request.form['content'],
    }
    comment.Comment.update_comment(data)
    return redirect('/g/groupnamehere/' + request.form['post_id'])


@app.route('/deleteComment/<int:post_id>/<int:id>')
def delete_comment(post_id, id):
    if 'user_id' not in session:
        return redirect('/logout')
    post_id = str(post_id)
    comment.Comment.delete_one_comment({"id": id})
    return redirect('/g/groupnamehere/' + post_id)
