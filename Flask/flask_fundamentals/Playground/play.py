from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def hello():
    return "Hello User"
@app.route('/play')
def level1():
    return render_template("index1.html",times=3)	
@app.route('/play/<int:times>')
def level2(times):
    return render_template("index1.html",times=times,color="#9fc5f8")
@app.route('/play/<int:times>/<color>')
def level3(times, color):
    return render_template("index1.html",times=times,color=color)	
if __name__=="__main__":
    app.run(debug=True)
