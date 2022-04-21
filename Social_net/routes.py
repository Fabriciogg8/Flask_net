from Social_net import app

from Social_net.filter import clean_date # We use it in the jinja.html file
from Social_net.data import users
from flask import jsonify, make_response, render_template, request, redirect, url_for, session, abort
from flask import send_from_directory, abort # Downloading img
from flask import flash # For messages

from datetime import datetime
import os
from werkzeug.utils import secure_filename
from PIL import Image #I use the Corey Schafer video 7 to resize the image


@app.route('/')
def index():
    # This print where to probe the config file
    # print(app.config)
    # print(app.congi['ENV'])
    
    # To see the 500 error
    # abort(500)
    
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


# @app.route('/sign_up', methods=['GET', 'POST'])
# def sign_up():
#     if request.method == 'POST':
#         req = request.form
#         username = req['username']
#         email = req.get('email')
#         password = request.form['password']

#         print(username, email, password)

#         return redirect(request.url)
#     return render_template('public/sign_up.html')


# @app.route('/profile/<username>')
# def profile(username):
#     user = None
#     if username in users:
#         user = users[username]

#     return render_template('public/profile.html', username=username, user=user)


@app.route('/multiple/<foo>/<bar>/<baz>')
def multiple(foo, bar, baz):
    return f'foo is {foo}, bar is {bar}, and baz is {baz}'


@app.route('/json', methods=['POST'])
def json():
    if request.is_json :
        req = request.get_json()

        response = {
            "message" : "JSON received",
            "name" : req.get("name")
        }

        res = make_response(jsonify(response), 200)

        return res
    else:
        res = make_response(jsonify({'message':"No JSON received"}), 400)
        return res


@app.route('/guestbook')
def guestbook():
    return render_template('public/guestbook.html')


@app.route('/guestbook/create_entry', methods=['POST'])
def create_entry():
    req = request.get_json()

    print(req)

    res = make_response(jsonify({'message': 'JSON received'}), 200)
    return res


# Example route to search: http://127.0.0.1:5000/query?bar=bar&baz=baz
@app.route('/query')
def query():
    # args = request.args
    # We can do:
    # for k, v in args.items():
    #     print(f'{k} : {v}')
    
    #Another:
    # if "foo" in args:
    #     foo = args.get("foo")
    
    #     print(foo)
    
    # return 'Query recieved' , 200 
    
    #Another:
    # if request.args:
    #     args = request.args
        
    #     serialized = ' ; '.join(f"{k} : {v}" for k, v in args.items())
        
    #     return f"Query : {serialized}", 200
    
    # else:
    #     return "No query received", 200
    
    #Another:
    req = request.query_string
    
    print(req)
    
    return 'Query recieved' , 200 


app.config['IMAGE_UPLOADS'] = '/Fabricio/Programacion/Platzi/A-Desarrollo_backend_con_Python_y_Django/12-Flask/3_App/Social_net/static/img/uploads'
app.config['ALLOWED_IMAGE_EXTENSIONS'] = ["PNG", "JPG", "JPEG", "GIF"]

def allowed_image(filename):
    ''' Function that takes the filname and return True if the extension 
    is one of the allowed extensions in the app.config'''
    if not "." in filename:
        return False
    
    ext = filename.rsplit(".",1)[1]
    if ext.upper() in app.config["ALLOWED_IMAGE_EXTENSIONS"]:
        return True
    else:
        return False    


@app.route('/upload_image', methods=['GET', 'POST'])
def upload_img():
    if request.method == "POST":
        if request.files:
                        
            image = request.files['image']
            
            if image.filename == "":
                print("Image must have a filename")
                return redirect(request.url)
            
            if not allowed_image(image.filename):
                print("That image extension is not allowed")
                return redirect(request.url)
            else:
                filename = secure_filename(image.filename)
                
                output_size = (120,120) 
                resize_image = Image.open(image)
                resize_image.thumbnail(output_size)
                
                resize_image.save(os.path.join(app.config["IMAGE_UPLOADS"], filename))
            
            print('Image saved')
            
            return redirect(request.url)
            
    
    return render_template("public/upload_image.html")


