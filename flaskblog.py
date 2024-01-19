from flask import Flask, render_template, url_for
from forms import RegistrationForm
app = Flask (__name__)

app.config['SECRET_KEY'] = '3ac3e61718a5a5aac5e1c1999ad8e66c'

posts = [
   {
      "author": "Carlos Luna",
      "title": "Blog Post 1",
      "content": "First post content",
      "date_posted": "December 15, 2023"
   },
   {
      "author": "Roberto Diaz",
      "title": "Blog Post 2",
      "content": "First post content",
      "date_posted": "December 16, 2023"
   }
]

###son las rutas de cada page del web site
@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html", posts=posts)

###son las rutas de cada page del web site
@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/register")
def register():
   form = RegistrationForm()
   return render_template('register.html', title='Register', form=form)

@app.route("/login")
def login():
   form = LoginForm()
   return render_template('login.html', title='Login', form=form)

if __name__ == "__main__":
 app.run(debug=True)