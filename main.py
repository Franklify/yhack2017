from flask import Flask, render_template, request
from google.appengine.ext import ndb

app = Flask(__name__)

def date_to_int(date):
    [year, month, day] = date.split("-")
    return 10000*int(year) + 100*int(month) + int(day)

def int_to_date(integer):
    day = integer % 100
    integer = integer / 100
    month = integer % 100
    integer = integer / 100
    year = integer
    return year + "-" + month + "-" + day

def time_to_int(time):
    [hour, minute] = time.split(":")
    return 100*int(hour) + int(minute)

def int_to_date(integer):
    hour = integer % 100
    integer = integer / 100
    minute = integer % 100
    return hour + ":" + minute

class Account(ndb.Model):
    username = ndb.StringProperty()
    userid = ndb.IntegerProperty()
    useremail = ndb.StringProperty()
    userschool = ndb.StringProperty()

def create_account(name, id, email, school):
    account = Account(
        username=name, userid=id, useremail=email, userschool=school)
    return account

def get_accounts(accounts_key):
    accounts = accounts_key.get()
    return trips

def save_account(account):
    account_key = accounts.put()
    return account_key

class School(ndb.Model):
    name = ndb.StringProperty()

def create_school(name):
    school = School(name=name)
    return school

def get_schools():
    schools = school_key.get()
    return schools

class Trip(ndb.Model):
    username = ndb.StringProperty()
    date = ndb.IntegerProperty()
    time_earliest = ndb.IntegerProperty()
    time_latest = ndb.IntegerProperty()
    comments = ndb.StringProperty()

def create_trip(name, date, time_earliest, time_latest, comments):
    trip = Trip()
    trip.username = name
    trip.date = date
    trip.time_earliest = time_earliest
    trip.time_latest = time_latest
    trip.comments = comments
    return trip

def get_trips(school_key):
    trips = school_key.get()
    return trips

def save_trip(school):
    trip_key = school.put()
    return trip_key


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/header')
def header():
    return render_template('header.html')

@app.route('/form')
def form():
    return render_template('form.html')

@app.route('/trips')
def trips():
    t = Trip()._query().fetch()
    return render_template('trips.html', trips=t)

@app.route('/submitted', methods=['POST'])
def submitted_form():
    name = request.form['name']
    email = request.form['email']
    date = request.form['date']
    time_earliest = request.form['time_earliest']
    time_latest = request.form['time_latest']
    comments = request.form['comments']

    t = create_trip(str(name), date_to_int(date), time_to_int(time_earliest), time_to_int(time_latest), str(comments))
    t._put()

    return render_template(
        'submitted_form.html',
        name=name,
        email=email,
        date=date,
        time_earliest=time_earliest,
        time_latest=time_latest,
        comments=comments)