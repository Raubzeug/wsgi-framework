# wsgi-framework
This is a very simple wsgi framework. It requires nothing additional modules.<br>
To run it wsgi server should be installed to your system and uwsgi module working.<br>

Use command "uwsgi --http :<port> --wsgi-file app.py" in your command line to run
server on localhost.<br><br>
<i>Note:</i> this module has <b>NO</b> WSGI server adapters.

<b>Usage example:</b>
To create page you should firstly create an instance of API class (<i>>>> app = API()</i>).<br>
Then create function with arguments <i>(request, response)</i> (these arguments must be used
 strictly otherwise your app will not work) that returns text you want to see in your page.
 To make a route use decorator @app.route('/source_address').
 You may see full example in app.py file.
