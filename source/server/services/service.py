# Class used to access authors data using a session

from server.models.model import Car
from server.models.model import Customer

# Class used to access authors data using a session

class RentalService:
    def __init__(self, db):
        self.db = db

    def get_all(self):
        return self.db.session.query(Car).all()

    # Not used in the GUI, included for reference
    def get(self, id):
        return self.db.session.query(Car).get(id)

    # Not used in the GUI, included for reference
    def add(self, json):
        rental = Car(model=json['model'], rentStartDate=json['rentStartDate'],rentEndDate =json['rentEndDate'], price=json['price'],customer_id=json['customer_id'])
        self.db.session.add(rental)
        self.db.session.commit()
        return rental

    # Not used in the GUI, included for reference
    def update(self, rental):
        # We don't actually need the author object here, we just need to commit
        self.db.session.commit()

    # Not used in the GUI, included for reference
    def delete(self, rental):
        self.db.session.delete(rental)
        self.db.session.commit()




class CustomerService:
    def __init__(self, db):
        self.db = db

    def get_all(self):
        return self.db.session.query(Customer).all()

    # Not used in the GUI, included for reference
    def get(self, id):
        return self.db.session.query(Customer).get(id)

    # Not used in the GUI, included for reference
    def add(self, json):
        customer = Customer(fullname=json['fullname'], address=json['address'],
                     phone_number =json['phone_number'], city=json['city'])
        self.db.session.add(customer)
        self.db.session.commit()
        return customer

    # Not used in the GUI, included for reference
    def update(self, customer):
        # We don't actually need the author object here, we just need to commit
        self.db.session.commit()

    # Not used in the GUI, included for reference
    def delete(self, customer):
        self.db.session.delete(customer)
        self.db.session.commit()
