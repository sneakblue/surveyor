from .db import db, environment, SCHEMA

class Field(db.Model):
    __tablename__ = 'fields'

    if environment == 'production':
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String(255), nullable=False)
    choices = db.Column(db.String(255), nullable=True)
    survey_id = db.Column(db.Integer, db.ForeignKey('surveys.id'))
    field_type_id = db.Column(db.Integer, db.ForeignKey('field_types.id'))

    survey = db.relationship('Survey', back_populates='fields',  lazy=True)
    field_type = db.relationship('Field_Type', back_populates='field_counts', lazy=True)
    

