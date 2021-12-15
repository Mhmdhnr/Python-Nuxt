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


class Question(db.Model):
    __tablename__ = 'Questions'

    id = db.Column(db.Integer, primary_key=True)
    question_fa = db.Column(db.String(80))
    question_en = db.Column(db.String(80), nullable=True)
    index = db.Column(db.Integer, nullable=True)
    indicator = db.Column(db.Integer)
    question_image = db.Column(db.String(80), nullable=True)

    question_choices = db.relationship('QuestionChoices', lazy='dynamic')
    test_id = db.Column(db.Integer, db.ForeignKey('Tests.id'))
    # test = db.relationship('Test')

    def __init__(self, question_fa, index, test_id, indicator):
        self.question_fa = question_fa
        self.test_id = test_id
        self.indicator = indicator
        self.index = index
        self.question_image = ""

    def json(self):
        question_choices = []
        for question_choice in self.question_choices:
            question_choices.append(question_choice)
        question_choices.sort(key=lambda x: x.index)
        return {
            'id': self.id,
            'question_fa': self.question_fa,
            'question_en': self.question_en,
            'index': self.index,
            'indicator': self.indicator,
            'choices': [question_choice.json() for question_choice in question_choices],
            'question_image': self.question_image,
        }


class QuestionChoices(db.Model):
    __tablename__ = 'QuestionChoices'
    id = db.Column(db.Integer, primary_key=True)
    index = db.Column(db.Integer)
    is_correct = db.Column(db.Boolean)
    points = db.Column(db.Integer)

    question_id = db.Column(db.Integer, db.ForeignKey('Questions.id'))
    choice_id = db.Column(db.Integer, db.ForeignKey('Choices.id'))

    def json(self):
        return {
            'id': self.id,
            'is_correct': self.is_correct,
            'points': self.points,
            'index': self.index,
            'content': Choice.query.filter_by(id=self.choice_id).first().json(),
        }


class Choice(db.Model):
    __tablename__ = 'Choices'

    id = db.Column(db.Integer, primary_key=True)
    choice_fa = db.Column(db.String(80))
    choice_en = db.Column(db.String(80), nullable=True)
    # index = db.Column(db.Integer)
    # points = db.Column(db.Integer)
    choice_image = db.Column(db.String(80), nullable=True)
    # is_correct = db.Column(db.Boolean)

    # question_id = db.Column(db.Integer, db.ForeignKey('Questions.id'))
    # question = db.relationship('Question')

    def __init__(self, choice_fa, index, points, question_id, is_correct):
        self.choice_fa = choice_fa
        # self.is_correct = is_correct
        # self.index = index
        # self.points = points
        self.question_id = question_id
        self.choice_image = ""

    def json(self):
        return {
            'id': self.id,
            'choice_fa': self.choice_fa,
            'choice_en': self.choice_en,
            # 'is_correct': self.is_correct,
            # 'points': self.points,
            # 'index': self.index,
            'choice_image': self.choice_image,
        }

