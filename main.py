from flask import Flask, render_template, url_for, redirect, request
import mysql.connector 
from datetime import datetime
from form import register_form
import requests

#connecting to database    
cnx = mysql.connector.connect(user='XXXX', password='XXXX',
                              host='XXXX', port = 'XXXX',
                              database='XXXX', ssl_ca='XXXX')

#initialising 
app = Flask(__name__)
app.config['SECRET_KEY'] = 'XXXXX'


#home page --> just static display page
@app.route('/')
def home():
    return render_template('home.html', title = 'Home')


#register page --> able to input name email & image 
@app.route('/register', methods = ['GET', 'POST'])
def register():
    error = ''
    form = register_form()
    current_time = datetime.now()
    if form.validate_on_submit():
        cursor = cursor()
        #cursor = cnx.cursor()
        image = form.picture.data.read()
        insert_query = "INSERT INTO studentmaster (UserID, Name, UserEmail, DateTimeSubmitted, EnroledStatus, DateTimeDecision, MentorID, Image) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
        args = (form.userid.data,form.name.data,form.email.data,current_time,'2',current_time,'1',image)
        '''
        try:
            cursor.execute(insert_query, args)
            cnx.commit()
        except mysql.connector.errors.IntegrityError: #userid already exists 
            error = 'How many times do you want to register!'
        else:
            return redirect(url_for('download'))
        cursor.close()
        '''
        

    return render_template('register.html',form=form, error=error, title = 'Sign Up')


#download page --> only able to access if one come from register page
@app.route('/Download', methods = ['GET', 'POST'])
def download():
    msg = ''
    referrer = request.referrer #check which URL the user comes from
    if referrer == 'http://127.0.0.1:5000/register': #change url once hosted 
        msg = 'correct'
    return render_template('download.html', title = 'Download', msg = msg)





#debugging only for prototype
if __name__ == "__main__":
    app.run(debug=True)

