from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'my little secret'
import random # import the random module
from datetime import datetime

@app.route('/')
def index():
    print('running the index function')
    if 'activity' not in session:
        session['activity'] = ""
    if 'gold' not in session:
        session['gold'] = 0
    return render_template('index.html')

@app.route('/process_money', methods=['POST'])
def process():
    print('*'*50)
    print(request.form['building'])
    if request.form['building'] == 'farm':
        money = random.randint(10, 20)
        session['gold'] += money  # farm gives between 10 - 20 gold
        session['activity'] += f"Earned {str(money)} gold from {request.form['building']}! ({str(datetime.now())})<br>"
    if request.form['building'] == 'cave':
        money = random.randint(5, 10)
        session['gold'] += money # cave gives between 5 - 10 gold
        session['activity'] += f"Earned {str(money)} gold from {request.form['building']}! ({str(datetime.now())})<br>"
    if request.form['building'] == 'house':
        money = random.randint(2, 5)
        session['gold'] += money # farm gives between 2 - 6 gold
        session['activity'] += f"Earned {str(money)} gold from {request.form['building']}! ({str(datetime.now())})<br>"
    if request.form['building'] == 'casino':
        win_or_lose = random.randint(0, 1)
        print(win_or_lose)
        money = random.randint(0, 50)
        if win_or_lose == 0: # farm gives/takes between 0 - 50 gold
            session['gold'] -= money
            session['activity'] += f"Lost {str(money)} gold from {request.form['building']}! ({str(datetime.now())})<br>"
        else:
            session['gold'] += money 
            session['activity'] += f"Earned {str(money)} gold from {request.form['building']}! ({str(datetime.now())})<br>"
    return redirect('/')

@app.route('/reset')
def reset():
    print('clearing the session')
    session.clear()
    return redirect('/')

app.run(debug=True)