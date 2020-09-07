from flask import *
import config
import vyos

app = Flask(__name__)
app.secret_key = config.FLASK_SECRET_KEY

@app.route('/', methods=['get'])
def index():
    return render_template("main.html")
