from api import API

app = API()

@app.route('/home')
def home(request, response):
    response.body = 'Here is our homepage!'

@app.route('/about')
def about(request, response):
    response.body = 'This is page about us!'

@app.post('/form')
def form(request, response):
    response.body = """"
    <form action="/account/create" method="POST">
    <label for="firstName">First namelabel>
    <input id="firstName" name="firstName" type="text" />
    
    <label for="lastName">Last namelabel>
    <input id="lastName" name="lastName" type="text" />
    
    <input type="submit" value="Sign up!"/>
    form>
    """
