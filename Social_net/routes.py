from Social_net import app

from Social_net.filter import clean_date # We use it in the jinja.html file
from Social_net.data import users
from flask import render_template, request, redirect

from datetime import datetime

@app.route('/')
def index():
    return render_template('public/index.html')


@app.route('/about')
def about():
    return render_template('public/about.html')


@app.route('/jinja')
def jinja():
    name = 'Fabricio'
    age = 36
    teams = ['Nacional', 'Independiente', 'Inter', 'Atletico Madrid', 'Arsenal']
    colors = ('Green', 'Blue')
    countries = {
        'Uruguay':'Montevideo',
        'Argentina':'Buenos Aires',
        'Brasil':'Brasilia',
        'Colombia':'Bogota',
        'Chile':'Santiago'
    }

    great = True

    def repeat(x,qty):
        return x * qty

    class GitRemote:
        def __init__(self, name, description, url):
            self.name = name
            self.description = description
            self.url = url

        def pull(self):
            return f'Pullin repo {self.name}'

        def clone(self):
            return f'Cloning into {self.url}'
    
    my_remote = GitRemote(
        name='Flask Jinja', 
        description='Template design tutorial', 
        url='www.example.com')

    date = datetime.utcnow()

    my_html = '<h5> MY HTML LINES </h5>'

    suspicious = '<script>alert("You have been hacked")</script>'

    return render_template('public/jinja.html', name=name, age=age, teams=teams, colors=colors, 
    countries=countries, great=great, repeat=repeat, GitRemote=GitRemote, my_remote=my_remote, date=date,
    my_html = my_html, suspicious=suspicious)


@app.route('/sign_up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        req = request.form
        username = req['username']
        email = req.get('email')
        password = request.form['password']

        print(username, email, password)

        return redirect(request.url)
    return render_template('public/sign_up.html')


@app.route('/profile/<username>')
def profile(username):
    user = None
    if username in users:
        user = users[username]

    return render_template('public/profile.html', username=username, user=user)


@app.route('/multiple/<foo>/<bar>/<baz>')
def multiple(foo, bar, baz):
    return f'foo is {foo}, bar is {bar}, and baz is {baz}'