from .db import db, environment, SCHEMA

class Field_Type(db.Model):
    __tablename__ = 'field_types'

    if environment == 'production':
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    field = db.Column(db.String(50), nullable=False)

    field_counts = db.relationship('Field', back_populates='field_type', lazy=True)