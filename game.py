from flask import Flask, redirect, render_template, request, session, url_for
import random

app = Flask(__name__)
app.secret_key = 'rsp_secret_key'

choices = ['rock', 'paper', 'scissors']

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return 'Tie 🤝'
    elif (
        (user_choice == 'rock' and computer_choice == 'scissors') or
        (user_choice == 'paper' and computer_choice == 'rock') or   
        (user_choice == 'scissors' and computer_choice == 'paper')      
    ):
        return 'You win 🎉'
    else:
        return 'Computer wins 🤖'
    
@app.route('/', methods=['GET', 'POST'])
def home():
    if "user_score" not in session:
        session['user_score'] = 0
        session['computer_score'] = 0

    user_choice = computer_choice = result = None

    if request.method == 'POST':
        user_choice = request.form['choice']
        computer_choice = random.choice(choices)
        result = determine_winner(user_choice, computer_choice)

        if result == 'You win 🎉':
            session['user_score'] += 1
        elif result == 'Computer wins 🤖':
            session['computer_score'] += 1

    return render_template(
        'home.html',
        user_choice=user_choice,
        computer_choice=computer_choice,
        result=result,
        user_score=session['user_score'],
        computer_score=session['computer_score']
    )

@app.route('/reset')
def reset():
    session['user_score'] = 0
    session['computer_score'] = 0   
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
