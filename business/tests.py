import json
from models.tests import TestAnswers


def calculate_raven_result(response):
    res = json.loads(response).get('responses')
    answers = TestAnswers.query.filter_by(test_id=2).all()
    correct_count = 0
    print(answers)
    print(res)
    for i in range(60):
        if answers[i].answer_index == res[i]:
            correct_count += 1

    result = [51, 51, 51, 51, 51, 51, 51, 51, 51, 54, 58, 61, 62, 64, 66, 68, 69, 71, 72, 74, 75, 76, 78, 79, 80, 81,
              82, 83, 85, 86, 87, 88, 89, 91, 92, 93, 94, 96, 97, 98, 100, 101, 102, 104, 106, 107, 109, 111, 112, 114,
              116, 118, 120, 122, 124, 126, 127, 131, 133, 136]

    iq = result[0] if correct_count == 0 else result[correct_count - 1]

    return {'iq': iq,
            'correct': correct_count}
