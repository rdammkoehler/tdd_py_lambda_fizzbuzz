def lambda_function(event, context):
    given = event['given']
    if given % 3 == 0:
        return 'fizz'
    if given == 5:
        return 'buzz'
    return str(given)


def test_lambda_function_fizz_buzz_returns_one_given_one():
    assert lambda_function(event={'given': 1}, context=None) == '1'


def test_lambda_function_fizz_buzz_returns_two_given_two():
    assert lambda_function(event={'given': 2}, context=None) == '2'


def test_lambda_function_fizz_buzz_returns_fizz_given_three():
    assert lambda_function(event={'given': 3}, context=None) == 'fizz'


def test_lambda_function_fizz_buzz_returns_fizz_given_six():
    assert lambda_function(event={'given': 6}, context=None) == 'fizz'


def test_lambd_function_fizz_buzz_returns_buzz_given_five():
    assert lambda_function(event={'given': 5}, context=None) == 'buzz'
