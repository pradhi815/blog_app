from flask import Flask,render_template , url_for



app = Flask(__name__)

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

if __name__ == '__main__':

    app.run(debug=True)