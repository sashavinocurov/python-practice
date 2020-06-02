from flask import Flask , render_template, request, redirect, session
app = Flask(__name__) 
app.secret_key = 'lalala' 

@app.route('/')
def counter():
    if 'counter' not in session:
       session['counter'] = 0
    session['counter'] += 1
    # else:
    #     print("key 'counter' does NOT exist")
    return render_template("index.html", counter=session['counter']) 

@app.route('/process', methods=['POST'])
def counterfun():
    return redirect('/')


@app.route('/reset')
def reset():
    session.clear()
    # session['counter'] = 0
    return redirect('/')

@app.route('/add2')
def add2():
    session['counter'] += 1
    return redirect ('/')


if __name__=="__main__":      
	app.run(debug=True)   
