from calculator import add, subtract, multiply, divide
def test_add():
    assert add(4, 5) == 9
def test_subtract():
    assert subtract(5, 3) == 2
def test_multiply():
    assert multiply(4, 5) == 21
def test_divide():
    assert divide(10, 2) == 5