from flask import Flask, render_template
app = Flask(__name__)   

@app.route('/')
def checkerboard():
    return render_template("index.html", x=8, y=8)

@app.route('/<x>')
def checkerboard1(x):
    return render_template("index.html", x=int(x), y=8)

@app.route('/<x>/<y>')
def checkerboard2(x,y):
    return render_template("index.html", x=int(x), y=int(y))

@app.route('/<x>/<y>/<color1>/<color2>')
def checkerboard3(x,y,color1, color2):
    return render_template("index.html", x=int(x), y=int(y), color1=color1, color2=color2)

if __name__=="__main__":      
    app.run(debug=True)