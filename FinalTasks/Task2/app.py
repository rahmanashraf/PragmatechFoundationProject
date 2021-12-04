from flask import Flask,request,render_template
from werkzeug.utils import redirect

app=Flask(__name__)


@app.route('/',methods=['GET','POST'])
def jinjak():
    if request.method=='POST':
        return redirect("/game")
        
    return render_template("index.html")
    
    


@app.route('/game', methods=['GET','POST'])
def hellow():
    if request.method=='POST':
        data1=request.form['ad']
        data2=request.form['soyad']
        # return redirect('/gamestart')
        return render_template("gamestart.html",data1=data1,data2=data2)
    return render_template("game.html")
    


@app.route("/gamestart")
def HelloUser():
    return render_template("gamestart.html",)


if __name__=='__main__':
    app.run(debug=True)