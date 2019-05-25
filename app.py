from api import API


application = API()

@application.route('/home')
@application.route('/')
def home(request, response):
    if request.method == 'POST' and request.content is not None:
        response.body = request.content + '\n' + 'Here is our homepage!'
        print(response.body)
    else:
        response.body = 'Here is our homepage!'


@application.route('/about')
def about(request, response):
    response.body = 'This is page about us!'
