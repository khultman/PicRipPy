#!/usr/bin/env python


# from pprint import pprint

# with open('uservars.json') as uservars_file:
# 	uservars = json.load(uservars_file)

# pprint(uservars['username'])

class requestWrapper():
	import json
	import pickle
	import requests
	import requests.utils

	def __init__(self, site):
		with open('cookies.txt', 'rw') as f:
			cookies = requests.utils.cookiejar_from_dict(pickle.load(f))
			self.session = requests.session(cookies=cookies)

	def loadCookie(filename):
		with open(filename, 'rb') as f:
			return pickle.load(f)

	def saveCookies(filename):
		with open(filename, 'wb') as f:
			pickle.dump(requests_cookiejar, f)

	def __del__(self):
		self.saveCookies(self.session.self.cookieFileName)

