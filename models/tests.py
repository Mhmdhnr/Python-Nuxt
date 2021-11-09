from db import db


class Tests(db.Model):
    __tablename__ = 'Tests'

    id = db.Column(db.Integer, primary_key=True)
    name_fa = db.Column(db.String(80))
    name_en = db.Column(db.String(80))

    def __init__(self, name_fa, name_en):
        self.name_fa = name_fa
        self.name_en = name_en

    def json(self):
        return {
            'id': self.id,
            'name_fa': self.name_fa,
            'name_en': self.name_en
        }


class Question:
    def __init__(self, question_fa, question_en, choices):
        self.question_fa = question_fa
        self.question_en = question_en

    def json(self):
        return {
            # 'id': self.id,
            'question_fa': self.question_fa,
            'question_en': self.question_en
        }


class Choice:
    def __init__(self, choice_fa, choice_en, index):
        self.choice_fa = choice_fa
        self.choice_en = choice_en
        self.index = index

    def json(self):
        return {
            'choice_fa': self.choice_fa,
            'choice_en': self.choice_en,
            'index': self.index
        }

