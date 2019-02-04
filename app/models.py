from app import db
from datetime import datetime


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    last_login = db.Column(db.DateTime)
    posted_questions = db.relationship('Question', backref='author', lazy=True)
    posted_answers = db.relationship('Answer', backref='author', lazy=True)
    comments = db.relationship('Comment', backref='commentor', lazy=True)


    def __repr__(self):
        return f"User email: {self.email}, created at: {self.created_at}"


    def save(self):
        db.session.add(self)
        db.session.commit()


    def query_all(self):
        return self.query.all()


    def query_first(self):
        return self.query.first()


class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    body = db.Column(db.Text, nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    #TODO implement one-one relationship of preferred answer
    answers = db.relationship('Answer', backref='question', lazy=True)


    def __repr__(self):
        return f"Question title: {self.title}, Body: {self.body}, Authored by: {self.author_id}"


class Answer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)
    up_votes = db.Column(db.Integer, nullable=True)
    down_votes = db.Column(db.Integer, nullable=True)
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    quesion_id = db.Column(db.Integer, db.ForeignKey('question.id'), nullable=False)
    comments = db.relationship('Comment', backref='answer', lazy=True)


class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    message = db.Column(db.Text, nullable=False)
    edited_at = db.Column(db.DateTime, nullable=True)
    answer_id = db.Column(db.Integer, db.ForeignKey('answer.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)