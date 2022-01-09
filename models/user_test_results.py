from db import db


class UserTestResults(db.Model):
    __tablename__ = 'UserTestResults'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('Users.id'))
    raven = db.Column(db.Boolean)
    mbti = db.Column(db.Boolean)
    johnson = db.Column(db.Boolean)
    holland = db.Column(db.Boolean)

    def __init__(self, user_id):
        self.user_id = user_id
        self.raven = False
        self.mbti = False
        self.johnson = False
        self.holland = False

    def json(self):
        return {
            'user_id': self.id,
            'raven': self.raven,
            'mbti': self.mbti,
            'johnson': self.johnson,
            'holland': self.holland,
            }

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()


class UserRavenResults(db.Model):
    __tablename__ = 'UserRavenResults'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('Users.id'))
    age = db.Column(db.Integer, nullable=False)
    correct_count = db.Column(db.Integer, nullable=False)
    iq = db.Column(db.Integer, nullable=False)

    def __init__(self, user_id, age, correct_count, iq):
        self.user_id = user_id
        self.age = age
        self.correct_count = correct_count
        self.iq = iq

    def json(self):
        return {
            'user_id': self.id,
            'age': self.age,
            'correct_count': self.correct_count,
            'iq': self.iq,
            }

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()


class UserMBTIResults(db.Model):
    __tablename__ = 'UserMBTIResults'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('Users.id'))
    type = db.Column(db.String(8), nullable=False)
    ei = db.Column(db.String(8), nullable=False)
    ei_value = db.Column(db.Integer, nullable=False)
    sn = db.Column(db.String(8), nullable=False)
    sn_value = db.Column(db.Integer, nullable=False)
    tf = db.Column(db.String(8), nullable=False)
    tf_value = db.Column(db.Integer, nullable=False)
    jp = db.Column(db.String(8), nullable=False)
    jp_value = db.Column(db.Integer, nullable=False)

    def __init__(self, user_id, type, ei, ei_value, sn, sn_value, tf, tf_value, jp, jp_value):
        self.user_id = user_id
        self.type = type
        self.ei = ei
        self.ei_value = ei_value
        self.sn = sn
        self.sn_value = sn_value
        self.tf = tf
        self.tf_value = tf_value
        self.jp = jp
        self.jp_value = jp_value

    def json(self):
        return {
            'user_id': self.user_id,
            'type': self.type,
            'ei': {
                'result': self.ei,
                'value': self.ei_value,
            },
            'sn': {
                'result': self.sn,
                'value': self.sn_value,
            },
            'tf': {
                'result': self.tf,
                'value': self.tf_value,
            },
            'jp': {
                'result': self.jp,
                'value': self.jp_value,
            }
        }

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()


class UserHollandResults(db.Model):
    __tablename__ = 'UserHollandResults'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('Users.id'))
    realistic = db.Column(db.Integer, nullable=False)
    investigative = db.Column(db.Integer, nullable=False)
    artistic = db.Column(db.Integer, nullable=False)
    social = db.Column(db.Integer, nullable=False)
    enterprising = db.Column(db.Integer, nullable=False)
    conventional = db.Column(db.Integer, nullable=False)

    def __init__(self, user_id, realistic, investigative, artistic, social, enterprising, conventional):
        self.user_id = user_id
        self.realistic = realistic
        self.investigative = investigative
        self.artistic = artistic
        self.social = social
        self.enterprising = enterprising
        self.conventional = conventional

    def json(self):
        return {
            'user_id': self.user_id,
            'realistic': self.realistic,
            'investigative': self.investigative,
            'artistic': self.artistic,
            'social': self.social,
            'enterprising': self.enterprising,
            'conventional': self.conventional,
        }

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()


class UserJohnsonResults(db.Model):
    __tablename__ = 'UserJohnsonResults'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('Users.id'))
    aptitude_1 = db.Column(db.Integer, nullable=False)
    aptitude_2 = db.Column(db.Integer, nullable=False)
    aptitude_3 = db.Column(db.Integer, nullable=False)
    aptitude_4 = db.Column(db.Integer, nullable=False)
    aptitude_5 = db.Column(db.Integer, nullable=False)
    aptitude_6 = db.Column(db.Integer, nullable=False)
    aptitude_7 = db.Column(db.Integer, nullable=False)
    aptitude_8 = db.Column(db.Integer, nullable=False)
    aptitude_9 = db.Column(db.Integer, nullable=False)
    aptitude_10 = db.Column(db.Integer, nullable=False)
    aptitude_11 = db.Column(db.Integer, nullable=False)
    aptitude_12 = db.Column(db.Integer, nullable=False)

    def __init__(self, user_id, aptitude_1, aptitude_2, aptitude_3, aptitude_4, aptitude_5, aptitude_6, aptitude_7, aptitude_8, aptitude_9, aptitude_10, aptitude_11, aptitude_12):
        self.user_id = user_id
        self.aptitude_1 = aptitude_1
        self.aptitude_2 = aptitude_2
        self.aptitude_3 = aptitude_3
        self.aptitude_4 = aptitude_4
        self.aptitude_5 = aptitude_5
        self.aptitude_6 = aptitude_6
        self.aptitude_7 = aptitude_7
        self.aptitude_8 = aptitude_8
        self.aptitude_9 = aptitude_9
        self.aptitude_10 = aptitude_10
        self.aptitude_11 = aptitude_11
        self.aptitude_12 = aptitude_12

    def json(self):
        return {
            'user_id': self.user_id,
            'aptitude_1': self.aptitude_1,
            'aptitude_2': self.aptitude_2,
            'aptitude_3': self.aptitude_3,
            'aptitude_4': self.aptitude_4,
            'aptitude_5': self.aptitude_5,
            'aptitude_6': self.aptitude_6,
            'aptitude_7': self.aptitude_7,
            'aptitude_8': self.aptitude_8,
            'aptitude_9': self.aptitude_9,
            'aptitude_10': self.aptitude_10,
            'aptitude_11': self.aptitude_11,
            'aptitude_12': self.aptitude_12,
        }

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

