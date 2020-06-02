from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/show', methods=['POST'])
def create_user():
    print("Got Post Info")
    print(request.form)
    print(f"username submitted: {request.form['username']}")
    print(f"email sumbitted: {request.form ['email']}")
    return redirect("show.html", name=request.form["username"], email=request.form["email"])

if __name__ == "__main__":
    app.run(debug=True)