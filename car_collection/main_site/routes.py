from flask import Blueprint, render_template
from flask_login import login_required

main = Blueprint('main',__name__,template_folder='main_templates')

@main.route('/')
def home():
    return render_template('index.html')

@main.route('/profile')
@login_required
def profile():
    return render_template('prof.html')