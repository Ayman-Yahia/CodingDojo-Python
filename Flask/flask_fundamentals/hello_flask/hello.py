from flask import Flask  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"

@app.route('/success')
def success():
    return "success"  
if __name__=="__main__":
    app.run(debug=True)    
