import sqlite3
from flask import Flask, render_template, request, redirect, url_for, session, flash
from forms import BookingForm

app= Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key-here'

def init_db():
    conn = sqlite3.connect("users.db")
    c = conn.cursor()
    c.execute("""
              CREATE TABLE IF NOT EXISTS users (
              id INTEGER PRIMARY KEY AUTOINCREMENT,
              username TEXT NOT NULL,
              password TEXT NOT NULL,
              role TEXT NOT NULL
        )
    """)

    c.execute("""
              CREATE TABLE IF NOT EXISTS bookings (
              id INTEGER PRIMARY KEY AUTOINCREMENT,
              student_name TEXT NOT NULL,
              email TEXT NOT NULL,
              address TEXT NOT NULL,
              age INTEGER NOT NULL,
              gender TEXT NOT NULL,
              tutor_id INTEGER NOT NULL,
              status TEXT NOT NULL DEFAULT 'Pending'
            )
        """)
    conn.commit()
    conn.close()

init_db()

tutors = [
    {
        "id": 1, 
        "name": "James", 
        "major": "Computer Science", 
        "rate": 30,
        "profile_pic": "static/James.png"
    },
    {
        "id": 2, 
        "name": "Lisa", 
        "major": "English", 
        "rate": 28,
        "profile_pic": "static/Lisa.png"
    },
    
 
     {
        "id": 3,
        "name": "Michael",
        "major": "Mathematics",
        "rate": 35,
        "profile_pic": "static/Michael.png"
        
    },
    {
        "id": 4,
        "name": "Sarah",
        "major": "Physics",
        "rate": 32,
        "profile_pic": "static/Sarah.png"
        
    },
    {
        "id": 5,
        "name": "David",
        "major": "Chemistry",
        "rate": 33,
        "profile_pic": "static/David.png"
        
    },
    {
        "id": 6,
        "name": "Emma",
        "major": "Biology",
        "rate": 31,
        "profile_pic": "static/Emma.png"
       
    },
    {
        "id": 7,
        "name": "Daniel",
        "major": "History",
        "rate": 28,
        "profile_pic": "static/Daniel.png"
       
    },
]

@app.route("/")
def index():
    return redirect(url_for('register_student'))

@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/tutor")
def tutor():
    return render_template("tutor.html", tutors=tutors) 

@app.route('/booking/<int:tutor_id>', methods=['GET', 'POST'])
def booking(tutor_id):
    tutor = tutors[tutor_id - 1]
    form = BookingForm()
    if form.validate_on_submit():
        conn = sqlite3.connect("users.db")
        c = conn.cursor()
        c.execute("""INSERT INTO bookings (student_name, email, address, age, gender, tutor_id, status)
                     VALUES (?, ?, ?, ?, ?, ?, 'Pending')""",
                  (form.name.data, form.email.data, form.Address.data, form.Age.data, form.Gender.data, tutor_id))
        conn.commit()
        conn.close()

        session['booking'] = {
            'name': form.name.data,
            'email': form.email.data,
            'address': form.Address.data,
            'age': form.Age.data,
            'gender': form.Gender.data,
            'tutor_id': tutor_id
        }
        return redirect(url_for('confirmation'))
    return render_template('mybooking.html',tutor=tutor, form=form)


@app.route('/confirmation')
def confirmation():
    booking = session.get('booking')
    if not booking:
        return redirect(url_for('home'))
    tutor = tutors[booking['tutor_id'] - 1]
    return render_template('confirmation.html', booking=booking, tutor=tutor)

@app.route('/register-student', methods=['GET', 'POST'])
def register_student():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        conn = sqlite3.connect("users.db")
        c = conn.cursor()
        c.execute("INSERT INTO users (username, password, role) VALUES (?, ?, ?)", (username, password, "student"))
        conn.commit()
        conn.close()
        return redirect(url_for('login_student'))
    return render_template("register_student.html")



@app.route('/register-tutor', methods=['GET', 'POST'])
def register_tutor():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        conn = sqlite3.connect("users.db")
        c = conn.cursor()
        c.execute("INSERT INTO users (username, password, role) VALUES (?, ?, ?)", (username, password, "tutor"))
        conn.commit()
        conn.close()
        return redirect(url_for('login_tutor'))
    return render_template("register_tutor.html")

@app.route('/login-student', methods=['GET', 'POST'])
def login_student():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        conn = sqlite3.connect("users.db")
        c = conn.cursor()
        c.execute("SELECT * FROM users WHERE username=? AND password=? AND role='student'", (username, password))
        user = c.fetchone()
        conn.close()
        if user:
            session['user'] = username
            session['role'] = 'student'
            return redirect(url_for('home'))
        return render_template("login_student.html")
    return render_template("login_student.html")
    
@app.route('/login-tutor', methods=['GET', 'POST'])
def login_tutor():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        conn = sqlite3.connect("users.db")
        c = conn.cursor()
        c.execute("SELECT * FROM users WHERE username=? AND password=? AND role='tutor'", (username, password))
        user = c.fetchone()
        conn.close()
        if user:
            session['user'] = username
            session['role'] = 'tutor'
            return redirect(url_for('home'))
    return render_template("login_tutor.html")

@app.route('/tutor-dashboard')
def tutor_dashboard():
    if session.get('role') != 'tutor':
        return redirect(url_for('login_tutor'))

    conn = sqlite3.connect("users.db")
    c = conn.cursor()
    c.execute("SELECT id, student_name, email, address, age, gender, tutor_id, status FROM bookings ORDER BY id DESC")
    rows = c.fetchall()
    conn.close()

    bookings_list = []
    for row in rows:
        tutor_info = tutors[row[6] - 1]
        bookings_list.append({
            'id': row[0],
            'student_name': row[1],
            'email': row[2],
            'address': row[3],
            'age': row[4],
            'gender': row[5],
            'tutor_name': tutor_info['name'],
            'tutor_major': tutor_info['major'],
            'status': row[7]
        })

    return render_template('tutor_dashboard.html', bookings=bookings_list)

@app.route('/booking-action/<int:booking_id>/<action>')
def booking_action(booking_id, action):
    if session.get('role') != 'tutor':
        return redirect(url_for('login_tutor'))
 
    new_status = 'Confirmed' if action == 'confirm' else 'Rejected'
    conn = sqlite3.connect("users.db")
    c = conn.cursor()
    c.execute("UPDATE bookings SET status=? WHERE id=?", (new_status, booking_id))
    conn.commit()
    conn.close()
    return redirect(url_for('tutor_dashboard'))

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('home'))


if __name__ == "__main__":
    app.run(debug=True)