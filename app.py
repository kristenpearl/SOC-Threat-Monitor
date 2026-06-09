from flask import Flask, render_template

app = Flask(name)

@app.route("/")

def dashboard():

    return render_template(
        "dashboard.html"
    )

if name == "main":

    app.run(debug=True)
