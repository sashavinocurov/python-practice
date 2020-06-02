from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)  
app.secret_key= 'lalalala'

@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/process', methods=['POST'])         
def process():
    session['raspberry']= request.form['raspberry']
    session['apple']= request.form['apple']
    session['strawberry']= request.form['strawberry']
    session['first_name']= request.form['first_name']
    session['last_name']= request.form['last_name']
    session['student_id']= request.form['student_id']
    session['count']= int(session['strawberry'])+int(session['apple'])+int(session['raspberry'])
    return redirect('/checkout')

@app.route('/checkout')
def checkout():
    return render_template("checkout.html", raspberry=session['raspberry'], apple=session['apple'],strawberry=session['strawberry'], first_name=session['first_name'], last_name=session['last_name'], student_id=session['student_id'], count=session['count'])

@app.route('/fruits')         
def fruits():
    return render_template("fruits.html")

if __name__=="__main__":   
    app.run(debug=True)    