from flask import Flask,request

app=Flask(__name__)

@app.route('/', methods=['GET','POST'])
def index():
    if request.method=='POST':
        _ad=request.form ['ad']
        _parol=request.form['parol']
        if _ad=="admin" and _parol=="admin":
            return about()        
    return  f"""
        <form action="/" method="POST">
        <input type="text" name="ad" id="">
        <input type="password" name="parol" id="">
        <input type="submit" name="" id=""> """

@app.route('/about')
def about():
    return f""" <h3 style="color:red;font-size: 50px;text-align: center;font-family: sans-serif;">Səhifəmizə xoş gəlmisiniz</h3>
    """

if __name__=='__main__':
    app.run(debug=True)
