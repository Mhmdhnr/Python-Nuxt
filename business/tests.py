import json
from flask_login import current_user
from models.tests import Question, QuestionChoices
from models.user_test_results import UserTestResults, UserRavenResults, UserMBTIResults, UserHollandResults, UserJohnsonResults
import math


def calculate_raven_result(response):

    result_plus_18 = [136, 133, 131, 127, 126, 124, 122, 120, 118, 116, 114, 112, 111, 109, 107, 106, 104, 102, 101,
                      100, 98, 97, 96, 94, 93, 92, 91, 89, 88, 87, 86, 85, 83, 82, 81, 80, 79, 78, 76, 75, 74, 72, 71,
                      69, 68, 66, 64, 62, 61, 58, 54, 51, 51, 51, 51, 51, 51, 51, 51, 51]

    result_17 = [138, 136, 134, 131, 129, 126, 124, 122, 120, 119, 117, 115, 113, 112, 110, 108, 107, 105, 104, 102,
                 100, 99, 98, 86, 95, 94, 93, 90, 90, 89, 88, 87, 86, 84, 83, 82, 81, 81, 79, 78, 76, 75, 74, 72, 70,
                 69, 67, 65, 63, 60, 68, 54, 51, 51, 51, 51, 51, 51, 51, 51]

    result_16 = [141, 138, 137, 134, 131, 129, 126, 125, 123, 121, 119, 118, 116, 114, 112, 110, 109, 107, 106, 104,
                 102, 101, 100, 99, 98, 97, 96, 94, 93, 92, 91, 90, 89, 88, 86, 85, 84, 83, 81, 80, 79, 77, 76, 74, 72,
                 71, 69, 67, 64, 62, 60, 56, 54, 51, 51, 51, 51, 51, 51, 51]

    result_15 = [144, 140, 138, 136, 134, 132, 130, 128, 126, 124, 122, 121, 119, 117, 115, 113, 112, 110, 108, 107,
                 105, 104, 102, 101, 100, 99, 98, 96, 95, 94, 93, 92, 90, 89, 88, 87, 86, 85, 84, 83, 82, 80, 79, 78,
                 76, 74, 72, 71, 69, 67, 63, 61, 58, 54, 51, 51, 51, 51, 51, 51]

    result_14 = [146, 144, 141, 139, 136, 134, 131, 129, 128, 127, 125, 124, 122, 120, 119, 117, 116, 114, 113, 111,
                 110, 109, 107, 106, 105, 104, 103, 102, 101, 100, 99, 98, 97, 96, 94, 93, 92, 91, 89, 88, 87, 85, 84,
                 82, 81, 79, 77, 74, 72, 70, 68, 65, 61, 58, 54, 51, 51, 51, 51, 51]

    result_13 = [149, 146, 144, 140, 137, 136, 134, 132, 131, 129, 128, 127, 126, 124, 122, 121, 120, 119, 118, 117,
                 116, 115, 114, 113, 112, 111, 110, 109, 108, 107, 106, 105, 104, 103, 102, 101, 100, 98, 97, 96, 95,
                 93, 91, 90, 89, 87, 85, 82, 79, 77, 74, 71, 67, 63, 59, 54, 51, 51, 51, 51	]

    result_12 = [149, 149, 146, 142, 140, 137, 136, 134, 132, 131, 129, 128, 127, 126, 125, 124, 122, 121, 120, 119,
                 118, 117, 116, 115, 114, 113, 112, 111, 110, 109, 108, 107, 106, 105, 104, 103, 102, 101, 100, 99, 97,
                 96, 94, 93, 92, 90, 88, 87, 83, 81, 78, 73, 69, 64, 60, 56, 54, 51, 51, 51]

    result_11 = [149, 149, 149, 146, 141, 138, 137, 136, 135, 131, 131, 129, 128, 127, 126, 125, 124, 122, 121, 120,
                 119, 118, 117, 116, 115, 114, 113, 112, 111, 110, 109, 108, 107, 106, 105, 104, 103, 102, 101, 100,
                 99, 97, 96, 94, 93, 92, 90, 88, 87, 83, 81, 78, 73, 69, 64, 60, 56, 54, 51, 51]

    result_10 = [149, 149, 149, 149, 146, 144, 141, 140, 138, 137, 135, 134, 132, 131, 130, 128, 127, 126, 125, 124,
                 122, 121, 120, 119, 118, 117, 116, 115, 114, 113, 112, 111, 110, 109, 107, 106, 105, 104, 103, 102,
                 101, 99, 98, 96, 95, 93, 92, 89, 88, 86, 83, 80, 78, 75, 73, 66, 61, 56, 54, 51]

    result_9 = [149, 149, 149, 149, 149, 149, 149, 149, 149, 146, 144, 142, 140, 138, 137, 135, 134, 133, 131, 130,
                128, 127, 126, 125, 124, 122, 121, 120, 119, 117, 116, 115, 114, 113, 112, 111, 110, 108, 107, 106,
                105, 104, 102, 101, 100, 98, 96, 94, 92, 90, 87, 85, 82, 78, 75, 71, 66, 51, 56, 54]

    choices = json.loads(response).get('choices')
    age = json.loads(response).get('age')

    test_questions = Question.query.filter_by(test_id=2).all()
    test_questions_id = []
    for test_question in test_questions:
        test_questions_id.append(test_question.id)
    test_choices = QuestionChoices.query.filter(QuestionChoices.question_id.in_(test_questions_id)).all()
    # test_choices = Choice.query.filter(Choice.question_id.in_(test_questions_id)).all()
    correct_answers = []
    for i in range(60):
        question = next(test_question for test_question in test_questions if test_question.index == i + 1)
        question_choices = [test_choice for test_choice in test_choices if test_choice.question_id == question.id]
        print(question_choices)
        correct_choice = next(question_choice for question_choice in question_choices if question_choice.points == 1)
        correct_answers.append(correct_choice.index)
    print(correct_answers)

    correct_count = 0
    print(choices)
    for i in range(60):
        if correct_answers[i] == choices[i]:
            correct_count += 1

    iq = 0

    if age == 18:
        iq = result_plus_18[-1] if correct_count == 0 else result_plus_18[-correct_count]
    elif age == 17:
        iq = result_17[-1] if correct_count == 0 else result_17[-correct_count]
    elif age == 16:
        iq = result_16[-1] if correct_count == 0 else result_16[-correct_count]
    elif age == 15:
        iq = result_15[-1] if correct_count == 0 else result_15[-correct_count]
    elif age == 14:
        iq = result_14[-1] if correct_count == 0 else result_14[-correct_count]
    elif age == 13:
        iq = result_13[-1] if correct_count == 0 else result_13[-correct_count]
    elif age == 12:
        iq = result_12[-1] if correct_count == 0 else result_12[-correct_count]
    elif age == 11:
        iq = result_11[-1] if correct_count == 0 else result_11[-correct_count]
    elif age == 10:
        iq = result_10[-1] if correct_count == 0 else result_10[-correct_count]
    elif age == 9:
        iq = result_9[-1] if correct_count == 0 else result_9[-correct_count]

    user_results = UserTestResults.query.filter_by(user_id=current_user.id).first()
    if user_results:
        if user_results.raven:
            user_raven_results = UserRavenResults.query.filter_by(user_id=current_user.id).first()
            user_raven_results.correct_count = correct_count
            user_raven_results.iq = iq
            user_raven_results.save_to_db()
        else:
            user_results.raven = True
            user_results.save_to_db()
            user_raven_results = UserRavenResults(current_user.id, age, correct_count, iq)
            user_raven_results.save_to_db()
    else:
        pass

    return {
        'age': age,
        'iq': iq,
        'correct': correct_count
    }


