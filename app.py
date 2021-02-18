# 1. import Flask
from flask import Flask

# 2. Create an app, being sure to pass __name__
app = Flask(__name__)

# 3. Define what to do when a user hits the index route
@app.route("/")
def home():
    print("Server received request for 'Home' page...")
    return "Welcome to my 'Hawaii Temperature Analysis' page!"

# 4. Define what to do when a user hits the /precipitation route
@app.route("/api/v1.0/precipitation")
def precipitation():
    print("Server received request for 'Precipitation' page...")
    return "Welcome to my 'Precipitation' page!"
    
    return jasonify (p_score)

# 5. Define what to do when a user hits the /stations route
@app.route("/api/v1.0/stations")
def stations():
    print("Server received request for 'Stations' page...")
    return "Welcome to my 'Stations' page!"
    
    return jasonify (active)

# 6. Define what to do when a user hits the /tobs route
@app.route("/api/v1.0/tobs")
def tobs():
    print("Server received request for 'Temperatures' page...")
    return "Welcome to my 'Temperatures' page!"

    return jasonify (tobs_score)



if __name__ == "__main__":
    app.run(debug=True)