import pandas as pd

# only need if we read our data from a sql databse
    # import sqlalchemy
    # from sqlalchemy.ext.automap import automap_base
    # from sqlalchemy.orm import Session
    # from sqlalchemy import create_engine, func

from flask import Flask, jsonify

# only need if we read our data from a sql databse
    #################################################
    # Database Setup
    #################################################
    # engine = create_engine("sqlite:///hawaii.sqlite")

    # # reflect an existing database into a new model
    # Base = automap_base()

    # # reflect the tables
    # Base.prepare(engine, reflect=True)

    # # Save reference to the tables
    # Measurement = Base.classes.measurement
    # Station = Base.classes.station

    # # Create our session (link) from Python to the DB
    # session = Session(engine)

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

#################################################
# Flask Routes
#################################################

@app.route("/")
def whatever():
    return




if __name__ == "__main__":
    app.run(debug=True)