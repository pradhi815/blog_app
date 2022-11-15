from flask import Flask,render_template , url_for ,flash
from forms import RegisterForm, LoginForm


app = Flask(__name__)

app.config['SECRET_KEY'] = 'def2618d56f97817dc2eb139b2d63f0c'

posts = [{
    "author":"Pradeep Raj",
    "title": "Blog Post 1",
    "content" : "1st post content",
    "date_created" : "Nov 2, 2019"
                               
},{
    "author":"Ibrahim",
    "title": "Blog Post 2",
    "content" : "2nd post content",
    "date_created" : "Nov 2, 2020"
                               
},{
    "author":"Mari",
    "title": "Blog Post 3",
    "content" : "3rd post content",
    "date_created" : "Sep 9, 2021"
                               
}]


@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html", posts = posts)
    
@app.route("/about")
def about():
    return render_template("about.html" , title ="About Page")

@app.route("/register", methods =["GET","POST"] )
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        flash(f"Account has been created for {form.username.data}","success")

    return render_template("register.html" , title ="Register",form= form)

@app.route("/login")
def login():
    form = LoginForm()

    return render_template("login.html" , title ="Login",form= form)

if __name__ == '__main__':

    app.run(debug=True)

    