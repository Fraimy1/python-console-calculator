import pytest
from src.calculator import Calculator
tests = [
    ('3 2 4 ** +', 19),
    ('5 1 2 + 4 ** + 3 -', 83),
    ('10 3 // 2 *', 6),
    ('20 3 % 2 +', 4),
    ('2 3 + 4 *', 20),
    ('2 3 4 * +', 14),
    ('2 +2 +', 4),
    ('5 -78 +', -73),
    ('3 2 1 + *', 9),
    ('6 2 3 ** /', 0.75),
]

calc = Calculator()

@pytest.mark.parametrize('expr,expected', tests)
def test_calculator(expr, expected):
    assert calc.calculate_rpn(expr) == pytest.approx(expected)