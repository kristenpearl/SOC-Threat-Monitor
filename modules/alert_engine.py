from flask import Flask

app = Flask(name)

@app.route("/")
def dashboard():

    return """
    <h1>SOC Threat Monitor</h1>

    <h3>Security Operations Center</h3>

    <p>Status: Monitoring Active</p>
    """

if name == "main":
    app.run(debug=True)
