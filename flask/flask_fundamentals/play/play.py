from flask import Flask, render_template
app= Flask(__name__)

@app.route('/play')
def play():
    return render_template('index.html')

@app.route('/play/<val>')
def play1(val):
    val = int(val)
    return render_template('index.html', val = val)

@app.route('/play/<val>/<color>')
def play2(val, color):
    val=int(val)
    return render_template('index.html', val=val, color=color)

if __name__=="__main__":
    app.run(debug=True)
