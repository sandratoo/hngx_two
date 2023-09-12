import os
from flask import Flask, jsonify, request, abort
from flask_sqlalchemy import SQLAlchemy

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///' + os.path.join(basedir, 'database.db')
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SECRET_KEY"] = "SECRETKEY"

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

    return jsonify({"persons": output})
    
#Read one specific person
@app.route("/api/<id>", methods=["GET"])
def fetch_person(id):
    person = Person.query.filter_by(id=id).first()
    if person is None:
        abort(404)

    person_data = {"firstname":person.firstname,"lastname":person.lastname,"job":person.job}

    return jsonify({person.id: person_data})

#Create a new person
@app.route("/api", methods=["POST"])
def add_person():
    person = Person(firstname=request.json["firstname"],
     lastname=request.json["lastname"],
     job=request.json["job"])

    db.session.add(person)
    db.session.commit()

    person_data = {"firstname":person.firstname,"lastname":person.lastname,"job":person.job}

    return jsonify({person.id: person_data})

#Update an existing person
@app.route("/api/<id>", methods=["PUT"])
def update_person(id):
    person = Person.query.filter_by(id=id).first()

    if person is None:
        abort(404)
    person.firstname=request.json["firstname"]
    person.lastname=request.json["lastname"]
    person.job=request.json["job"]
        
    db.session.commit()

    person_data = {"firstname":person.firstname,"lastname":person.lastname,"job":person.job}

    return jsonify({person.id: person_data})
        
#Delete a person
@app.route("/api/<id>", methods=["DELETE"])
def delete_person(id):
    person = Person.query.filter_by(id=id).first()

    if person is None:
        abort(404)
    db.session.delete(person)
    db.session.commit()

    return jsonify({person.id : "deleted"})


if __name__ == ("__main__"):
    app.run()