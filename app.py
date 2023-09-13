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
    name = db.Column(db.String(50), nullable=False)
    #lastname = db.Column(db.String(50), nullable=False)
    #job = db.Column(db.String(150), nullable=False)

    def __str__(self):
        return f"Name:{self.id}: Job:{self.name}"
        

#Read all People from database
@app.route("/api",methods=["GET"])
def fetch_all():
    persons = Person.query.all()
    output = []
    for person in persons:
        data = {"id":person.id,"name":person.name}
        output.append(data)

    return jsonify({"persons": output})
    
#Read one specific person
@app.route("/api/<id>", methods=["GET"])
def fetch_person(id):
    person = Person.query.filter_by(id=id).first()
    if person is None:
        abort(404)

    return jsonify({person.id: person.name})

#Create a new person
@app.route("/api", methods=["POST"])
def add_person():
    person = Person(name=request.json["name"])

    db.session.add(person)
    db.session.commit()

    return jsonify({person.id: person.name})

#Update an existing person
@app.route("/api/<id>", methods=["PUT"])
def update_person(id):
    person = Person.query.filter_by(id=id).first()

    if person is None:
        abort(404)
    person.name=request.json["name"]
        
    db.session.commit()

    return jsonify({person.id: person.name})
        
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