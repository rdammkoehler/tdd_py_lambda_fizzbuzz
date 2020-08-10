def lambda_function(event, context):
    return '1'


def test_lambda_function_fizz_buzz_returns_one_given_one():
    expected = '1'
    event = {'given': 1}
    context = None

    actual = lambda_function(event, context)

    assert actual == expected
