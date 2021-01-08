from . import db

class Inventory(db.Model):
    """
    Inventory of card 
    """
    __tablename__ = 'inventory'

    id = db.Column(db.Integer, primary_key=True)
    value = db.Column(db.String(80), unique=True, nullable=False)
    monthyPrice = db.Column(db.Numeric(10,2), nullable=False)
    setupPrice = db.Column(db.Numeric(10,2), nullable=False)
    currency = db.Column(db.String(10), nullable=False)

    def __init__(self, value="", monthyPrice=0.0, setupPrice=0.0, currency="U$"):
        """
        Construct of inventory
        """
        self.value = value
        self.monthyPrice = monthyPrice
        self.setupPrice = setupPrice
        self.currency = currency
    
    def __repr__(self):
        """
        Magic method for repr
        """
        return '<User - id {}>'.format(self.id)
    
    def save(self):
        """
        Save current instance in database
        """
        db.session.add(self)
        db.session.commit()
    
    def update(self, data):
        #set all new values
        for field, value in data.items():
            setattr(self, field, value)
        db.session.commit()