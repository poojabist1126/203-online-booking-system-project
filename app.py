from flask import Flask, render_template, request
app = Flask(__name__)

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

@app.route('/')
def home():
    return render_template('index.html', tutors=tutors)

@app.route('/booking/<int:tutor_id>')
def booking(tutor_id):
    return render_template('booking.html', tutor=tutors[tutor_id - 1])

if __name__ == '__main__':
    app.run(debug=True)