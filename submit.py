from flask import Flask, request, redirect
import os
import smtplib
from email.message import EmailMessage

app = Flask(__name__)
app.secret_key = '(aXesDE9d...??)'  # Set a secret key for flash messages

@app.route('/submit', methods=['POST'])
def submit():
    # Get the form data
    name = request.form['name']
    email = request.form['email']
    whatsapp = request.form['number']
    topic = request.form['topic']
    message = request.form['message']

    # Set up the email message
    msg = EmailMessage()
    msg.set_content(f'Name: {name}\nNumber: {whatsapp}\nEmail: {email}\nTopic: {topic}\nMessage: {message}')
    msg['Subject'] = 'Form Submission'
    msg['From'] = os.getenv('MY_EMAIL')
    msg['To'] = os.getenv('MY_EMAIL')

     try:
         # Send the email using Gmail's SMTP server
         with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
             smtp.login(os.getenv('MY_EMAIL'), os.getenv('MY_PASSWORD'))
             smtp.send_message(msg)
             flash('Email sent successfully!', 'success')
     except Exception as e:
         flash(f'Error sending email: {str(e)}', 'danger')

    # Redirect back to the form page
    return redirect('/index.html', code=302)

if __name__ == '__main__':
    app.run()
