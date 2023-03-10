"""Flask app for Cupcakes"""

from flask import Flask, render_template,redirect, flash, jsonify, request
from models import db, connect_db, Cupcake

from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.app_context().push() 

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///cupcakes'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCH EMY_ECHO'] = True
app.config['SECRET_KEY'] = "SECRET!"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

debug = DebugToolbarExtension(app)

connect_db(app)


@app.route("/")
def home_page():
    return render_template ("index.html")

# ************************************************************************************
@app.route("/api/cupcakes")
def show_all_cupcakes():
    """Get data about all cupcakes in JSON"""

    all_cupcakes = [cupcake.serialize() for cupcake in Cupcake.query.all()]
    return jsonify(all_cupcakes = all_cupcakes)

@app.route("/api/cupcakes", methods=["POST"])
def create_cupcake():
    """Add cupcake, and return data about new cupcake.

    Returns JSON like:
        {cupcake: [{id, flavor, rating, size, image}]}
    """

    data = request.json

    cupcake = Cupcake(
        flavor=data['flavor'],
        rating=data['rating'],
        size=data['size'],
        image=data['image'] or None)

    db.session.add(cupcake)
    db.session.commit()

    # POST requests should return HTTP status of 201 CREATED
    return (jsonify(cupcake=cupcake.serialize()), 201)


@app.route("/api/cupcakes/<int:cupcake_id>")
def single_cupcake_data(cupcake_id):
    """Get data about a single cupcake."""

    single_cupcake = Cupcake.query.get(cupcake_id)
    return jsonify(single_cupcake = single_cupcake.serialize())


@app.route ("/api/cupcakes/<int:cupcake_id>", methods = ["PATCH"])
def update_single_cupcake(cupcake_id):

    single_cupcake = Cupcake.get_or_404(cupcake_id)
    
    data = request.json

    single_cupcake.flavor = data['flavor']
    single_cupcake.rating = data['rating']
    single_cupcake.size = data['size']
    single_cupcake.image = data['image']

    db.session.add(single_cupcake)
    db.session.commit()

    return jsonify(single_cupcake=single_cupcake.serialize())

@app.route ("/api/cupcakes/<int:cupcake_id>", methods = ["DELETE"])
def delete_single_cupcake(cupcake_id):

    single_cupcake = Cupcake.query.get_or_404(cupcake_id)

    db.session.delete(single_cupcake)
    db.session.commit()

    return jsonify(message="Deleted")

