from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# In-memory data store (for demo purposes)
allUser1 = []
allPass1 = []
allAge = []

# Home Route
@app.route('/')
def home():
    return render_template('login.html')

# Login Route
@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    # Check if username exists
    if username in allUser1:
        index = allUser1.index(username)
        if password == allPass1[index]:
            return render_template('home.html')
        else:
            return "Wrong password!"
    else:
        return "Wrong username!"

# Signup Route
@app.route('/signup')
def signup():
    return render_template('signup.html')

# Create Account Route
@app.route('/create_account', methods=['POST'])
def create_account():
    username = request.form['username']
    password = request.form['password']
    age = int(request.form['age'])

    # Check if username already exists
    if username in allUser1:
        return "Username already exists!"
    elif age < 18:
        return "You must be at least 18 years old to create an account."
    else:
        allUser1.append(username)
        allPass1.append(password)
        allAge.append(age)
        return redirect(url_for('home'))

# Logout Route
@app.route('/logout')
def logout():
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
