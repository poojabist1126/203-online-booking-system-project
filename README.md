#  Tutor Booking System

A web-based application where students can browse available tutors, view their subjects and hourly rates, and book a session. Built with Flask (Python), HTML, and CSS.

---

##  Team Members

| Name | Role |
|------|------|
| Pooja | Tutor listing page, CSS styling, search section, static assets |
| Shishir | Flask setup, routing, home page |

---

##  Tech Stack

- **Backend:** Python, Flask
- **Frontend:** HTML, CSS
- **Templating:** Jinja2
- **Version Control:** Git & GitHub

---

##  Project Structure

```
ROUGH_OBS/
│
├── static/
│   ├── style.css        # All CSS styling
│   ├── James.png        # Tutor profile images
│   ├── Lisa.png
│   ├── Michael.png
│   ├── Sarah.png
│   ├── David.png
│   ├── Emma.png
│   └── Daniel.png
│
├── templates/
│   └── index.html       # Main tutor listing page
│
└── app.py               # Flask application and tutor data
```

---

##  How to Run the App

### Step 1 — Make sure Python is installed
Open your terminal and check:
```
python --version
```
If Python is not installed, download it from https://www.python.org

---

### Step 2 — Install Flask
In your terminal, run:
```
pip install flask
```

---

### Step 3 — Go to the project folder
```
cd path/to/ROUGH_OBS
```
For example:
```
cd Desktop/ROUGH_OBS
```

---

### Step 4 — Run the app
```
python app.py
```
You should see something like this in the terminal:
```
 * Running on http://127.0.0.1:5000
```

---

### Step 5 — Open in browser
Open your browser and go to:
```
http://127.0.0.1:5000
```
The tutor listing page should now be visible.

---

##  Features (First Prototype)

- Navigation bar with logo and links
- Search section with subject input, date picker, and time dropdown
- Tutor listing page showing 7 tutors with profile pictures, subjects, rates, and Book Now buttons
- Dynamic tutor cards using Jinja2 templating
- Clean CSS styling with flexbox layout

---

## Planned for Part B

- Connect search bar to filter tutors by subject, date, and time
- Book Now button linked to a booking form page
- Database integration to replace hardcoded tutor data
- Improved UI and responsive design

