from flask import Flask, render_template, redirect, url_for, request, session, flash

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

app.secret_key = 'your_secret_key'  # Required for session management and flashing messages

# Sample user data
users = [
    {'id': 1, 'username': 'Mercy', 'password': 'password'},
    {'id': 2, 'username': 'Mark', 'password': 'password'},
    {'id': 3, 'username': 'Admin', 'password': 'admin'}
]

headings = ("NAMES", "COUNTRY", "Ranking")
schooldata = (
    ("KTU", "Ghana", "High"),
    ("MIT", "USA", "High"),
    ("TUG", "Germany","High"),
    ("Cambridge", "USA","High")
)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        user = next((x for x in users if x['username'] == username), None)
        
        if user and user['password'] == password:
            session['user_id'] = user['id']
            return redirect(url_for('profile'))
        
        flash('Invalid username or password. Please try again.')
        return redirect(url_for('login'))

    return render_template('login.html')

@app.route('/profile', methods=['GET', 'POST'])
def profile():
    if 'user_id' in session:
        user_id = session['user_id']
        user = next((x for x in users if x['id'] == user_id), None)
        if user:
            if request.method == 'POST':
                # Process form data
                excountry = request.form.get('excountry')
                exschool = request.form.get('exschoolname')
                gpa = request.form.get('gpa')
                fprogram = request.form.get('fprogram')
                fcountry = request.form.get('fcountry')
                
                # For simplicity, we'll just check if these fields are filled
                if excountry and exschool and gpa and fprogram and fcountry:
                    return render_template('profile.html', username=user['username'], headings=headings, schooldata=schooldata, show_table=True)
            return render_template('profile.html', username=user['username'], show_table=False)
    return redirect(url_for('login'))


if __name__ == '__main__':
    app.run(debug=True)
