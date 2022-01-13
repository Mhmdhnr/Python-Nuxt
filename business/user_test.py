from flask_login import current_user
from models.user_test_results import UserTestResults, UserRavenResults, UserMBTIResults, UserHollandResults, UserJohnsonResults, UserGlasserResults


def get_user_test_results():
    user_test_results = UserTestResults.query.filter_by(user_id=current_user.id).first()
    user_raven_results = UserRavenResults.query.filter_by(user_id=current_user.id).first()
    user_mbti_results = UserMBTIResults.query.filter_by(user_id=current_user.id).first()
    user_holland_results = UserHollandResults.query.filter_by(user_id=current_user.id).first()
    user_johnson_results = UserJohnsonResults.query.filter_by(user_id=current_user.id).first()
    user_glasser_results = UserGlasserResults.query.filter_by(user_id=current_user.id).first()
    return {
        'user_test_result': user_test_results.json(),
        'user_raven_results': user_raven_results.json(),
        'user_mbti_results': user_mbti_results.json(),
        'user_holland_results': user_holland_results.json(),
        'user_johnson_results': user_johnson_results.json(),
        'user_glasser_results': user_glasser_results.json(),
    }

