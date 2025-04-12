from flask import Flask, request, render_template, redirect, url_for, session
import sqlite3
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'super-secret-key'  # Needed for session

# Initialize database
def init_db():
    with sqlite3.connect('feedback.db') as conn:
        conn.execute('''CREATE TABLE IF NOT EXISTS feedback
                      (id INTEGER PRIMARY KEY AUTOINCREMENT,
                       name TEXT,
                       email TEXT,
                       category TEXT,
                       message TEXT,
                       status TEXT,
                       created_at TEXT)''')
init_db()

# Home page with feedback form
@app.route('/')
def index():
    success = request.args.get('success', False)
    return render_template('index.html', success=success)

# Submit feedback
@app.route('/submit', methods=['POST'])
def submit():
    name = request.form.get('name', '')
    email = request.form.get('email', '')
    category = request.form.get('category')
    message = request.form.get('message')
    
    # Basic validation
    if not message or len(message) > 500:
        return "Error: Message required (max 500 chars)", 400
    
    with sqlite3.connect('feedback.db') as conn:
        conn.execute('INSERT INTO feedback (name, email, category, message, status, created_at) VALUES (?, ?, ?, ?, ?, ?)',
                    (name, email, category, message, 'Open', datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
        conn.commit()
    
    return redirect(url_for('index', success=True))

# Login page
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if username == 'admin' and password == 'password123':
            session['logged_in'] = True
            return redirect(url_for('dashboard'))
        else:
            return render_template('login.html', error="Invalid credentials")
    return render_template('login.html')

# Admin dashboard
@app.route('/dashboard')
def dashboard():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    with sqlite3.connect('feedback.db') as conn:
        feedback = conn.execute('SELECT * FROM feedback ORDER BY created_at DESC').fetchall()
    return render_template('dashboard.html', feedback=feedback)

# Update status
@app.route('/update_status/<int:id>/<status>')
def update_status(id, status):
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    with sqlite3.connect('feedback.db') as conn:
        conn.execute('UPDATE feedback SET status = ? WHERE id = ?', (status, id))
        conn.commit()
    return redirect(url_for('dashboard'))

# Logout
@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)