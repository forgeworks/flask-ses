Flask-SES
=========

Flask-SES is an extension that simplifies interacting with AWS Simple Email Service (SES).
 
Installation
------------

Install Flask-SES with `pip` ::

    pip install Flask-SES
    
Example
-------

This is a quick example on how to set-up the application to send an email using Flask-SES ::

    from flask import Flask
    from flask_ses import SESMailer
    
    app = Flask(__name__)
    app.config['AWS_REGION'] = 'eu-west-1'
    app.config['AWS_ACCESS_KEY_ID'] = '<aws_access_key_id>'
    app.config['AWS_SECRET_ACCESS_KEY'] = '<aws_secret_access_key>'
    app.config['SES_SOURCE_EMAIL'] = 'noreply@example.com'
    
    mailer = SESMailer(app)
    
    @app.route('/')
    def index():
        mailer.send("Subject", "Sample Body", ['customer@example.com'])
        return "You should receive an email shortly"
    
    if __name__ == "__main__":
        app.run()
    
Resources
---------

* `pypi <https://pypi.python.org/pypi/Flask-SES>`_


