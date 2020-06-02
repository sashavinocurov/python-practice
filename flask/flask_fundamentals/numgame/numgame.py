import random

from flask import Flask , render_template, request, redirect, session
app = Flask(__name__) 
app.secret_key = 'lalallalala' 

@app.route('/')
def game():
    if 'randnum' not in session:
        session['randnum'] = random.randint(1,100)
    
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    if int(request.form['guessnum']) < session['randnum']:
        session['answer'] = "Too Low!" 
        print("LOW")
    elif int(request.form['guessnum']) > session['randnum']:
        session['answer'] = "Too High!"
        print("High")
    else: 
        session['answer'] = "You Guess Correct!"
        print("correct")
    return redirect('/')

@app.route('/reset', methods=['POST'])
def reset():
    session.clear()
    return redirect('/')

if __name__=="__main__":      
	app.run(debug=True)   