from db import db


class Test(db.Model):
    __tablename__ = 'Tests'

    id = db.Column(db.Integer, primary_key=True)
    name_fa = db.Column(db.String(80))
    name_en = db.Column(db.String(80), nullable=True)
    time = db.Column(db.Integer)
    questions = db.relationship('Question', lazy='dynamic')

    def __init__(self, name_fa, time):
        self.name_fa = name_fa
        self.time = time

    def json(self):
        questions = []
        for question in self.questions:
            questions.append(question)
        questions.sort(key=lambda x: x.index)


        return {
            'id': self.id,
            'name_fa': self.name_fa,
            'name_en': self.name_en,
            'time': self.time,
            'questions': [question.json() for question in questions],
        }

    @classmethod
    def get_by_id(cls, test_id):
        return cls.query.filter_by(id=test_id).first()


class TestAnswers(db.Model):
    __tablename__ = 'TestAnswers'

    id = db.Column(db.Integer, primary_key=True)
    question_index = db.Column(db.Integer)
    answer_index = db.Column(db.Integer)
    test_id = db.Column(db.Integer, db.ForeignKey('Tests.id'))

    def __init__(self):
        pass

    def json(self):
        return {
            'id': self.id,
            'question_index': self.question_index,
            'answer_index': self.answer_index,
            'test_id': self.test_id,
        }

    def get_by_test_id(self, test_id):
        return self.query.filter_by(test_id=test_id).all()

class Question(db.Model):
    __tablename__ = 'Questions'

    id = db.Column(db.Integer, primary_key=True)
    question_fa = db.Column(db.String(80))
    question_en = db.Column(db.String(80), nullable=True)
    index = db.Column(db.Integer, nullable=True)
    question_image = db.Column(db.String(80), nullable=True)

    choices = db.relationship('Choice', lazy='dynamic')
    test_id = db.Column(db.Integer, db.ForeignKey('Tests.id'))
    # test = db.relationship('Test')

    def __init__(self, question_fa, index, test_id):
        self.question_fa = question_fa
        self.test_id = test_id
        self.index = index
        self.question_image = ""

    def json(self):
        choices = []
        for choice in self.choices:
            choices.append(choice)
        choices.sort(key=lambda x: x.index)
        return {
            'id': self.id,
            'question_fa': self.question_fa,
            'question_en': self.question_en,
            'index': self.index,
            'choices': [choice.json() for choice in choices],
            'question_image': self.question_image,
        }


class Choice(db.Model):
    __tablename__ = 'Choices'

    id = db.Column(db.Integer, primary_key=True)
    choice_fa = db.Column(db.String(80))
    choice_en = db.Column(db.String(80), nullable=True)
    index = db.Column(db.Integer)
    choice_image = db.Column(db.String(80), nullable=True)

    question_id = db.Column(db.Integer, db.ForeignKey('Questions.id'))
    # question = db.relationship('Question')

    def __init__(self, choice_fa, index, question_id):
        self.choice_fa = choice_fa
        self.index = index
        self.question_id = question_id
        self.choice_image = ""

    def json(self):
        return {
            'id': self.id,
            'choice_fa': self.choice_fa,
            'choice_en': self.choice_en,
            'index': self.index,
            'choice_image': self.choice_image,
        }

