import pytest
from src.calculator import Calculator

success_cases = [
    # Basic arithmetic
    ('3   2  +', 5),
    ('5 1 2 + 4 ** + 3 -', 83), # mixed ops
    (' 6  4 / ', 1.5), # float division
    ('10 3 //', 6), # division
    ('20 3 %', 2),
    ('5 -78 +', -73), # unary minus
    ('5 +78 -', -73), # unary plus
    
    # Order in chaining check
    ('2 3 2 ** **', 512), # (2^3)^2 = 64
    ('2 3 ** 2 **', 64), # 2^(3^2) = 512

    # Operations with parentheses
    ('(2)', 2),
    ('(3 ( 2 1 + ) *)', 9),
    ('( 3 4 +) (5 2 - ) *', 21),
    ('(3 (2 1 +) *)', 9),

    # 1_000 syntax check
    ('2_000_000 2_000 +', 2002000),
    ('1_000.500_000 + 1.5', 1002.0),

    # Complex nesting simulation
    ('3 5 2 * + 8 4 / -', 11), # 5*2 + 3 - 8/4 = 10 + 3 - 2 = 11 
    ('2 3 4 + * 5 6 * +', 44), # (3+4) * 2 + 5*6 = 14 + 30 = 44
    ('10 2 3 ** *', 80), # 2^3 * 10 = 8 * 10 = 80
]

error_cases = [

]

calc = Calculator()

@pytest.mark.parametrize('expr,expected', success_cases)
def test_calculator(expr, expected):
    assert calc.calculate_rpn(expr) == pytest.approx(expected)