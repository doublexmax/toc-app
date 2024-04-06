from flask import Blueprint, render_template

user_view = Blueprint('user', __name__)

@user_view.route('/')
def home(methods=['GET']):
	return render_template('home.html', title = "Home")