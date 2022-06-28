from flask import Blueprint, render_template

main = Blueprint('main',__name__,template_folder='main_templates')

@main.route('/')
def home():
    return render_template('index.html')