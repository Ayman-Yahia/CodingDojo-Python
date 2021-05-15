from flask import Flask, render_template, redirect, session
app = Flask(__name__)
app.secret_key = 'Secret'

@app.route('/')
def index():
    session['count'] += 1
    return render_template("index.html", count = session['count'])
@app.route('/add')
def add():
    session['count'] += 1
    return redirect("/")

@app.route('/destroy_session')
def reset():
    session['count'] = 0
    return redirect("/")

if __name__=="__main__":
    app.run(debug=True)