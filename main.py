from flask import Flask, render_template
from flask_talisman import Talisman

app = Flask(__name__)
talisman = Talisman(
    app,
    content_security_policy={
        'default-src': '\'self\'',
        'img-src': [
            '\'self\'',
            '*.google-analytics.com',
            '*.doubleclick.net',
            '*.google.com'
        ],
        'script-src': [
            '\'self\'',
            '*.googletagmanager.com'
        ],
        'style-src': [
            '\'self\'',
            '*.googleapis.com'
        ],
        'font-src': [
            '\'self\'',
            '*.googleapis.com',
            '*.gstatic.com'
        ]
    },
    content_security_policy_nonce_in=['script-src']
)

@app.route("/")
@app.route("/home")
def home():
    return render_template('layout.html')


if __name__ == '__main__':
    app.run()
