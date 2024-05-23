from calculator.calculator import Calculator

class TestCalculator:
    def test_add(self):
        # arrange
        a = 4321
        b = 1234
        cal = Calculator()

        # act
        result = cal.add(a, b)

        # assert
        expected = 5555
        assert result == expected
    
    
    def test_subtract(self):
        # arrange
        a = 4321
        b = 1234
        cal = Calculator()

        # act
        result = cal.subtract(a, b)

        # assert
        expected = 3087
        assert result == expected

    
    
    def test_multiply(self):
        # arrange
        a = 4321
        b = 1234
        cal = Calculator()

        # act
        result = cal.multiply(a, b)

        # assert
        expected = 5332114
        assert result == expected

    
    
    def test_divide(self):
        # arrange
        a = 4321
        b = 1234
        cal = Calculator()

        # act
        result = cal.divide(a, b)

        # assert
        expected = 4321 / 1234
        assert result == expected


    def test_divide_by_zero(self):
        cal = Calculator()
        a, b = 4321, 0

        try:
            cal.divide(a, b)
        except ZeroDivisionError as e:
            assert str(e) == "Division by zero error"


