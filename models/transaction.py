from db import db

class TransactionModel(db.Model):
    __tablename__ = 'transactions'

    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(80), unique=True, nullable=False)
    value = db.Column(db.Float, nullable=False)
    
    category_id = db.Column(db.Integer, db.ForeignKey("categories.id"))
    category = db.relationship("CategoryModal", back_populates="transactions")

