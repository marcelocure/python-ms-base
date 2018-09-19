#!flask/bin/python
from flask import Flask

app = Flask(__name__)


with app.app_context():
    import routes
    app.run(debug=True)