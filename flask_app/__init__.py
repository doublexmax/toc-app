from flask import Flask

def create_app():
	app = Flask(__name__)

	app.config.from_object('flask_app.settings.Config')

	from flask_app.user import user_view
	app.register_blueprint(user_view, url_prefix='/')

	return app