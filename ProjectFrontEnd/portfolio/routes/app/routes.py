from run import app
from flask import Flask,redirect,url_for,render_template,request
@app.route("/")
def portfolio():
    from modules import Blogs
    from modules import Home
    from modules import Skills
    homes=Home.query.all()
    blogs = Blogs.query.all()
    skills = Skills.query.all()
    return render_template("app/index.html", blogs=blogs,homes=homes,skills=skills)