from flask import Flask, render_template, redirect ,request
app = Flask(__name__)

@app.route('/')
def survey():
    return render_template('index.html')

@app.route('/process', methods=["POST"])
def process():
    yourname= request.form['yourname']
    location= request.form['location']
    language= request.form['language']
    comment= request.form['comment']
    return render_template("formsubmission.html", yourname=yourname, location=location, language=language, comment=comment)

# @app.route('/submitted')
# def submitted():
#     return render_template("formsubmission.html")


if __name__=="__main__":
    app.run(debug=True)