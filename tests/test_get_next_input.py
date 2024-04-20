from get_next_input import get_next_input


# The monkeypatch pytest fixture is used to simulate user input, so we can test each possible input
def test_get_next_input_option1(monkeypatch):
    """Simulates a user input of 1 to test the response of 'get_next_input' function."""

    # Monkeypatch the input function so that it returns '1', simulating the user entering '1'
    monkeypatch.setattr('builtins.input', lambda _: '1')
    assert get_next_input() == 1


# The monkeypatch pytest fixture is used to simulate user input, so we can test each possible input
def test_get_next_input_option2(monkeypatch):
    """Simulates a user input of 2 to test the response of 'get_next_input' function."""

    # Monkeypatch the input function so that it returns '1', simulating the user entering '2'
    monkeypatch.setattr('builtins.input', lambda _: '2')
    assert get_next_input() == 2


# The monkeypatch pytest fixture is used to simulate user input, so we can test each possible input
def test_get_next_input_option3(monkeypatch):
    """Simulates a user input of 3 to test the response of 'get_next_input' function."""

    # Monkeypatch the input function so that it returns '3', simulating the user entering '3'
    monkeypatch.setattr('builtins.input', lambda _: '3')
    assert get_next_input() == 3


# The monkeypatch pytest fixture is used to simulate user input, so we can test each possible input
def test_get_next_input_option4(monkeypatch):
    """Simulates a user input of 4 to test the response of 'get_next_input' function."""

    # Monkeypatch the input function so that it returns '4', simulating the user entering '4'
    monkeypatch.setattr('builtins.input', lambda _: '4')
    assert get_next_input() == 4