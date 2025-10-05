import pytest
from src.calculator import Calculator

tests = [
    # Basic arithmetic
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

    # Exponentiation and chaining
    ('2 3 ** 2 **', 64),           # 2^(3^2) = 64
    ('2 3 2 ** **', 512),          # (2^3)^2 = 512
    ('9 0.5 **', 3),               # sqrt(9) = 3

    # Mixed operators with precedence
    ('5 1 2 + 4 ** + 3 -', 83),
    ('3 4 * 2 5 * +', 22),
    ('10 2 5 + *', 70),
    ('100 5 / 2 -', 18),

    # Unary and negative handling
    ('-3 -2 *', 6),
    ('-3 2 **', 9),
    ('2 -3 **', 0.125),
    ('-5 -2 **', 0.04),

    # Integer division and modulo
    ('7 3 //', 2),
    ('7 3 %', 1),
    ('10 4 % 3 +', 5),

    # Complex nesting simulation
    ('3 5 2 * + 8 4 / -', 11),       # (3 + 10) - 2 = 11 - 3 = 11
    ('2 3 4 + * 5 6 * +', 44),
    ('10 2 3 ** *', 80),             # 10 * (2^3) = 80

    # Floating point
    ('5.5 2 *', 11.0),
    ('3.2 1.2 + 2 *', 8.8),

    # Division by float
    ('6 4 /', 1.5),
    ('5 2 /', 2.5),
]

calc = Calculator()

@pytest.mark.parametrize('expr,expected', tests)
def test_calculator(expr, expected):
    assert calc.calculate_rpn(expr) == pytest.approx(expected)