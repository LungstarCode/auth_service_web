from flask import Flask, render_template, request, redirect, url_for, flash, session
from firebase_admin import credentials, auth, initialize_app
import firebase_admin
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)

# Initialize Firebase Admin SDK
cred = credentials.Certificate("sentiment-analysis-cc7ce-firebase-adminsdk-fbsvc-59b4f37414.json")
firebase_admin.initialize_app(cred)

@app.route('/')
def index():
    user = session.get('user')
    return render_template('index.html', user=user)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        id_token = request.form.get('id_token')
        try:
            decoded_token = auth.verify_id_token(id_token)
            if not decoded_token.get('email_verified', False) and decoded_token.get('provider_id') != 'phone':
                flash('Please verify your email before logging in.', 'error')
                return redirect(url_for('login'))
            session['user'] = decoded_token
            flash('Login successful!', 'success')
            return redirect(url_for('dashboard'))
        except Exception as e:
            flash(f'Login failed: {str(e)}', 'error')
            return redirect(url_for('login'))
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        id_token = request.form.get('id_token')
        try:
            decoded_token = auth.verify_id_token(id_token)
            session['user'] = decoded_token
            flash('Registration successful! Please check your email to verify your account.', 'success')
            return redirect(url_for('login'))
        except Exception as e:
            flash(f'Registration failed: {str(e)}', 'error')
            return redirect(url_for('register'))
    return render_template('register.html')

@app.route('/reset_password', methods=['GET', 'POST'])
def reset_password():
    if request.method == 'POST':
        email = request.form.get('email')
        try:
            auth.generate_password_reset_link(email)
            flash('Password reset email sent! Check your inbox.', 'success')
            return redirect(url_for('login'))
        except Exception as e:
            flash(f'Error sending reset email: {str(e)}', 'error')
            return redirect(url_for('reset_password'))
    return render_template('reset_password.html')

@app.route('/dashboard')
def dashboard():
    user = session.get('user')
    if not user:
        flash('Please log in to access the dashboard.', 'error')
        return redirect(url_for('login'))
    return render_template('dashboard.html', user=user)

@app.route('/logout')
def logout():
    session.pop('user', None)
    flash('Logged out successfully.', 'success')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)