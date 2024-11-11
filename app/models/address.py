from app.extensions.database import db

class Address(db.Model):
    __tablename__ = "addresses"

    ADD_addressId = db.Column(db.Integer, primary_key=True)  # Unique address ID
    ADD_street = db.Column(db.String(200), nullable=False)
    ADD_ext_number = db.Column(db.String(10), nullable=False)
    ADD_int_number = db.Column(db.String(10), nullable=True)
    ADD_neighborhood = db.Column(db.String(50), nullable=False)
    ADD_zip_code = db.Column(db.String(5), nullable=False)
    ADD_city = db.Column(db.String(50), nullable=False)
    ADD_state = db.Column(db.String(50), nullable=False)
    ADD_special_instructions = db.Column(db.String(200), nullable=True)
    
    def __init__(
        self, ADD_street, ADD_ext_number, ADD_neighborhood, ADD_zip_code,
        ADD_city, ADD_state, ADD_special_instructions=None, ADD_int_number=None
    ):
        self.ADD_street = ADD_street
        self.ADD_ext_number = ADD_ext_number
        self.ADD_int_number = ADD_int_number
        self.ADD_neighborhood = ADD_neighborhood
        self.ADD_zip_code = ADD_zip_code
        self.ADD_city = ADD_city
        self.ADD_state = ADD_state
        self.ADD_special_instructions = ADD_special_instructions

    def __repr__(self):
        return (f"{self.ADD_street}, No. {self.ADD_ext_number},"
                f"Col. {self.ADD_neighborhood}, {self.ADD_zip_code}, {self.ADD_city}")
