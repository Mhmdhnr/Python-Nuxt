from flask_login import current_user
from models.user_test_results import UserTestResults, UserRavenResults, UserMBTIResults, UserHollandResults, UserJohnsonResults, UserGlasserResults, UserStephenResults


def get_user_test_results():
    user_test_results = UserTestResults.query.filter_by(user_id=current_user.id).first()
    if user_test_results:
        pass
    else:
        user_test_results = UserTestResults(current_user.id)
        user_test_results.save_to_db()
    if UserRavenResults.query.filter_by(user_id=current_user.id).first():
        user_raven_results = UserRavenResults.query.filter_by(user_id=current_user.id).first()
    else:
        user_raven_results = UserRavenResults(current_user.id, 0, 0, 0)
        user_raven_results.save_to_db()
    if UserMBTIResults.query.filter_by(user_id=current_user.id).first():
        user_mbti_results = UserMBTIResults.query.filter_by(user_id=current_user.id).first()
    else:
        user_mbti_results = UserMBTIResults(current_user.id, "", "", 0, "", 0, "", 0, "", 0)
        user_mbti_results.save_to_db()
    if UserHollandResults.query.filter_by(user_id=current_user.id).first():
        user_holland_results = UserHollandResults.query.filter_by(user_id=current_user.id).first()
    else:
        user_holland_results = UserHollandResults(current_user.id, 0, 0, 0, 0, 0, 0)
        user_holland_results.save_to_db()
    if UserJohnsonResults.query.filter_by(user_id=current_user.id).first():
        user_johnson_results = UserJohnsonResults.query.filter_by(user_id=current_user.id).first()
    else:
        user_johnson_results = UserJohnsonResults(current_user.id, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        user_johnson_results.save_to_db()
    if UserGlasserResults.query.filter_by(user_id=current_user.id).first():
        user_glasser_results = UserGlasserResults.query.filter_by(user_id=current_user.id).first()
    else:
        user_glasser_results = UserGlasserResults(current_user.id, 0, 0, 0, 0, 0)
        user_glasser_results.save_to_db()
    if UserStephenResults.query.filter_by(user_id=current_user.id).first():
        user_stephen_results = UserStephenResults.query.filter_by(user_id=current_user.id).first()
    else:
        user_stephen_results = UserStephenResults(current_user.id, 0, 0, 0)
        user_stephen_results.save_to_db()
    return {
        'user_test_result': user_test_results.json(),
        'user_raven_results': user_raven_results.json(),
        'user_mbti_results': user_mbti_results.json(),
        'user_holland_results': user_holland_results.json(),
        'user_johnson_results': user_johnson_results.json(),
        'user_glasser_results': user_glasser_results.json(),
        'user_stephen_results': user_stephen_results.json(),
    }

