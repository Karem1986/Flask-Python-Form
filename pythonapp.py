from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def form():
    return '''
        <form method="POST" action="/submit">
            Name: <input type="text" name="name"><br>
            Age: <input type="text" name="age"><br>
            Email: <input type="text" name="email"><br>
            Country: <input type="text" name="country"><br>
            <input type="submit" value="Submit">
        </form>
    '''

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    age = request.form['age']
    email = request.form['email']
    country = request.form['country']
    return f'Thank you, {name}. Your age is {age}. Your email is {email}. Your country is {country}.'

# This code checks if the script is being run directly (as opposed to being imported as a module). 
# If it is, the Flask application is started with debugging enabled.
if __name__ == '__main__':
    app.run(debug=True)
    
# http://localhost:5000 --> to access this application