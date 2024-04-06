import os

class Config(object):
	SECRET_KEY = os.environ['TOC_SECRET_KEY']

	DEBUG = True