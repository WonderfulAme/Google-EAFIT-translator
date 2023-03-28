from flask import Flask, render_template ,request,session,redirect,send_file,send_from_directory
app = Flask(__name__)
LANGUAGES = ["No translate","spanish","english","german","basque","italian","russian"]
class webpage:
	@app.route("/",methods=['POST','GET'])
	def index():
		return render_template("index.html",languages=LANGUAGES)
	@app.route("/configurations.html",methods=['POST','GET'])
	def config():
		if request.method == "POST":
			port=request.form["port"]
			host=request.form["host"]
		return render_template("configurations.html")
if __name__ == "__main__":
	app.run(debug=True,host="127.0.0.1",port=9600)