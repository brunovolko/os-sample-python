from flask import Flask, jsonify
application = Flask(__name__)

@application.route("/")
def hello():
	return jsonify({
        "saludo": "hola"
    })

@application.route("/chau", methods=['GET'])
def chau():
    return render_template('chau.html', saludo="Hasta la proxima")



if __name__ == "__main__":
    application.run()
