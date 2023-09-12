import os
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///' + os.path.join(basedir, 'database.db')
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(50), nullable=False)
    lastname = db.Column(db.String(50), nullable=False)
    job = db.Column(db.String(150), nullable=False)

    def __str__(self):
        return f"Name:{self.firstname}: Job:{self.job}"
        

#Read all People from database
@app.route("/api/users",methods=["GET"])
def fetch_all():
    persons = Person.query.all()
    output = []
    for person in persons:
        data = {"id":person.id,"firstname":person.firstname,"lastname":person.lastname,"job":person.job}
        output.append(data)

    return {"persons": output}
    
#Read one specific person
@app.route("/api/{person_id}")
def fetch_person():
    return "person"

#Create a new person
@app.route("/api/users", methods=["POST"])
def add_person():
    person = Person(firstname=request.json["firstname"],
     lastname=request.json["lastname"],
      job=request.json["job"])
    db.session.add(person)
    db.session.commit()
    return{person.id: person.firstname}


if __name__ == ("__main__"):
    app.run()