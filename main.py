from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/header')
def header():
    return render_template('header.html')

@app.route('/form')
def form():
    return render_template('form.html')

@app.route('/submitted', methods=['POST'])
def submitted_form():
    name = request.form['name']
    email = request.form['email']
    date = request.form['date']
    time_earliest = request.form['time_earliest']
    time_latest = request.form['time_latest']
    comments = request.form['comments']

    return render_template(
        'submitted_form.html',
        name=name,
        email=email,
        date=date,
        time_earliest=time_earliest,
        time_latest=time_latest,
        comments=comments)