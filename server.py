from flask import Flask, render_template, redirect
from flask import request
import csv

app = Flask(__name__)


@app.route("/")
def home_page():
	return render_template('index.html')

@app.route("/<string:page_name>")
def page_name(page_name):
	return render_template(page_name)

def write_to_file(data):
	database = open('database.txt', mode='a')
	email = data["email"]
	subject = data["subject"]
	message = data["message"]
	file = database.write(f'\n{email},{subject},{message}')


def write_to_csv(data):
	database2 = open('database.csv', newline='', mode='a')
	email = data["email"]
	subject = data["subject"]
	message = data["message"]
	fieldnames = ['email', 'subject', 'message']
	csv_writer = csv.writer(database2, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
	csv_writer.writerow([email, subject, message])

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
	if request.method == 'POST':
		data = request.form.to_dict()
		write_to_csv(data)
		return redirect('/thankyou.html')
	else:
		return 'something went wrong'

        #if valid_login(request.form['username'],
         #              request.form['password']):
          #  return log_the_user_in(request.form['username'])
        #else:
            #error = 'Invalid username/password'
    # the code below is executed if the request method
    # was GET or the credentials were invalid
   # return render_template('login.html', error=error)
