from flask import jsonify, make_response, request
from flask_restful import Resource
from werkzeug.exceptions import *


# Class responsible for /rentals/
class RentalList(Resource):
    def __init__(self, rentals):
        self.rentals = rentals

    def get(self):
        return jsonify(self.rentals.get_all())

    # Not used in the GUI, included for reference
    def post(self):
        rental = self.rentals.add(request.json)

        # Use make_response to change the status code to 201 CREATED
        return make_response(jsonify(rental), 201)


# Class responsible for /authors/<id>
class Rental(Resource):
    def __init__(self, rentals):
        self.rentals = rentals

    # Not used in the GUI, included for reference
    def get(self, id):
        rental = self.rentals.get(id)

        if not rental:
            raise NotFound('Invalid id, author not found.')

        return jsonify(rental)

    # Not used in the GUI, included for reference

    def put(self, id):
        rental = self.rentals.get(id)

        if not rental:
            raise NotFound('Invalid id, author not found.')

        json = request.get_json()
        rental.model = json['model']
        rental.rentStartDate = json['rentStartDate']
        rental.rentEndDate = json['rentEndDate']
        rental.price = json['price']
        rental.customer_id = json['customer_id']

        self.rentals.update(rental)

        return jsonify(rental)

    # Not used in the GUI, included for reference
    def delete(self, id):
        rental = self.rentals.get(id)

        if not rental:
            raise NotFound('Invalid id, author not found.')

        self.rentals.delete(rental)

        return jsonify(rental)

# Class responsible for /rentals/
class CustomerList(Resource):
    def __init__(self, customers):
        self.customers = customers

    def get(self):
        return jsonify(self.customers.get_all())

    # Not used in the GUI, included for reference
    def post(self):
        customer = self.customers.add(request.json)

        # Use make_response to change the status code to 201 CREATED
        return make_response(jsonify(customer), 201)


# Class responsible for /authors/<id>
class Customer(Resource):
    def __init__(self, customers):
        self.customers = customers

    # Not used in the GUI, included for reference
    def get(self, id):
        customer = self.customers.get(id)

        if not customer:
            raise NotFound('Invalid id, author not found.')

        return jsonify(customer)

    # Not used in the GUI, included for reference
    def put(self, id):
        customer = self.customers.get(id)

        if not customer:
            raise NotFound('Invalid id, customer not found.')

        json = request.get_json()
        customer.fullname = json['fullname']
        customer.address = json['address']
        customer.phone_number = json['phone_number']
        customer.city = json['city']

        self.customers.update(customer)

        return jsonify(customer)

    # Not used in the GUI, included for reference
    def delete(self, id):
        customer = self.customers.get(id)

        if not customer:
            raise NotFound('Invalid id, customer not found.')

        self.customers.delete(customer)

        return jsonify(customer)