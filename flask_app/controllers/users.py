from flask import render_template, redirect, session, request, flash
from flask_app import app
from flask_app.models import comment, group, post, user
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt(app)


@app.route('/login')
def login(): 
    return render_template("login_page.html")


@app.route('/create_user', methods=['POST'])
def create_user():
    #print(f'Request Form: {request.form}')
    if not user.User.validate_user(request.form):
        return redirect('/login')
    data = {
        'user_name': request.form['user_name'],
        'email': request.form['email'],
        'password': bcrypt.generate_password_hash(request.form['password'])
    }
    #print(f'Data: {data}')
    user.User.register_user(data)
    user_info = user.User.user_by_email(data)
    #print('New User info:')
    #print(f'User Name: {user_info.user_name}')
    session['user_id'] = user_info.id
    #print(f'Session data: {session}')
    return redirect('/dashboard')


@app.route('/login_user', methods=['POST'])
def login_user():
    #print(f'Request Form: {request.form}')
    user_in_db = user.User.user_by_email(request.form)
    #print(f'user_in_db: {user_in_db}')
    if user_in_db is False:
        flash("Invalid Email", "login")
        return redirect('/login')
    if not bcrypt.check_password_hash(user_in_db.password, request.form['password']):
        flash("Invalid Password", "login")
        return redirect('/login')
    session['user_id'] = user_in_db.id
    return redirect('/dashboard')


@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect('/logout')
    user_id = session['user_id']
    user_info = user.User.user_by_id({"id": user_id})
    return render_template("dashboard.html", user=user_info)


@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')
