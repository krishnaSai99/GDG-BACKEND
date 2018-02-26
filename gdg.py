from flask import Flask
app =Flask(__name__)
@app.route("/")
def hello():
      return jsonify({
         "message":'krishna',
          'flag':True
})
if __name__=="__main__":
	app.run(debug=True)
