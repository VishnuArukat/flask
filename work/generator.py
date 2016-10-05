from flask import Flask, render_template
import markdown
import os
# for caching the data
from werkzeug import cached_property
import yaml

# WERKZEUG_DEBUG_PIN= 'off'

# CONSTANT
POST_PATH_EXTENSION = '.md'
app = Flask(__name__)

class Post(object):
	def __init__(self,path,root_dir =''):
		# removing the file from the path
		self.rootdir = os.path.splitext(path.strip('/'))[0]
		self.filepath = os.path.join(root_dir,path.strip('/'))
		# self.filepath = path
		# calling the function
		self._initialize_metadata()

	@cached_property
	def html(self):
		# opening a file with 'with' keyword so that it will close after we done with it
		with open(self.filepath,'r') as fin:
			# spliting the file into two parts using the two new line char and only does once and the [1] means the content part
			content = fin.read().split('\n\n',1)[1].strip()
			# content is in html to convert it into markup use the package markdown
		return markdown.markdown(content)

	@property
	def url(self):
		return url_for('post',self.filepath)

# this acts like private and only function inside the class
	def _initialize_metadata(self):
		content = ''
		with open(self.filepath,'r') as fin:
			for line in fin:
				# checking whether the path is blank or not
				if not line.strip():
					break
				content += line
				# here __dict__ is the internal dict and the we update that with the metadata from the file using the yaml
				# yaml.load will convert the all the content to the dict format so that we can use it in the update function
		self.__dict__.update(yaml.load(content))

	# using the flask filters 
@app.template_filter('date')
def format_date(value,format ='%B %d,%Y'):
	return value.strftime(format)

# This is a context processor this will merge the given function to the template context in the jinja template
# @app.context_processor
# def inject_format_date():
# 	return {'format_date' : format_date}

	# Using the jinja filters
# app.jinja_env.filters['date'] = format_date

@app.route('/')

def index():
	posts = [Post('post/hello.md')]
 	return render_template('index.html',posts)

@app.route('/blog/<path:path>/')

def post(path):
	# import ipdb; ipdb.set_trace()
	# specifying the path for the file here post is the directory
	# here the path is in the url
	path = os.path.join('posts', path + POST_PATH_EXTENSION)
	post = Post(path) #creating the object
	# passing the post object as the argument we dont have to pass the content as the post_content= 'Hello world'
	# this post object can be used in the html
	return render_template('post.html',post= post)

app.run(debug =True,port=5000,host='0.0.0.0') 