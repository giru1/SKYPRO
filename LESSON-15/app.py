import json
import sqlite3
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


@app.route('/')
def index():  # put application's code here
    return 'Hello World!'


@app.route('/item/<id>', methods=['GET', 'PUT', 'DELETE'])
def get_animal_id(id):
    db = sqlite3.connect('animal.sqlite')
    cursor = db.cursor()

    queries = 'select "index",
    'animal_breed.breed,'
    'animal_color.color,'
    'animal_types.name,'
    'animal_fin.age_upon_outcome,'
    'animal_fin.animal_id,'
    'animal_fin.name,'
    'animal_fin.date_of_birth,'
    'animal_outcome.outcome,'
    'animal_outcome.oc_month,'
    'animal_outcome.oc_year,'
    'animal_outcome.oc_subtype'


    'FROM animals'
    'left join animal_breed on animals."index" = animal_breed.id'
    'left join animal_color on animals."index" = animal_color.id'
    'left join animal_types on animals."index" = animal_types.id'
    'left join animal_fin on animals."index" = animal_fin.id'
    'left join animal_outcome on animals."index" = animal_outcome.id'
    'where "index" = 5'

cursor.execute(queries.GET_ANIMAL_ID, (id,))
row = cursor.fetchone()

cursor.close()
print(jsonify(row))
return jsonify(row)

if __name__ == '__main__':
    app.run(debug=True)
