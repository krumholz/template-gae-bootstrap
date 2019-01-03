from flask import Flask, render_template
from flask_sslify import SSLify

app = Flask(__name__)
sslify = SSLify(app, permanent=True)


@app.route("/")
@app.route("/home")
def home():
    return render_template('layout.html')


if __name__ == '__main__':
    app.run(debug=True)
