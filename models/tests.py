from db import db


class Test(db.Model):
    __tablename__ = 'Tests'

    id = db.Column(db.Integer, primary_key=True)
    name_fa = db.Column(db.String(80))
    name_en = db.Column(db.String(80), nullable=True)
    questions = db.relationship('Question', lazy='dynamic')

    def __init__(self, name_fa):
        self.name_fa = name_fa

    def json(self):
        return {
            'id': self.id,
            'name_fa': self.name_fa,
            'name_en': self.name_en,
            'questions': [question.json() for question in self.questions],
        }

    @classmethod
    def get_by_id(cls, test_id):
        return cls.query.filter_by(id=test_id).first()


class Question(db.Model):
    __tablename__ = 'Questions'

    id = db.Column(db.Integer, primary_key=True)
    question_fa = db.Column(db.String(80))
    question_en = db.Column(db.String(80), nullable=True)
    index = db.Column(db.Integer, nullable=True)

    choices = db.relationship('Choice', lazy='dynamic')
    test_id = db.Column(db.Integer, db.ForeignKey('Tests.id'))
    test = db.relationship('Test')

    def __init__(self, question_fa, index, test_id):
        self.question_fa = question_fa
        self.test_id = test_id
        self.index = index

    def json(self):
        return {
            'id': self.id,
            'question_fa': self.question_fa,
            'question_en': self.question_en,
            'index': self.index,
            'choices': [choice.json() for choice in self.choices],
            # 'test_id': self.test_id,
        }


class Choice(db.Model):
    __tablename__ = 'Choices'

    id = db.Column(db.Integer, primary_key=True)
    choice_fa = db.Column(db.String(80))
    choice_en = db.Column(db.String(80), nullable=True)
    index = db.Column(db.Integer)

    question_id = db.Column(db.Integer, db.ForeignKey('Questions.id'))
    question = db.relationship('Question')

    def __init__(self, choice_fa, index, question_id):
        self.choice_fa = choice_fa
        self.index = index
        self.question_id = question_id

    def json(self):
        return {
            'choice_fa': self.choice_fa,
            'choice_en': self.choice_en,
            'index': self.index,
            # 'question_id': self.question_id,
        }

