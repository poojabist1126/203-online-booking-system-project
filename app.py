import flask
app = flask.Flask(__name__)

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
    return flask.render_template('index.html', tutors=tutors)

if __name__ == '__main__':
    app.run(debug=True)

