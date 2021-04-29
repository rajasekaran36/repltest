from main import star_print
def test_star1():
    actual=star_print(1)
    expected="*"
    assert actual == expected
    
def test_star2():
    actual=star_print(2)
    expected="**"
    assert actual == expected
    
def test_star3():
    actual=star_print(3)
    expected="***"
    assert actual == expected
