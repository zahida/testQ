from flask import Flask
app = Flask(__name__)
@app.route("/new")
def hello():
    
    print ( "new ")
	return "Hello World!"
if __name__ == "__main__":
	app.run()
