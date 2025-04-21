from app.extensions import db

class Email(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    to = db.Column(db.String(255), nullable=False)
    subject = db.Column(db.String(255))
    body = db.Column(db.Text)
