from .. import db

class Workout(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    user_id=db.Column(db.Integer,db.ForeignKey('user.id'),nullable=False)
    exercise_type=db.Column(db.String(100),nullable=False)
    duration=db.Column(db.Integer,nullable=False) #in minutes
    date=db.Column(db.DateTime,default=db.func.current_timestamp())
