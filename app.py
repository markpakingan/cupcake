"""Flask app for Cupcakes"""

from flask import Flask, render_template,redirect, flash, jsonify
from models import db, connect_db, Cupcake
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.app_context().push() 

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///cupcake'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCH EMY_ECHO'] = True
app.config['SECRET_KEY'] = "SECRET!"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

debug = DebugToolbarExtension(app)


app.route("/api/cupcakes")
def show_all_cupcakes():
    """Get data about all cupcakes."""

    all_cupcakes = [Cupcake.serialize() for cupcake in Cupcake.query.all()]
    return jsonify(all_cupcakes)
