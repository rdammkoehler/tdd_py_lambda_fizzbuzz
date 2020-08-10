def lambda_function(event, context):
    return str(event['given'])


def test_lambda_function_fizz_buzz_returns_one_given_one():
    assert lambda_function(event={'given': 1}, context=None) == '1'


def test_lambda_function_fizz_buzz_returns_two_given_two():
    assert lambda_function(event={'given': 2}, context=None) == '2'
