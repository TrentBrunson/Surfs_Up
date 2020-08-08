#%%
from flask import Flask
app = Flask(__name__)

#%%
@app.route('/')
def hello_world():
    return 'Hello World!'
#%%
import datetime as dt
import numpy as np
import pandas as pd
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, jsonify
#%%
# create engine for connection and reflect the DB
engine = create_engine("sqlite:///hawaii.sqlite")
Base = automap_base()
Base.prepare(engine, reflect = True)
#%%
# create variable to hold references for tables & create session link
Measurement = Base.classes.measurement
Station = Base.classes.station
session = Session(engine)
#%%
# activate flask
app = Flask(__name__)

# %%
