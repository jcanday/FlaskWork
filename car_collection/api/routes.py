from flask import Blueprint, request, jsonify
from car_collection.helpers import token_required
from car_collection.models import db, User, Car, car_schema, cars_schema

api = Blueprint('api', __name__, url_prefix = '/api')

@api.route('/test')
@token_required
def test(current_user_token):
    return {'User' : 'Value'}

@api.route('/cars', methods = ['POST'])
@token_required
def create_car(current_user_token):
    name = request.json['name']
    make = request.json['make']
    model = request.json['model']
    year = request.json['year']
    user_token = current_user_token.token
    
    print(f"Testing: {current_user_token.token}")
    
    car = Car(name, make, model, year, user_token = user_token)
    
    db.session.add(car)
    db.session.commit()
    res = car_schema.dump(car)
    
    return jsonify(res)

@api.route('/cars', methods = ['GET'])
@token_required
def get_cars(current_user_token):
    own = current_user_token.token
    cars = Car.query.filter_by(user_token = own).all()
    res = cars_schema.dump(cars)
    
    return jsonify(res)

@api.route('/cars<id>', methods = ['GET'])
@token_required
def get_car(current_user_token, id):
    own = current_user_token.token
    if own == current_user_token.token:
        car = Car.query.get(id)
        res = car_schema.dump(car)
        return jsonify(res)
    
    else:
        return jsonify('message : Valid Token Not Received'), 401
    
@api.route('/cars/<id>', methods = ['POST', 'PUT'])
@token_required
def update_car(current_user_token, id):
    car = car.query.get(id)
    
    car.name = request.json['name']
    car.make = request.json['make']
    car.model = request.json['model']
    car.year = request.json['year']
    car.user_token = current_user_token.token
    
    db.session.commit()
    
    res = car_schema.dump(car)
    
    return jsonify(res)

@api.route('/cars/<id>', methods = ['DELETE'])
@token_required
def delete_car(current_user_token, id):
    car = car.query.get(id)
    
    db.session.delete(car)
    
    db.session.commit()
    
    res = car_schema.dump(car)
    
    return jsonify(res)
    
    