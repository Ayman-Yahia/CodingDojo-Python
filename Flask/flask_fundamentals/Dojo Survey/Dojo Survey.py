from datetime import date
today = date.today()
from flask import Flask, render_template, request
app = Flask(__name__)
@app.route('/')
def root_route():
    return render_template("index.html")
@app.route('/result',methods=['POST'])
def results():
    print (request.form)
    fname = request.form['first_name']
    lname = request.form['last_name']
    loc = request.form['location']
    lang = request.form['language']
    comm = request.form['comments']
    return render_template("result.html",fname = fname, lname = lname, location = loc, language = lang, comments = comm,today=today)
if __name__=="__main__":   
    app.run(debug=True) 