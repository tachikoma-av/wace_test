from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    content = db.Column(db.String(500), nullable=False)
    response = db.Column(db.String(500))

    def fillResponse(self, response):
        self.response = response
    
    def toJson(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'content': self.content,
            'response': self.response
        }

