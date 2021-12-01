import registr
from flask import Flask,request,render_template

app=Flask(__name__)

@app.route('/', methods=['GET','POST'])
def index():
    if request.method=='POST':
        _ad=request.form ['ad']
        # _parol=request.form['parol']
        if _ad==registr.Goster.Username():
            return about()        
        return  render_template ("index.html",data=registr.Goster.Username())

@app.route('/about')
def about():
    return f""" <h3 style="color:red;font-size: 50px;text-align: center;font-family: sans-serif;">Səhifəmizə xoş gəlmisiniz</h3>
    """

if __name__=='__main__':
    app.run(debug=True)
