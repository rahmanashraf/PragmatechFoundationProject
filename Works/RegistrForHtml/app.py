
from flask import Flask, request,render_template


app=Flask(__name__)

@app.route('/',methods=['GET','POST'])
def index():
    return render_template ('registr.html')
@app.route('/registr')    
def registr():
    return 'Rehman salam netersen'

if __name__=='__main__':
    app.run(debug=True)