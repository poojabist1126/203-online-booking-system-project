Title: Online Tutor Booking System

Description: A web-based application that allows tutors and students to connect online. It allows students to find tutors and book the sessions. Tutors can login to their dashboard and confirm or reject the booking requests.

Technologies used:
Python- backend logic
Flask- web framework
SQLite- database to store users and bookings
WTForms- form validation
HTML/CSS- fronted templates
Jinja templates

Features:
- Student and tutor registration and login
- Browse available tutors with their subject and hourly rate
- Book a tutoring session by filling in personal details
- Booking confirmation page after submitting
- Tutor dashboard to confirm or reject bookings
- Status tags showing Pending, confirmed, or rejected
  
 How to Run:
 1. Clone the repository
 2. Install dependencies

    Pip install flask flask-wtf wtforms email-validator
    1. Run the app
  Python app.py
    1. Open the browser and go to
  http://127.0.0.1:5000

Database
Uses SQLite, Database is created automatically when you run the app.

Pages:

   ** Page                                  
       Home                                    
       Tutors                                 
       Book a session                          
       Confirmation                          
       Student Login                          
       Tutor login                            
       Student Register                       
       Tutor Register                         
       Tutor Dashboards                       
