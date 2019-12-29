python_pages=[
	{'title': 'Official Python Tutorial',
	'url':'http://docs.python.org/3/tutorial/',
	'views':100}, 
	{'title':'How to Think like a Computer Scientist',
	'url':'http://www.greenteapress.com/thinkpython/',
	'views':96},
	{'title':'Learn Python in 10 Minutes',
	'url':'http://www.korokithakis.net/tutorials/python/',
	'views':99} ]
		 
django_pages=[
	{'title':'Official Django Tutorial',
	'url':'https://docs.djangoproject.com/en/2.1/intro/tutorial01/',
	'views':90},
	{'title':'Django Rocks',
	'url':'http://www.djangorocks.com/',
	'views':80},
	{'title':'How to Tango with Django',
	'url':'http://www.tangowithdjango.com/',
	'views':98} ]
		 
other_pages=[
	{'title':'Bottle',
	'url':'http://bottlepy.org/docs/dev/',
	'views':60},
	{'title':'Flask',
	'url':'http://flask.pocoo.org',
	'views':97} ]
		 
cats={'Python': {'pages': python_pages,'views':128,'likes':64},
	'Django': {'pages': django_pages,'views':64,'likes':32},
	'Other Frameworks': {'pages': other_pages,'views':32,'likes':16} }
		  
for cat, cat_data in cats.items():
	#c = add_cat(cat,cat_data['views'],cat_data['likes'])#新增了views和likes
	for p in cat_data['pages']:
		print(p['title'],p['views'])