def calculate_mbti_result(response):
    choices = json.loads(response).get('choices')
    print(choices)
    test_questions = Question.query.filter_by(test_id=1).all()
    test_questions_id = []
    for test_question in test_questions:
        test_questions_id.append(test_question.id)
    test_choices = QuestionChoices.query.filter(QuestionChoices.question_id.in_(test_questions_id)).all()
    ei_questions = [test_question for test_question in test_questions if test_question.indicator == 1]
    sn_questions = [test_question for test_question in test_questions if test_question.indicator == 2]
    tf_questions = [test_question for test_question in test_questions if test_question.indicator == 3]
    jp_questions = [test_question for test_question in test_questions if test_question.indicator == 4]

    client_e_point = 0
    client_i_point = 0
    client_s_point = 0
    client_n_point = 0
    client_t_point = 0
    client_f_point = 0
    client_j_point = 0
    client_p_point = 0
    for i in range(93):
        question = next(question for question in test_questions if question.index == i + 1)
        question_choices = [test_choice for test_choice in test_choices if test_choice.question_id == question.id]
        client_response = choices[i]
        if question.id in (question.id for question in ei_questions):
            if any(question_choice for question_choice in question_choices if question_choice.index == client_response):
                selected_choice = next(question_choice for question_choice in question_choices if question_choice.index == client_response)
                if selected_choice.points == 1:
                    client_e_point += 1
                else:
                    client_i_point += 1
        elif question.id in (question.id for question in sn_questions):
            if any(question_choice for question_choice in question_choices if question_choice.index == client_response):
                selected_choice = next(question_choice for question_choice in question_choices if question_choice.index == client_response)
                if selected_choice.points == 1:
                    client_s_point += 1
                else:
                    client_n_point += 1
        elif question.id in (question.id for question in tf_questions):
            if any(question_choice for question_choice in question_choices if question_choice.index == client_response):
                selected_choice = next(question_choice for question_choice in question_choices if question_choice.index == client_response)
                if selected_choice.points == 1:
                    client_t_point += 1
                else:
                    client_f_point += 1
        elif question.id in (question.id for question in jp_questions):
            if any(question_choice for question_choice in question_choices if question_choice.index == client_response):
                selected_choice = next(question_choice for question_choice in question_choices if question_choice.index == client_response)
                if selected_choice.points == 1:
                    client_j_point += 1
                else:
                    client_p_point += 1

    client_e_point = client_e_point + 1 if client_e_point == client_i_point else client_e_point
    client_ei = "E" if client_e_point > client_i_point else "I"
    client_ei_value = abs(client_e_point - client_i_point) / (client_e_point + client_i_point) * 50

    client_s_point = client_s_point + 1 if client_s_point == client_n_point else client_s_point
    client_sn = "S" if client_s_point > client_n_point else "N"
    client_sn_value = abs(client_s_point - client_n_point) / (client_s_point + client_n_point) * 50

    client_t_point = client_t_point + 1 if client_t_point == client_f_point else client_t_point
    client_tf = "T" if client_t_point > client_f_point else "F"
    client_tf_value = abs(client_t_point - client_f_point) / (client_t_point + client_f_point) * 50

    client_j_point = client_j_point + 1 if client_j_point == client_p_point else client_j_point
    client_jp = "J" if client_j_point > client_p_point else "P"
    client_jp_value = abs(client_j_point - client_p_point) / (client_j_point + client_p_point) * 50

    client_type = ""
    client_type = client_type + "E" if client_ei == "E" else client_type + "I"
    client_type = client_type + "S" if client_sn == "S" else client_type + "N"
    client_type = client_type + "T" if client_tf == "T" else client_type + "F"
    client_type = client_type + "J" if client_jp == "J" else client_type + "P"

    user_results = UserTestResults.query.filter_by(user_id=current_user.id).first()
    if user_results:
        if user_results.mbti:
            user_mbti_results = UserMBTIResults.query.filter_by(user_id=current_user.id).first()
            user_mbti_results.type = client_type
            user_mbti_results.ei = client_ei
            user_mbti_results.ei_value = math.floor(client_ei_value)
            user_mbti_results.sn = client_sn
            user_mbti_results.sn_value = math.floor(client_sn_value)
            user_mbti_results.tf = client_tf
            user_mbti_results.tf_value = math.floor(client_tf_value)
            user_mbti_results.jp = client_jp
            user_mbti_results.jp_value = math.floor(client_jp_value)
            user_mbti_results.save_to_db()
        else:
            user_results.mbti = True
            user_results.save_to_db()

            user_mbti_results = UserMBTIResults(current_user.id, client_type, client_ei, math.floor(client_ei_value),
                                                 client_sn, math.floor(client_sn_value), client_tf,
                                                 math.floor(client_tf_value), client_jp, math.floor(client_jp_value))
            user_mbti_results.save_to_db()
    else:
        pass

    return {
        'type': client_type,
        'EI': {
            'result': client_ei,
            'value': math.floor(client_ei_value),
        },
        'SN': {
            'result': client_sn,
            'value': math.floor(client_sn_value),
        },
        'TF': {
            'result': client_tf,
            'value': math.floor(client_tf_value),
        },
        'JP': {
            'result': client_jp,
            'value': math.floor(client_jp_value),
        },
    }


