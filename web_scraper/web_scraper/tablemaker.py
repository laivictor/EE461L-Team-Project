import json
from json2html import *
from flask import Flask, render_template

with open('countries.json') as f:
	data = json.load(f)



for x in data:

	open new html file - > data[0].html
	header stuff > file 

x = data[0]

table = json2html.convert(json = x)

