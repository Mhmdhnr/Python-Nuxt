import json


def calculate_raven_result(response):
    res = json.loads(response)
    return {'result': res}