def calculate_holland_result(response):
    choices = json.loads(response).get('choices')
    print(choices)
    test_questions = Question.query.filter_by(test_id=3).all()
    test_questions_id = []
    for test_question in test_questions:
        test_questions_id.append(test_question.id)
    test_choices = QuestionChoices.query.filter(QuestionChoices.question_id.in_(test_questions_id)).all()
    r_questions = [test_question for test_question in test_questions if test_question.indicator == 1]
    i_questions = [test_question for test_question in test_questions if test_question.indicator == 2]
    a_questions = [test_question for test_question in test_questions if test_question.indicator == 3]
    s_questions = [test_question for test_question in test_questions if test_question.indicator == 4]
    e_questions = [test_question for test_question in test_questions if test_question.indicator == 5]
    c_questions = [test_question for test_question in test_questions if test_question.indicator == 6]
    client_r_points = 0
    client_i_points = 0
    client_a_points = 0
    client_s_points = 0
    client_e_points = 0
    client_c_points = 0
    for i in range(48):
        question = next(question for question in test_questions if question.index == i + 1)
        question_choices = [test_choice for test_choice in test_choices if test_choice.question_id == question.id]
        client_response = choices[i]
        if question.id in (question.id for question in r_questions):
            if any(question_choice for question_choice in question_choices if question_choice.index == client_response):
                selected_choice = next(question_choice for question_choice in question_choices if question_choice.index == client_response)
                client_r_points += selected_choice.points
        if question.id in (question.id for question in i_questions):
            if any(question_choice for question_choice in question_choices if question_choice.index == client_response):
                selected_choice = next(question_choice for question_choice in question_choices if question_choice.index == client_response)
                client_i_points += selected_choice.points
        if question.id in (question.id for question in a_questions):
            if any(question_choice for question_choice in question_choices if question_choice.index == client_response):
                selected_choice = next(question_choice for question_choice in question_choices if question_choice.index == client_response)
                client_a_points += selected_choice.points
        if question.id in (question.id for question in s_questions):
            if any(question_choice for question_choice in question_choices if question_choice.index == client_response):
                selected_choice = next(question_choice for question_choice in question_choices if question_choice.index == client_response)
                client_s_points += selected_choice.points
        if question.id in (question.id for question in e_questions):
            if any(question_choice for question_choice in question_choices if question_choice.index == client_response):
                selected_choice = next(question_choice for question_choice in question_choices if question_choice.index == client_response)
                client_e_points += selected_choice.points
        if question.id in (question.id for question in c_questions):
            if any(question_choice for question_choice in question_choices if question_choice.index == client_response):
                selected_choice = next(question_choice for question_choice in question_choices if question_choice.index == client_response)
                client_c_points += selected_choice.points

    user_results = UserTestResults.query.filter_by(user_id=current_user.id).first()
    if user_results:
        if user_results.holland:
            user_holland_results = UserHollandResults.query.filter_by(user_id=current_user.id).first()
            user_holland_results.realistic = math.floor(client_r_points / 40 * 100)
            user_holland_results.investigative = math.floor(client_i_points / 40 * 100)
            user_holland_results.artistic = math.floor(client_a_points / 40 * 100)
            user_holland_results.social = math.floor(client_s_points / 40 * 100)
            user_holland_results.enterprising = math.floor(client_e_points / 40 * 100)
            user_holland_results.conventional = math.floor(client_c_points / 40 * 100)
            user_holland_results.save_to_db()
        else:
            user_results.holland = True
            user_results.save_to_db()

            user_holland_results = UserHollandResults(current_user.id,
                                                      math.floor(client_r_points / 40 * 100),
                                                      math.floor(client_i_points / 40 * 100),
                                                      math.floor(client_a_points / 40 * 100),
                                                      math.floor(client_s_points / 40 * 100),
                                                      math.floor(client_e_points / 40 * 100),
                                                      math.floor(client_c_points / 40 * 100)
                                                      )
            user_holland_results.save_to_db()
    else:
        pass

    return {
        "R": math.floor(client_r_points / 40 * 100),
        "I": math.floor(client_i_points / 40 * 100),
        "A": math.floor(client_a_points / 40 * 100),
        "S": math.floor(client_s_points / 40 * 100),
        "E": math.floor(client_e_points / 40 * 100),
        "C": math.floor(client_c_points / 40 * 100),
    }


