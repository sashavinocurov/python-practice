from flask import Flask, render_template  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"

@app.route('/')          # The "@" decorator associates this route with the function immediately following
def hello_world():
    return render_template('index.html', phrase="hello", times=5)

@app.route('/play/<num>/<color>')
def play():
    return render_template('play.html')
# @app.route('/dojo')
# def success():
#     return "Dojo"

# @app.route('/say/<name>')
# def say(name):
#     print(name)
#     return "Hello, "+ name +"!"

# @app.route('/repeat/<num>/<text>')
# def repeat(text, num):
#     num= int(num)
#     return (text) * num

# @app.route('/users/<username>/<id>')
# def show_user_profile(username, id):
#     print(username)
#     print(id)
#     return "username: " + username +  ", id: "+ id
if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.