# DOWNLOADING FILES

app.config['CLIENT_IMAGES'] = 'D:/Fabricio/Programacion/Platzi/A-Desarrollo_backend_PYTHON_y_Django/12-Flask/3_App/Social_net/static/client/img'
app.config['CLIENT_CSV'] = 'D:/Fabricio/Programacion/Platzi/A-Desarrollo_backend_PYTHON_y_Django/12-Flask/3_App/Social_net/static/client/csv'
app.config['CLIENT_REPORTS'] = 'D:/Fabricio/Programacion/Platzi/A-Desarrollo_backend_PYTHON_y_Django/12-Flask/3_App/Social_net/static/client/reports'


@app.route('/get_image/<image_name>')
def get_image(image_name):
    try:
        return send_from_directory(app.config['CLIENT_IMAGES'], path=image_name, as_attachment=True) 
    except FileNotFoundError:
        abort(404)
        

@app.route('/get_csv/<filename>')
def get_csv(filename):
    try:
        return send_from_directory(app.config['CLIENT_CSV'], path=filename, as_attachment=False) 
    except FileNotFoundError:
        abort(404)
        

@app.route('/get_report/<path:path>')
def get_report(path):
    try:
        return send_from_directory(app.config['CLIENT_REPORTS'], path=path, as_attachment=True) 
    except FileNotFoundError:
        abort(404)
        

# COOKIES

@app.route('/cookies')
def cookies():
    res = make_response('Cookies', 200)
    res.set_cookie(
        'flavor', 
        value='chocolate_chip',
        max_age=10,
        expires=None,
        path=request.path,
        domain=None,
        secure=False,
        httponly=False,
        samesite=None
        )
    res.set_cookie('cuadro', 'Nacional')
    res.set_cookie('país', 'Uruguay')
    
    cookies = request.cookies
    cuadro = cookies.get('cuadro')
    # cuadro = cookies['cuadro'] we don't use it in this form because the cookie can be deleted 
    # and in that case we will get an error
    print(cuadro)
    
    return res


# SESSION 

app.config['SECRET_KEY'] = 'sUpEr_sEvErE_SeCrEt_KeY'


users = {
    'fabricio':{
        'username':'fabricio',
        'email':'fgonzalezguasque@gmail.com',
        'password': 'example123',
        'bio':'Junior programmer, with high dreams'
        },
    'drago':{
        'username':'drago',
        'email':'drago@gmail.com',
        'password':'drago_blonde',
        'bio': 'A blonde little guy, who do not appears in Harry Potter'
        },
}


@app.route('/sign_in', methods=['GET','POST'])
def sign_in():
    if request.method == 'POST':
        req = request.form
        username = req.get("username")
        password = req.get("password")
        
        if not username in users:
            print("username not found")
            return redirect(request.url)
        else:
            user = users[username]
            
        if not password == user['password']:
            print('Password incorrect')
            return redirect(request.url)
        else:
            session['USERNAME'] = user['username']
            print('User added to session')
            return redirect(url_for('profile'))
            
    return render_template("public/sign_in.html")


@app.route('/profile')
def profile():
    
    if session['USERNAME'] is not None: 
        username = session['USERNAME']
        user = users[username]
        return render_template('public/profile.html', username=username, user=user)
    else:
        print('Username not found in session')
        return redirect(url_for('sign_in'))
    

@app.route('/sign_out')
def logout():
    
    session.pop['USERNAME', None]
    return redirect(url_for('sign_in'))

# MESSAGE FLASHING

@app.route('/sign_up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        # Three ways of doing the same
        req = request.form
        username = req['username']
        email = req.get('email')
        password = request.form['password']

        if not len(password) >= 10:
            flash('You have to enter at least 10 character password', 'danger') 
            return redirect(request.url)
        
        flash('Account created successfully', 'success')
        return redirect(request.url)
    return render_template('public/sign_up.html')