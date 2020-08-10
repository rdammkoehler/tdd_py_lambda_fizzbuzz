def lambda_function(event, context):
    return '1'


def test_lambda_function_fizz_buzz_returns_one_given_one():
    assert lambda_function({'given': 1}, None) == '1'
