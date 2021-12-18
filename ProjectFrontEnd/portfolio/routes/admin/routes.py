from run import app
from flask import Flask,flash,redirect,url_for,render_template,request



@app.route("/admin/blog", methods=["GET","POST"])
def blog():
    from modules import Blogs
    import os
    from run import db
    from werkzeug.utils import secure_filename
    blogs = Blogs.query.all()
    if request.method == "POST":
        file = request.files['blog_img']
        filename = secure_filename(file.filename)
        file.save(os.path.join('static/uploads/', filename))
        blog_title = request.form["blog_title"]
        blog_content = request.form["blog_content"]
        blg = Blogs(
            blog_title = blog_title,
            blog_content = blog_content,
            blog_img = os.path.join('static/uploads/', filename),
        )
        db.session.add(blg)
        db.session.commit()
        return redirect ("/admin/blog")
    return render_template("admin/blog.html", blogs=blogs)

@app.route("/blogDelete/<int:id>",methods=["GET","POST"])
def blog_delete(id):
    from modules import Blogs
    import os
    from run import db
    blogs = Blogs.query.filter_by(id=id).first()
    filename = blogs.blog_img
    os.unlink(os.path.join(filename))
    db.session.delete(blogs)
    db.session.commit()
    return redirect ("/admin/blog")


@app.route("/blogEdit/<int:id>",methods=["GET","POST"])
def blog_edit(id):
    from modules import Blogs
    from run import db
    newBlogs = Blogs.query.filter_by(id=id).first()
    if request.method=="POST":
        blogs = Blogs.query.filter_by(id=id).first()
        blogs.blog_title = request.form["blog_title"]   
        blogs.blog_content = request.form["blog_content"]
        db.session.commit()
        return redirect("/")
    return render_template ("/admin/update_blog.html",newBlogs=newBlogs)




@app.route("/admin/home", methods=["GET","POST"])
def home():
    from modules import Home
    import os
    from run import db
    from werkzeug.utils import secure_filename
    homes = Home.query.all()
    if request.method == "POST":
        home_content = request.form["home_content"]
        home = Home(
            home_content = home_content,
        )
        db.session.add(home)
        db.session.commit()
        return redirect ("/admin/home")
    return render_template("admin/home.html", homes=homes)

@app.route("/homeDelete/<int:id>",methods=["GET","POST"])
def home_delete(id):
    from modules import Home
    from run import db
    homes = Home.query.filter_by(id=id).first()
    db.session.delete(homes)
    db.session.commit()
    return redirect ("/admin/home")

@app.route("/homeUpdate/<int:id>",methods=["GET","POST"])
def home_edit(id):
    from modules import Home
    from run import db
    newHome = Home.query.filter_by(id=id).first()
    if request.method=="POST":
        homes = Home.query.filter_by(id=id).first()  
        homes.home_coontent = request.form["home_content"]
        db.session.commit()
        return redirect("/")
    return render_template ("/admin/update_home.html",newHome=newHome)


@app.route("/admin/skills", methods=["GET","POST"])
def skills():
    from modules import Skills
    import os
    from run import db
    from werkzeug.utils import secure_filename
    skills = Skills.query.all()
    if request.method == "POST":
        file = request.files['skills_img']
        filename = secure_filename(file.filename)
        file.save(os.path.join('static/uploads/', filename))
        skills_title = request.form["skills_title"]
        sklls = Skills(
            skills_title = skills_title,
            skills_img = os.path.join('static/uploads/', filename),
        )
        db.session.add(sklls)
        db.session.commit()
        return redirect ("/admin/skills")
    return render_template("admin/skills.html", skills=skills)

@app.route("/skillsDelete/<int:id>",methods=["GET","POST"])
def skills_delete(id):
    from modules import Skills
    import os
    from run import db
    skills = Skills.query.filter_by(id=id).first()
    filename = skills.skills_img
    os.unlink(os.path.join(filename))
    db.session.delete(skills)
    db.session.commit()
    return redirect ("/admin/skills")

@app.route("/admin/projects",methods=["GET","POST"])
def project():
    from modules import Projects
    import os
    from run import db
    from werkzeug.utils import secure_filename
    projects = Projects.query.all()
    if request.method=="POST":
        file = request.files['project_img']
        filename = secure_filename(file.filename)   
        file.save(os.path.join('static/uploads/', filename))
        project_url = request.form["project_url"]
        prjct = Projects(
            project_url = project_url,
            project_img = os.path.join('static/uploads/', filename),
        )
        db.session.add(prjct)
        db.session.commit()
        return redirect("/")
    return render_template("admin/project.html", projects=projects)

@app.route("/projectDelete/<int:id>",methods=["GET","POST"])
def project_delete(id):
    from modules import Projects
    import os
    from run import db
    projects = Projects.query.filter_by(id=id).first()
    filename = projects.project_img
    os.unlink(os.path.join(filename))
    db.session.delete(projects)
    db.session.commit()
    return redirect ("/admin/projects")

@app.route("/projectEdit/<int:id>",methods=["GET","POST"])
def project_edit(id):
    from modules import Projects
    from run import db
    newProject = Projects.query.filter_by(id=id).first()
    if request.method=="POST":
        projects = Projects.query.filter_by(id=id).first()
        projects.project_url = request.form["project_url"]
        db.session.commit()
        return redirect("/")
    return render_template ("/admin/update_project.html",newProject=newProject)