# importing the class "Flask" which create website object instances
from flask import Flask, render_template
import pandas as pd

# it's possibile to define other static paths with static_url_path, beyond the default one "static"
app = Flask(__name__, static_url_path='/static')

# applying route method to the object app
# make sure to add the html pages inside the "templates" folder 
# the images has to be in a folder called "static"
# and render them through the render_template function

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/api/v1/<station>/<date>")
def api(station, date):
    df = pd.read_csv()
    return {"station": station,
            "date": date,
            "temperature": temperature}

# the app has to enabled only when we run this script directly
# in order to run multiple apps, we can specify the port number
if __name__ == "__main__":
   app.run(debug = True, port = 5001)