from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from controllers.controller import Rental, RentalList, Customer, CustomerList
from services.service import RentalService, CustomerService


def main():
    # Create the Flask app
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///rental.sqlite'

    # Create the Flask-RESTful API
    api = Api(app)

    # Connect to the database with Flask-SQLAlchemy
    db = SQLAlchemy(app)

    # Create the authors service. The database is dependency injected to the constructor.
    # Controllers can then use db.session to get access to a scoped session.
    rentals = RentalService(db)
    customers = CustomerService(db)

    # Register the route for each resource
    api.add_resource(RentalList, '/rentals/',
                     resource_class_args=[rentals])  # Send authors as an argument to AuthorList

    api.add_resource(Rental, '/rentals/<id>',
                     resource_class_args=[rentals])   # Send authors as an argument to Author

    api.add_resource(CustomerList, '/customers/',
                     resource_class_args=[customers])  # Send authors as an argument to AuthorList

    api.add_resource(Customer, '/customers/<id>',
                     resource_class_args=[customers])   # Send authors as an argument to Author

    app.run(debug=True)


if __name__ == '__main__':
    main()