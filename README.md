											Flask
									-------------------------
									
		
		we call the flask  script as app.py
		set up a virtualenv using the virtualenv packages it is better for the different projects
		app gets all the requests and these are processed and figures out the response (particular function) MVC 
		
		'@'  decorator function which wraps around another function.
		@map.route should be above the function that it direct to
		rendered template use the template rendering (send back html)
			use the """ to hold onto line breaks inside the """ we can write the html
			
		but the fastest and cleanest way is to use the render_template and create a folder named "template" and use the render_template(file name) 
			flask automaticly look for the templates folder to add the template
			flask uses ginja 2 which are used for rendering and in that we use "{{ " for printing the variables and we have to pass the variables to the views
			
		In the python Flask we can use the template inheritance to use the same code as a block use the {%block block_name%} {%endblock%} 
		
		ADDIng the CSS
		
		static files are included in the folder static (css and scripts)
		
		
		Adding the forms
		----------------
			
			pdb means that python debugger and it can be used to get all the requests for example for the form request.form
			
		COOKIES
		------------
		To use the cookies we have to import the json package
		in java script the cookies are seted after the response
		some times we have to fake the response using the make_response package and use it to set the cookie
		
		redirect means it will redirect to the @app.route() where the function name is under
				for example if the function name is index and the call is redirect(url_for(index)) it will check the route for the page
		
		
		dont use the {{}} in the html comments it will cause templatesyntax error
		
		
		
		
		Flash Messages
		---------------------
			To sending messages to the user using the module flash in flask.flash uses  secret key for encrypting the message.
			Important is that flash messages only persist untill the next section that is when we refresh it it will disappear and only appear after the submition of the field
			
			
			
			
			TUTS PLUS ______________   STATIC BLOG
			------------------------------------------

install flask 
 jinja	in the flask enables us to use the template inheritance property	

@property  act as a descriptor object and its like if there is a function called foo then the foo = property(foo)
for easy data fetching use the caching property provided by the werkzeug (it is part of the flask).
in flask we can add dynamic paths in the url using the '<path> ' and also we can use this for type converting like <int:varname>
dump() is the most usable thing in the debugger it returns the local variables


we can use the pdb using the settrace() improved version of pdb is ipdb


Adding post metadta
---------------------

	for this we use the pyyaml package for this 
	all python classes have an internal __dict__ which include all the information on the file
	when adding the metadta  as dict remember to add space or it will result in a value error
	
	
JInja formatter
---------------------
using the context processor which is dictionary and we pass the values to the template.This is will be avaialable for every template and it can be used to pass functions also

But we can also use the jinja filters to do the same thing 

		Regestring the format date function as a jinja filter. using the jinja_env.filter.
		remember that the filters are represented by the '|' like the safe html
		
		Another method is using the @app.template_filter(name of the filter)
		 we can pass the custom format for the date or the filters as using the (and the values)
