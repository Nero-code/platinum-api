import firebase_admin
from flask import Flask
from src.Training.routes.training_route import trainingBlueprint
from flask_mail import Mail, Message
from firebase_admin import credentials
from firebase_admin import db
from firebase_admin import auth
import os
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)

app.register_blueprint(trainingBlueprint)

# this line modified for test ssh configuration

# ref = db.reference('users')
# print(ref.get())
#
# user = auth.create_user(
#     email='user@example.com',
#     email_verified=False,
#     phone_number='+15555550100',
#     password='secretPassword',
#     display_name='John Doe',
#     disabled=False)
# print('Successfully created new user: {0}'.format(user.email))
#
# email = "user@example.com"
# user = auth.get_user_by_email(email)
# print('Successfully fetched user data: {0}'.format(user.password))

mail = Mail(app)


@app.route('/', methods=["GET"])
def hello_app():
    return "Platinum Api; version=1.0.0"


@app.route('/send-mail', methods=["GET"])
def send_mail():
    msg = Message('Hello From flask', sender='yazan.ash.doonaas@gmail.com', recipients=['yazan.k.aboshash@gmail.com'])
    msg.body = "This is the email body"
    mail.send(msg)
    return "Sent"


if __name__ == "__main__":
    app.run(debug=True, port=5000)
