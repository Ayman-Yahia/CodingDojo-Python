from flask import Flask,render_template
app = Flask(__name__)
@app.route("/")
def chekboard1():
    return render_template("index.html", x=8, y=8,color1="red",color2="black")
@app.route("/4")
def chekboard2():
    return render_template("index.html", x=8, y=4,color1="red",color2="black")
@app.route("/<int:x>/<int:y>")
def chekboard(x,y):
    return render_template("index.html", x=x, y=y,color1="red",color2="black")
@app.route("/<int:x>/<int:y>/<color1>/<color2>")
def chek_board(x,y,color1,color2):
    return render_template("index.html", x=x, y=y,color1=color1,color2=color2)
if __name__ == "__main__":
    app.run(debug = True)