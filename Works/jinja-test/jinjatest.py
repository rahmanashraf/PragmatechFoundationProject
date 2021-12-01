from flask import Flask,request,render_template

app=Flask(__name__)

@app.route('/')
def jinjak():
    return render_template("index.html")


@app.route('/hello')
def hellow():
    return render_template ('hello.html')


@app.route("/hello/<name>")
def HelloUser(name):
    return render_template("hello.html",username=name)

if __name__=='__main__':
    app.run(debug=True)