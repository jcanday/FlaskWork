from flask import Blueprint, render_template, request, redirect, url_for, flash
from car_collection.models import Person, db, check_password_hash
from car_collection.form  import UserLoginForm

 
from flask_login import login_user, logout_user, current_user, login_required
auth = Blueprint('auth',__name__,template_folder='auth_templates')

@auth.route('/signin', methods = ['GET','POST'])
def signin():
    form = UserLoginForm()
    try:
        if request.method == "POST" and form.validate_on_submit():
            email = form.email.data
            password = form.password.data
            print(email, password)
            
            logged_user = Person.query.filter(Person.email == email).first()
            if logged_user and check_password_hash(logged_user.password, password):
                login_user(logged_user)
                flash('You were successfully login in via Email/Password', 'auth-success')
                return redirect(url_for('main_site.home '))
            else:
                flash('Your Email/Password is incorrect', 'auth-failed')
                return redirect(url_for('auth.signin'))
            
    except:
        raise Exception('Invalid Form Data: Please check your form.')
    return render_template('signin.html',form=form)

@auth.route('/signup', methods = ['GET','POST'])
def signup():  
    form = UserLoginForm()
    try:
        if request.method == "POST" and form.validate_on_submit():
            email = form.email.data
            password = form.password.data
            favorite_car = form.favorite_car.data
            print(email, password,favorite_car)

            person = Person(email, password = password, favorite_car=favorite_car)

            db.session.add(person)
            db.session.commit()

            flash(f"You have succesfully created a user account {email}", 'user-created')

            return redirect(url_for('auth.signin'))
    except:
        raise Exception('Invalid Form Data: Please Check Your Form')   
    return render_template('signup.html',form=form)