def calculate_johnson_result(response):
    choices = json.loads(response).get('choices')
    print(choices)
    test_questions = Question.query.filter_by(test_id=4).all()
    test_questions_id = []
    for test_question in test_questions:
        test_questions_id.append(test_question.id)
    test_choices = QuestionChoices.query.filter(QuestionChoices.question_id.in_(test_questions_id)).all()
    aptitude_1_questions = [test_question for test_question in test_questions if test_question.indicator == 1]
    aptitude_2_questions = [test_question for test_question in test_questions if test_question.indicator == 2]
    aptitude_3_questions = [test_question for test_question in test_questions if test_question.indicator == 3]
    aptitude_4_questions = [test_question for test_question in test_questions if test_question.indicator == 4]
    aptitude_5_questions = [test_question for test_question in test_questions if test_question.indicator == 5]
    aptitude_6_questions = [test_question for test_question in test_questions if test_question.indicator == 6]
    aptitude_7_questions = [test_question for test_question in test_questions if test_question.indicator == 7]
    aptitude_8_questions = [test_question for test_question in test_questions if test_question.indicator == 8]
    aptitude_9_questions = [test_question for test_question in test_questions if test_question.indicator == 9]
    aptitude_10_questions = [test_question for test_question in test_questions if test_question.indicator == 10]
    aptitude_11_questions = [test_question for test_question in test_questions if test_question.indicator == 11]
    aptitude_12_questions = [test_question for test_question in test_questions if test_question.indicator == 12]
    aptitude_1_points = 0
    aptitude_2_points = 0
    aptitude_3_points = 0
    aptitude_4_points = 0
    aptitude_5_points = 0
    aptitude_6_points = 0
    aptitude_7_points = 0
    aptitude_8_points = 0
    aptitude_9_points = 0
    aptitude_10_points = 0
    aptitude_11_points = 0
    aptitude_12_points = 0

    for i in range(58):
        question = next(question for question in test_questions if question.index == i + 1)
        question_choices = [test_choice for test_choice in test_choices if test_choice.question_id == question.id]
        client_response = choices[i]
        if question.id in (question.id for question in aptitude_1_questions):
            if any(question_choice for question_choice in question_choices if question_choice.index == client_response):
                selected_choice = next(question_choice for question_choice in question_choices if question_choice.index == client_response)
                aptitude_1_points += selected_choice.points
        if question.id in (question.id for question in aptitude_2_questions):
            if any(question_choice for question_choice in question_choices if question_choice.index == client_response):
                selected_choice = next(question_choice for question_choice in question_choices if question_choice.index == client_response)
                aptitude_2_points += selected_choice.points
        if question.id in (question.id for question in aptitude_3_questions):
            if any(question_choice for question_choice in question_choices if question_choice.index == client_response):
                selected_choice = next(question_choice for question_choice in question_choices if question_choice.index == client_response)
                aptitude_3_points += selected_choice.points
        if question.id in (question.id for question in aptitude_4_questions):
            if any(question_choice for question_choice in question_choices if question_choice.index == client_response):
                selected_choice = next(question_choice for question_choice in question_choices if question_choice.index == client_response)
                aptitude_4_points += selected_choice.points
        if question.id in (question.id for question in aptitude_5_questions):
            if any(question_choice for question_choice in question_choices if question_choice.index == client_response):
                selected_choice = next(question_choice for question_choice in question_choices if question_choice.index == client_response)
                aptitude_5_points += selected_choice.points
        if question.id in (question.id for question in aptitude_6_questions):
            if any(question_choice for question_choice in question_choices if question_choice.index == client_response):
                selected_choice = next(question_choice for question_choice in question_choices if question_choice.index == client_response)
                aptitude_6_points += selected_choice.points
        if question.id in (question.id for question in aptitude_7_questions):
            if any(question_choice for question_choice in question_choices if question_choice.index == client_response):
                selected_choice = next(question_choice for question_choice in question_choices if question_choice.index == client_response)
                aptitude_7_points += selected_choice.points
        if question.id in (question.id for question in aptitude_8_questions):
            if any(question_choice for question_choice in question_choices if question_choice.index == client_response):
                selected_choice = next(question_choice for question_choice in question_choices if question_choice.index == client_response)
                aptitude_8_points += selected_choice.points
        if question.id in (question.id for question in aptitude_9_questions):
            if any(question_choice for question_choice in question_choices if question_choice.index == client_response):
                selected_choice = next(question_choice for question_choice in question_choices if question_choice.index == client_response)
                aptitude_9_points += selected_choice.points
        if question.id in (question.id for question in aptitude_10_questions):
            if any(question_choice for question_choice in question_choices if question_choice.index == client_response):
                selected_choice = next(question_choice for question_choice in question_choices if question_choice.index == client_response)
                aptitude_10_points += selected_choice.points
        if question.id in (question.id for question in aptitude_11_questions):
            if any(question_choice for question_choice in question_choices if question_choice.index == client_response):
                selected_choice = next(question_choice for question_choice in question_choices if question_choice.index == client_response)
                aptitude_11_points += selected_choice.points
        if question.id in (question.id for question in aptitude_12_questions):
            if any(question_choice for question_choice in question_choices if question_choice.index == client_response):
                selected_choice = next(question_choice for question_choice in question_choices if question_choice.index == client_response)
                aptitude_12_points += selected_choice.points

    user_results = UserTestResults.query.filter_by(user_id=current_user.id).first()
    if user_results:
        if user_results.johnson:
            user_johnson_results = UserJohnsonResults.query.filter_by(user_id=current_user.id).first()
            user_johnson_results.aptitude_1 = math.floor(aptitude_1_points / len(aptitude_1_questions) * 100),
            user_johnson_results.aptitude_2 = math.floor(aptitude_2_points / len(aptitude_2_questions) * 100),
            user_johnson_results.aptitude_3 = math.floor(aptitude_3_points / len(aptitude_3_questions) * 100),
            user_johnson_results.aptitude_4 = math.floor(aptitude_4_points / len(aptitude_4_questions) * 100),
            user_johnson_results.aptitude_5 = math.floor(aptitude_5_points / len(aptitude_5_questions) * 100),
            user_johnson_results.aptitude_6 = math.floor(aptitude_6_points / len(aptitude_6_questions) * 100),
            user_johnson_results.aptitude_7 = math.floor(aptitude_7_points / len(aptitude_7_questions) * 100),
            user_johnson_results.aptitude_8 = math.floor(aptitude_8_points / len(aptitude_8_questions) * 100),
            user_johnson_results.aptitude_9 = math.floor(aptitude_9_points / len(aptitude_9_questions) * 100),
            user_johnson_results.aptitude_10 = math.floor(aptitude_10_points / len(aptitude_10_questions) * 100),
            user_johnson_results.aptitude_11 = math.floor(aptitude_11_points / len(aptitude_11_questions) * 100),
            user_johnson_results.aptitude_12 = math.floor(aptitude_12_points / len(aptitude_12_questions) * 100),
            user_johnson_results.save_to_db()
        else:
            user_results.johnson = True
            user_results.save_to_db()

            user_johnson_results = UserJohnsonResults(current_user.id,
                                                      math.floor(aptitude_1_points / len(aptitude_1_questions) * 100),
                                                      math.floor(aptitude_2_points / len(aptitude_2_questions) * 100),
                                                      math.floor(aptitude_3_points / len(aptitude_3_questions) * 100),
                                                      math.floor(aptitude_4_points / len(aptitude_4_questions) * 100),
                                                      math.floor(aptitude_5_points / len(aptitude_5_questions) * 100),
                                                      math.floor(aptitude_6_points / len(aptitude_6_questions) * 100),
                                                      math.floor(aptitude_7_points / len(aptitude_7_questions) * 100),
                                                      math.floor(aptitude_8_points / len(aptitude_8_questions) * 100),
                                                      math.floor(aptitude_9_points / len(aptitude_9_questions) * 100),
                                                      math.floor(aptitude_10_points / len(aptitude_10_questions) * 100),
                                                      math.floor(aptitude_11_points / len(aptitude_11_questions) * 100),
                                                      math.floor(aptitude_12_points / len(aptitude_12_questions) * 100),
                                                      )
            user_johnson_results.save_to_db()
    else:
        pass

    return {
        'aptitude_1': math.floor(aptitude_1_points / len(aptitude_1_questions) * 100),
        'aptitude_2': math.floor(aptitude_2_points / len(aptitude_2_questions) * 100),
        'aptitude_3': math.floor(aptitude_3_points / len(aptitude_3_questions) * 100),
        'aptitude_4': math.floor(aptitude_4_points / len(aptitude_4_questions) * 100),
        'aptitude_5': math.floor(aptitude_5_points / len(aptitude_5_questions) * 100),
        'aptitude_6': math.floor(aptitude_6_points / len(aptitude_6_questions) * 100),
        'aptitude_7': math.floor(aptitude_7_points / len(aptitude_7_questions) * 100),
        'aptitude_8': math.floor(aptitude_8_points / len(aptitude_8_questions) * 100),
        'aptitude_9': math.floor(aptitude_9_points / len(aptitude_9_questions) * 100),
        'aptitude_10': math.floor(aptitude_10_points / len(aptitude_10_questions) * 100),
        'aptitude_11': math.floor(aptitude_11_points / len(aptitude_11_questions) * 100),
        'aptitude_12': math.floor(aptitude_12_points / len(aptitude_12_questions) * 100),
    }



