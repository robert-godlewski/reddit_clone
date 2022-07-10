from pymysql import NULL
from flask import render_template, redirect, session, request, flash
from flask_app import app
from flask_app.models import comment, group, post, user
# from flask_bcrypt import Bcrypt

# bcrypt = Bcrypt(app)


# for the api to work we need to review https://developers.google.com/youtube/iframe_api_reference
@app.route('/')
def index():
    all_posts = post.Post.get_all_posts()
    # print('All of the posts in route:')
    # print(all_posts)
    return render_template("index.html", posts=all_posts)


@app.route('/create_post', methods=['POST'])
def create_post():
    content = request.form['content']
    if 'user_id' not in session:
        return redirect('/logout')
    if not post.Post.validate_post(request.form):
        return redirect('/dashboard')
    if(request.form['isVideo'] == "1"):
        content = request.form['content'].split('v=')[1]
        content = content.split('&')[0]
    data = {
        "user_id": session['user_id'],
        "title": request.form['title'],
        "content": content,
        "isVideo": request.form['isVideo']
    }
    post.Post.save_post(data)
    return redirect('/dashboard')


@app.route('/edit_post/<int:id>')
def edit_post(id):
    if 'user_id' not in session:
        return redirect('/logout')
    post_info = post.Post.show_one_post({"id": id})
    print(f'post_info: {post_info}')
    return render_template("edit_post.html", post=post_info)


@app.route('/g/groupnamehere/<int:id>')
def focus_post(id):
    all_posts = post.Post.focus_post({"id": id})
    list = []
    for all in all_posts:
        list.append(all)
    if 'user_id' not in session:
        return render_template("focus_post.html", all_posts=list)
    user_id = session['user_id']
    return render_template("focus_post.html", all_posts=list, user_id=user_id)


@ app.route('/update_post', methods=['POST'])
def update_post():
    content = request.form['content']
    if 'user_id' not in session:
        return redirect('/logout')
    if not post.Post.validate_post(request.form):
        return redirect(f"/edit_post/{request.form['id']}")
    if(request.form['isVideo'] == "1"):
        content = request.form['content'].split('v=')[1]
        content = content.split('&')[0]
    data = {
        "id": request.form['id'],
        "title": request.form['title'],
        "content": content
    }
    post.Post.update_post(data)
    return redirect('/dashboard')


@app.route('/destroy_post/<int:id>')
def destroy_post(id):
    if 'user_id' not in session:
        return redirect('/logout')
    comment.Comment.delete_posts_comments({"post_id": id})
    post.Post.delete_post({"id": id})
    return redirect('/dashboard')
