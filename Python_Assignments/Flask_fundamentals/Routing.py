from flask import Flask  
app = Flask(__name__) 
@app.route('/<val>')
def err(val):
    if val=='dojo' or val=='say' or val=='repeat' or val =='repeat1' :
        pass
    else:
        return "Sorry! No response. Try again."   
@app.route('/')         
def hello_world():
    return 'Hello World!'
@app.route('/dojo') 
def dojo():
    return 'dojo'
@app.route('/say/<name>')
def say(name):
    return f'Hi {name}'
@app.route('/repeat/<times_repeat>/<string>')
def repstr(times_repeat,string):
    return f'{string} '*int(times_repeat)
@app.route('/repeat1/<int:times_repeat>/<string>')
def repstri(times_repeat,string):
    return f'{string} '*times_repeat
if __name__=="__main__":
    app.run(debug=True)    
