from flask import Flask,request,render_template
from werkzeug.utils import redirect

app=Flask(__name__)


@app.route('/')
def jinjak():
    return render_template("index.html")


@app.route('/game', methods=['get','post'])
def hellow():
    if request.method=='post':
        data1=request.form['ad']
        data2=request.form['soyad']
    return render_template("game.html",data1=data1,data2=data2)


# @app.route("/gamestart")
# def HelloUser():
#     return render_template("gamestart.html",)


if __name__=='__main__':
    app.run(debug=True)