Flask Firebase Authentication Service
This is a Flask web application integrated with Firebase Authentication, providing a complete user authentication system. It supports email/password, Google, and phone-based login, email verification, password reset, and a user dashboard.
Features

Email/Password Authentication: Register and log in using email and password, with mandatory email verification.
Google Sign-In: Log in using Google accounts via Firebase Authentication.
Phone Authentication: Log in using phone numbers with SMS verification and reCAPTCHA.
Email Verification: Users must verify their email before logging in (except for phone-based logins).
Password Reset: Allows users to reset their password via email.
Dashboard: A protected page displayed after successful login, showing the user's email.
Session Management: Uses Flask sessions to track logged-in users.
Responsive UI: Built with Tailwind CSS for a clean, responsive interface.

Project Structure
your_project/
├── app.py
├── templates/
│   ├── index.html
│   ├── login.html
│   ├── register.html
│   ├── reset_password.html
│   └── dashboard.html
├── static/
├── sentiment-analysis-cc7ce-firebase-adminsdk-fbsvc-59b4f37414.json
└── requirements.txt


app.py: Flask application with routes for index, login, register, password reset, dashboard, and logout.
templates/: HTML templates for the UI, styled with Tailwind CSS.
static/: Directory for static assets (empty in this project, as Tailwind CSS is loaded via CDN).
sentiment-analysis-cc7ce-firebase-adminsdk-fbsvc-59b4f37414.json: Firebase Admin SDK service account key (not included in version control).
requirements.txt: Python dependencies for the project.

Prerequisites

Python 3.8+: Required for Flask and Firebase Admin SDK.
Firebase Project: Set up a Firebase project with Email/Password, Google, and Phone authentication enabled.
Firebase Service Account Key: Download from Firebase Console (Project Settings > Service Accounts).
Node.js: Optional, for testing Firebase JavaScript SDK locally (not required for production).

Setup Instructions

Clone the Repository:
git clone <your-repository-url>
cd your_project


Install Dependencies:
pip install -r requirements.txt

The requirements.txt includes:

Flask==2.3.3
firebase-admin==6.5.0


Firebase Configuration:

Create a Firebase project at Firebase Console.
Enable Email/Password, Google, and Phone authentication in Authentication > Sign-in method.
Configure email verification and password reset templates in Authentication > Templates.
For phone authentication, ensure reCAPTCHA and SMS settings are configured.
Download the Firebase Admin SDK service account key and place it in the project root as sentiment-analysis-cc7ce-firebase-adminsdk-fbsvc-59b4f37414.json.


Verify Firebase Config:

Ensure the Firebase configuration in login.html and register.html matches your Firebase project's credentials:const firebaseConfig = {
    apiKey: "AIzaSyCofNTK9-TafcyMlI4MvQmmmBfqud9jSFI",
    authDomain: "sentiment-analysis-cc7ce.firebaseapp.com",
    projectId: "sentiment-analysis-cc7ce",
    storageBucket: "sentiment-analysis-cc7ce.firebasestorage.app",
    messagingSenderId: "614339285917",
    appId: "1:614339285917:web:bf63e34183dd8cc82d5574"
};




Run the Application:
python app.py


The app will run at http://localhost:5000.
Use debug=True for development only.



Usage

Home Page (/):

Displays a welcome message and links to login or register for unauthenticated users.
Shows the user's email and a dashboard link for authenticated users.


Registration (/register):

Users enter an email and password.
A verification email is sent automatically. Users must click the link to verify their email before logging in.
Redirects to the login page after successful registration.


Login (/login):

Supports three methods:
Email/Password: Requires a verified email. Enter email and password to log in.
Google: Uses Google Sign-In (typically auto-verified).
Phone: Enter a phone number (e.g., +1234567890), complete reCAPTCHA, and enter the SMS verification code.


Redirects to the dashboard upon successful login.


Password Reset (/reset_password):

Enter an email to receive a password reset link.
Redirects to the login page after sending the email.


Dashboard (/dashboard):

A protected page showing the user's email and a logout button.
Accessible only to authenticated users.


Logout (/logout):

Clears the session and redirects to the home page.



Security Notes

Service Account Key: The sentiment-analysis-cc7ce-firebase-adminsdk-fbsvc-59b4f37414.json file contains sensitive credentials. Do not commit it to version control. Use .gitignore to exclude it.
reCAPTCHA: Ensure reCAPTCHA is not blocked by browser extensions for phone authentication.
Email Verification: Enforced for email/password logins but bypassed for phone logins, as they don’t rely on email.
Session Management: Flask sessions are used for simplicity. For production, consider a more secure session store (e.g., Redis).

Troubleshooting

Registration Fails: Check Firebase Console for authentication settings and ensure the email/password provider is enabled.
Login Fails:
For email/password, verify the email is verified in Firebase Authentication.
For Google, ensure the Google provider is enabled and the Firebase config is correct.
For phone, check the phone number format (e.g., +1234567890) and SMS delivery settings in Firebase.


Email Verification Not Received: Check Firebase Authentication > Templates and the user’s spam/junk folder.
reCAPTCHA Issues: Ensure browser extensions (e.g., ad blockers) are not interfering with reCAPTCHA.
Token Errors: Verify the Firebase Admin SDK service account key and Firebase config in login.html and register.html.

Dependencies

Backend:
Flask: Web framework for routing and templating.
firebase-admin: Python SDK for Firebase Authentication (server-side).


Frontend:
Firebase JavaScript SDK: Handles client-side authentication (loaded via CDN).
Tailwind CSS: Styling framework (loaded via CDN).



License
This project is licensed under the MIT License.
Contributing
Feel free to submit issues or pull requests to improve the project. Ensure any changes maintain compatibility with Firebase Authentication and Flask.
