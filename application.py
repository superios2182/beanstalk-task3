from flask import Flask

application = Flask(__name__)

@application.route("/")
def index():
    return "Hello from ngt8zi57 Elastic Beanstalk CI-CD verification-2026092013095211242"
