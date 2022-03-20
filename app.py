from flask import Flask
from database.db import initialize_db
from resources.movie import movies

app = Flask(__name__)

# MongoDB Config
app.config['MONGO_URI'] = 'mongodb://localhost:27017/movie-bag'
initialize_db(app)

app.register_blueprint(movies)

app.run(debug=True)
