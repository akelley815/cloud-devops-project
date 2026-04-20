from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def form():
    return render_template("form.html")

@app.route("/character", methods=["POST"])
def character():
    data = request.form

    return render_template("character.html", data=data)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)