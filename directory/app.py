from flask import Flask, render_template, request, redirect, url_for
from data import db, Data

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///Data.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

@app.before_first_request
def create_table():
    db.create_all()


@app.route("/")
def index():
    all_data = Data.query.all()

    return render_template("index.html", contacts=all_data)


@app.route("/insert", methods=["POST"])
def insert():

    if request.method == "POST":

        name = request.form["name"]
        surname = request.form["surname"]
        telephone = request.form["phone"]
        address =request.form["address"]

        my_data = Data(name, surname, telephone, address)
        db.session.add(my_data)
        db.session.commit()

        return redirect(url_for('index'))

@app.route("/update", methods=["POST", "GET"])
def update():

    if request.method == "POST":
        my_data = Data.query.get(request.form.get("id"))

        my_data.name = request.form["name"]
        my_data.surname = request.form["surname"]
        my_data.phone = request.form["telephone"]
        my_data.address = request.form["address"]

        db.session.add(my_data)
        db.session.commit()

        return redirect(url_for('index'))


@app.route("/delete/<id>", methods=["GET","POST"])
def delete(id):
    my_data = Data.query.get(id)
    db.session.delete(my_data)
    db.session.commit()

    return redirect(url_for("index"))








if __name__ == "__main__":
    app.run(debug=True)
